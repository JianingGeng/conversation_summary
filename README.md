# conversation_summary

used to sumary a conversation text

API Section

1. Secure File Uploader/Ingester
   POST /api/upload: Uploads a file, performing security checks.
   GET /api/files: Lists all uploaded files.
   DELETE /api/files/{fileId}: Deletes a specific file.

2. Text NLP Analysis
   (Utilizing Hugging Face's Transformers)

POST /api/analyze/text
Description: Use Hugging Face's Transformers, choose a BART based model to generate a concise summary of a conversation text.
Request Body: JSON object with a text field containing the text to summarize.
Response: JSON object with a summary field, presenting the result.

Environment Setup

- python -m venv ec530
- .\ec530\Scripts\activate

Starting the Django Development Server

- python manage.py runserver
  Deactivating the Virtual Environment
- deactivate

git remote add origin https://github.com/JianingGeng/conversation_summary.git
