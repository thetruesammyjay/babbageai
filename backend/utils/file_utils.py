import os
from werkzeug.utils import secure_filename

def save_uploaded_file(file, upload_folder):
    """
    Saves an uploaded file to the specified folder
    """
    try:
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    except Exception as e:
        raise Exception(f"Error saving uploaded file: {e}")