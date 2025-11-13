import os
import logging 
logging.basicConfig(
    filename="rename_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_folder_path():
  """Function take from user folder path then check if correct else ask again and create backupfolder based on your folder base name main.
  return: folder path, backup
  """
  while True:
    #Get from user folder path
    folder = input("Enter folder path: ").strip()
    #Named backup based on folder path
    backup = folder + "_backup"
    #Check if folder path correct
    if os.path.exists(folder):
      #create backup if folder path correct
      os.makedirs(backup, exist_ok=True)
      try:
          shutil.copytree(folder, backup)
          print(f"💥 {folder} backup to {backu}")
      except Exception as error:
          print(f"❌️ Error backup: {error}")
      finally:
          return folder
    else:
      print("❌️ incorrect folder path, try again")


def auto_rename(folder):
    files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder, x)))
print(files)
    for count, filename in enumerate(files, 1):
        if filename == "rename_log.txt":
          continue
        ext = os.path.splitext(filename)[1]
        new_name = f"file_{count}{ext}"
        while os.path.exists(os.path.join(folder, new_name)):
            count += 1
            new_name = f"file_{count}{ext}"
            
        try:
            os.rename(os.path.join(folder, filename),
                  os.path.join(folder, new_name))
            print(f"📦 Renamed: {filename} → {new_name}")
            logging.info(f"📦 Renamed: {filename} → {new_name}")
        except Exception as error:
            print(f"Error: {error}")
            logging.error(f"Error: {error}")
    print(f"🎯 Total Files renamed: {len(files)}")
    print("✅️ File renamed Successfully!")


def main():
    print("=" * 30)
    print("=== FILE RENAMER TOOLS ===".center(30))
    print("=" * 30)
    
    folder = get_folder_path()
    auto_rename(folder)

main()
