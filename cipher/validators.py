"""
Validators for the cipher app.
"""
import os
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile


def validate_file_extension(value: InMemoryUploadedFile):
    """
    Validate the file extension of the uploaded file.
    Accepts only .txt files.
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
