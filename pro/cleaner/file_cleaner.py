import os

def clean_folder(folder):
    if not os.path.exists(folder):
        print("Folder not found.")
        return

    deleted = 0
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) == 0 or file.endswith(('.tmp', '.log')):
                os.remove(file_path)
                deleted += 1

    print(f"🧹 Removed {deleted} empty/temp files.")