# main.py
from cleaner.file_cleaner import clean_folder
from cleaner.duplicate_remover import remove_duplicates
from cleaner.organizer import organize_files

def main():
    print("=== FILE CLEANER ===")
    folder = input("Enter folder path to clean: ").strip()

    print("\n[1] Cleaning empty and temporary files...")
    clean_folder(folder)

    print("[2] Removing duplicates...")
    remove_duplicates(folder)

    print("[3] Organizing by file type...")
    organize_files(folder)

    print("\n✅ Cleaning complete! Check 'outputs/report.txt' for details.")

if __name__ == "__main__":
    main()