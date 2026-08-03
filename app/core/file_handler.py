import os
import uuid
import shutil
from fastapi import UploadFile


default_dir = "uploads"


def save_image(image: UploadFile):
    os.makedirs(default_dir,exist_ok=True)
    extension = os.path.splitext(image.filename)[1]
    file_name = f"{uuid.uuid4()}{extension}"
    location = os.path.join(default_dir,file_name)
    with open(location,"wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return file_name