import os
import shutil

# Define the folder path to organize
folder_path = "C:/Users/YourUsername/Downloads"  # Change this to your target folder

# Define file categories and their corresponding extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}

# Create subfolders if they don’t exist
for category in file_categories.keys():
    category_path = os.path.join(folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Move files to corresponding folders
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue
    
    # Get file extension
    _, file_extension = os.path.splitext(file)
    
    # Move file to the appropriate folder
    for category, extensions in file_categories.items():
        if file_extension.lower() in extensions:
            shutil.move(file_path, os.path.join(folder_path, category, file))
            print(f"Moved {file} to {category} folder.")
            break

print("File organization complete!")

