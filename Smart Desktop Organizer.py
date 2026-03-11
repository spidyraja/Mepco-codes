import os
import shutil

# Set the path to the folder you want to clean
target_dir = os.path.expanduser("~/Downloads")

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Scripts": [".py", ".js", ".html", ".css"],
    "Zips": [".zip", ".tar", ".rar"]
}

def organize_folder():
    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        if os.path.isfile(filepath):
            for category, exts in extensions.items():
                if any(filename.lower().endswith(e) for e in exts):
                    dest_dir = os.path.join(target_dir, category)
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.move(filepath, os.path.join(dest_dir, filename))
                    print(f"Moved: {filename} -> {category}")

if __name__ == "__main__":
    organize_folder()
