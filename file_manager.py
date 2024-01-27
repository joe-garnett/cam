import os
from PIL import Image

# dir paths
base_path = os.path.join(".", "data")
unsorted_path = os.path.join(".", "unsorted_images")

def create_master_files():
    # Loop from 0 to 180
    for i in range(181):
        # Folder name as the current number
        folder_name = str(i)
        # Full path for the new folder
        new_path = os.path.join(base_path, folder_name)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            print(f"Folder '{folder_name}' created.")
        else:
            print(f"Folder '{folder_name}' already exists.")

    if not os.path.exists(unsorted_path):
        os.makedirs(unsorted_path)
        print(f"Folder unsorted_images created.")

def add_image(score_img, angle):
    # Pass filename of file in unsorted_images

    # Splits filename into score and suffix e.g. "64" "jpg"
    score, suffix = score_img.split(".")
    dir = os.path.join(base_path, str(score))
    dir_contents = os.listdir(dir)

    # Creates lowest possible unique number id for photo, just to keep things nice and organised
    ids = set()
    for f in dir_contents:
        index, _= f.split(".")
        ids.add(int(index))
    if ids:
        maximum = max(ids)
    else: 
        maximum = -1
    minimum = 0

    possible_ids = set()
    for i in range(minimum, maximum + 2):
        possible_ids.add(i)

    available_ids = possible_ids - ids
    id = min(available_ids)
    save_image(score_img, (str(id) + '.' + suffix), dir, angle)

    


def save_image(score_img, filename, target_dir, angle):
    old_file_path = os.path.join(unsorted_path, score_img)
    image = Image.open(old_file_path)
    rotated_image = image.rotate(angle)
    # Save the image to the correct directory with a new filename
    rotated_image.save(os.path.join(target_dir, filename))

    # Remove old file
    os.remove(old_file_path)

    