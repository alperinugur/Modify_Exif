"""
Script to modify the 'UserComment' EXIF field in JPG files. 
User can extract the EXIF UserComment, modify it, and then save it back.
"""

from PIL import Image
from PIL.ExifTags import TAGS
import os
import piexif

DIRPATH = 'files'

def extract_exif_data(file_path):
    """
    Extract the 'UserComment' EXIF field from a JPG file.
    
    Args:
    - file_path (str): Path to the JPG file
    
    Returns:
    - str: The cleaned UserComment or None if EXIF data isn't present.
    """
    image = Image.open(file_path)
    exif_data = image._getexif()
    
    if not exif_data:
        return None

    labeled_exif_data = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}
    
    # Decode UserComment based on its encoding
    user_comment_text = ""
    if 'UserComment' in labeled_exif_data:
        user_comment_bytes = labeled_exif_data['UserComment']
        if user_comment_bytes.startswith(b"UNICODE\0"):
            user_comment_text = user_comment_bytes[8:].decode('utf-8')
        elif user_comment_bytes.startswith(b"ASCII\0"):
            user_comment_text = user_comment_bytes[6:].decode('ascii')
        else:
            user_comment_text = user_comment_bytes.decode('utf-8', 'ignore')

    cleaned_string = user_comment_text.replace("\x00", "")

    return cleaned_string

def dumpexifdata(file_path, new_file, newExif):
    """
    Save a JPG file with modified 'UserComment' EXIF data.

    Args:
    - file_path (str): Original file path
    - new_file (str): New file path for saved file with modified EXIF
    - newExif (str): Modified UserComment data

    Returns:
    - str: Path of the new file
    """
    exif_dict = piexif.load(file_path)
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = newExif.encode('utf-8')
    exif_bytes = piexif.dump(exif_dict)
    image = Image.open(file_path)
    image.save(new_file, exif=exif_bytes)
    
    return new_file


if __name__ == '__main__':

    os.system('cls' if os.name=='nt' else 'clear')

    jpg_files = [f for f in os.listdir(DIRPATH) if f.lower().endswith('.jpg')]
    
    if not jpg_files:
        print('No JPG / JPEG files found.')
        exit()

    first_file_path = os.path.join(DIRPATH, jpg_files[0])
    modified_file_path = os.path.splitext(first_file_path)[0] + '_EXIF.jpg'
    
    exif_data = extract_exif_data(first_file_path)
    print(f'\033[92m{exif_data}\033[00m\n')

    with open(os.path.join(DIRPATH, 'exif.txt'), 'w', encoding='utf-8') as f:
        f.write(exif_data)

    os.system('notepad.exe files/exif.txt')

    with open(os.path.join(DIRPATH, 'exif.txt'), 'r', encoding='utf-8') as f:
        new_exif = f.read()

    print(f'\033[96m{new_exif}\033[00m\n')

    dumpexifdata(first_file_path, modified_file_path, new_exif)
