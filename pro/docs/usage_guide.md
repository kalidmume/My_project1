# 📘 FileCleaner Usage Guide

## 1️⃣ Overview
FileCleaner automatically removes junk, empty, or duplicate files from a folder and organizes them by file type.

---

## 2️⃣ Steps to Run
1. Open the project folder:
   ```bash
   cd FileCleaner

2. Run the script:

python main.py


3. Enter the folder path you want to clean.


4. Check results:

Cleaned files are removed

Organized folders created

A report saved in outputs/report.txt





---

3️⃣ Example

Input:

/sdcard/Downloads

Output folders:

Downloads/
├── Documents/
├── Images/
├── Videos/
├── Others/

---

## 🧩 Step 6 — `README.md`
```markdown
# 🧹 FileCleaner

FileCleaner is a Python utility that automatically cleans junk, duplicate, and empty files from any folder — then organizes them by type.  
Fast, lightweight, and perfect for keeping storage clean!

---

## 🚀 Features
- Remove empty or temporary files  
- Delete duplicate files  
- Organize by file type (Documents, Images, etc.)  
- Lightweight and reusable  

---

## ⚙️ How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/KalidCode/FileCleaner.git
   cd FileCleaner

2. Run the script:

python main.py


3. Enter your folder path (e.g. /sdcard/Downloads)


4. Done ✅ — cleaned and organized automatically!




---

📸 Demo




---

📂 Folder Structure

FileCleaner/
├── main.py
├── cleaner/
├── docs/
├── images/
└── outputs/


---

📜 License

Licensed under the MIT License — see LICENSE.


---

👨‍💻 Author

KalidCode
Freelance Python Developer
🌐 GitHub: KalidCode

---

## 🧠 Step 7 — Git Commands to Upload
```bash
cd /sdcard/KalidCodeHub/FileCleaner
git init
git add .
git commit -m "Initial FileCleaner commit with docs and structure"
git branch -M main
git remote add origin https://github.com/KalidCode/FileCleaner.git
git push -u origin main

