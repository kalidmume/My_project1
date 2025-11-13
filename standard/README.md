
---

# 🧹 File Auto-Renamer (Standard Version)

---

## 📘 Description
A powerful and reliable Python tool that automatically **renames all files** in a selected folder while **creating a safe backup** and **tracking changes in a log file**.  
It ensures all files get unique, clean names like `file_1.jpg`, `file_2.pdf`, etc., and safely saves a backup copy before renaming.

This standard version is designed for freelancers and professionals who handle large file batches or client data with safety and clarity.

---

## ⚙️ Features
✅ Automatic renaming of all files in a folder  
✅ Creates a full backup before renaming  
✅ Keeps a detailed log of renamed files and errors  
✅ Handles duplicates safely and avoids overwriting  
✅ User-friendly console messages and progress display  
✅ Cross-platform support for Windows, Linux, macOS  

---

## 🗂️ Folder Structure
├── standard/
   │    │    ├── file_cleaner_standard.py
   │    │    ├── README.md
   │    │    ├── examples/
   │    │    │    ├── sample_input.txt
   │    │    │    ├── sample_output.txt
   │    │    │     |── rename_log.txt
   │    │    │    └── demo_folder/
   │    │    │         ├── file1.txt
   │    │    │         ├── file2.txt
---

## 🧠 How It Works
1. The script displays a banner and asks you to enter a folder path.  
2. It checks if the folder exists.  
3. Creates a backup folder automatically (`yourfolder_backup`).  
4. Renames each file with a clean numbered format (`file_1`, `file_2`, etc.).  
5. Logs every action in `rename_log.txt`.  
6. Shows a clear summary of renamed files.

---

## 🧩 Example Output

============================== === FILE RENAMER TOOLS ===

Enter folder path: /Documents/test 💥 /Documents/test backup to /Documents/test_backup 📦 Renamed: photo.jpg → file_1.jpg 📦 Renamed: report.pdf → file_2.pdf 🎯 Total Files renamed: 2 ✅️ File renamed Successfully!

---

## 📜 Usage
1. Copy the script into your project or working folder.  
2. Run it with Python (`python file_cleaner_standard.py`).  
3. Enter the folder path when asked.  
4. The tool automatically:
   - Creates a safe backup  
   - Renames all files  
   - Logs every rename result  

---

## 💡 Ideal Use Cases
- File organization for clients or deliveries  
- Backup and cleanup before project submission  
- Renaming media or document batches  
- Safe automation for business folders  

---

## 🧰 Requirements
- Python 3.8 or higher  
- Works on Windows, Linux, and macOS  

---

## 👨‍💻 Author
**Developer:** KalidCode  
**Focus:** Python Automation & Freelance Tools  
**Version:** Standard v1.0  
**Category:** File Management Automation


---
