import os
import shutil
from tqdm import tqdm

downloads_folder = os.path.expanduser("~/Downloads")
organized_folder = os.path.expanduser("~/Organized_Downloads")

file_categories = {
    "Images": [".jpg", ".png", ".gif", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Others": []
}

os.makedirs(organized_folder, exist_ok=True)

# Prepare files and counters
all_files = [
    f for f in os.listdir(downloads_folder)
    if os.path.isfile(os.path.join(downloads_folder, f))
]
category_counts = {category: 0 for category in file_categories}
category_counts["Others"] = 0

# Process files with progress bar
for filename in tqdm(all_files, desc="Organizing files"):
    file_path = os.path.join(downloads_folder, filename)
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Find category
    found = False
    for category, extensions in file_categories.items():
        if ext in extensions:
            target_folder = os.path.join(organized_folder, category)
            os.makedirs(target_folder, exist_ok=True)
            shutil.copy2(file_path, target_folder)
            category_counts[category] += 1
            found = True
            break
    
    if not found:
        target_folder = os.path.join(organized_folder, "Others")
        os.makedirs(target_folder, exist_ok=True)
        shutil.copy2(file_path, target_folder)
        category_counts["Others"] += 1

# Summary
print("\n=== Organization Summary ===")
for category, count in category_counts.items():
    print(f"{category}: {count} files")