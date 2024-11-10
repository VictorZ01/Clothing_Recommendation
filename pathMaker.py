import os 
import json

parent_folder = 'images'

image_files = []
for root, dirs, files in os.walk(parent_folder):
    for file in files:
        if file.endswith(('.jpg', '.jpeg')):
            image_files.append(os.path.join(root, file))

with open('B:\WebScrapper\image_paths.json', 'w') as f:
    json.dump(image_files, f)           