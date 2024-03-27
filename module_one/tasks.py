from celery import shared_task
from scipy.spatial.distance import cdist

import numpy as np
import glob
import shutil
import os

import torch
from pyannote.audio import Model, Inference


@shared_task
def process_inference(
    folder_path, folder_find, target_folder_path, model_path, threshold=0.6
):
    # 目标文件夹
    if not os.path.isdir(target_folder_path):
        os.makedirs(target_folder_path)

    # 加载模型并设置推理
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = Model.from_pretrained(model_path)
    model.to(device)
    inference = Inference(model, window="whole", device=device)

    # 提取 "speaker1" 的嵌入
    embeddings_speaker1 = []
    for audio_path in glob.glob(os.path.join(folder_path, "*.wav")):
        embedding = inference(audio_path)
        embeddings_speaker1.append(embedding)

    # 计算 "speaker1" 的平均嵌入
    mean_embedding_speaker1 = np.mean(embeddings_speaker1, axis=0)
    mean_embedding_speaker1 = mean_embedding_speaker1[np.newaxis, :]

    # 遍历目标文件夹中的音频文件
    for audio_path in glob.glob(os.path.join(folder_find, "*.wav")):
        try:
            embedding_other = inference(audio_path)
            embedding_other = embedding_other[np.newaxis, :]

            # 计算余弦距离
            distance = cdist(mean_embedding_speaker1, embedding_other, metric="cosine")[
                0, 0
            ]

            # 如果距离低于阈值，复制到目标文件夹
            if distance < threshold:
                shutil.copyfile(
                    audio_path,
                    os.path.join(target_folder_path, os.path.basename(audio_path)),
                )
        except Exception as e:
            # 处理异常
            continue
