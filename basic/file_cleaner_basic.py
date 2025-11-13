import os
            
def auto_rename(folder):
    files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder,file))]
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    log_path = os.path.join(folder, "basic_log.txt")
    
    with open(log_path, "w", encoding="utf-8") as file:
        for count, filename in enumerate(files, 1):
            ext = os.path.splitext(filename)[1]
            new_name = f"file_{count}{ext}"
            
            while os.path.exists(os.path.join(folder, new_name)):
                count += 1
                new_name = f"file_{count}{ext}"
                
            try:
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
                print(f"📦 Renamed: {filename} → {new_name}")
                file.write(f"📦 Renamed: {filename} → {new_name}\n")
                   
            except Exception as error:
                print(f"Error: {error}")
                file.write(f"Error renamed: {error}\n")
                
        print(f"🎯 Total Files renamed: {len(files)}")
        print("✅️ File renamed Successfully!")

folder = input("Enter folder path: ").strip()
if not os.path.exists(folder):
    print("❌ Folder not found!")
    exit()
auto_rename(folder)
