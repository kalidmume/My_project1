import os, shutil

def organize_files(folder):
    types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Archives': ['.zip', '.rar'],
        'Others': []
    }

    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()

            target = next((k for k, v in types.items() if ext in v), 'Others')
            dest_dir = os.path.join(folder, target)

            os.makedirs(dest_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_dir, file))

    print("📁 Files organized successfully.")