from django.shortcuts import render

# Create your views here.


from rest_framework import status, views
from rest_framework.response import Response
from .models import AudioFile
from .serializers import AudioFileSerializer


class AudioFileList(views.APIView):
    def get(self, request):
        audio_files = AudioFile.objects.all()
        serializer = AudioFileSerializer(audio_files, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AudioFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
