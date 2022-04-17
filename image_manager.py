import os
import random
def folder_search(folder_name):
    path = "images/{}".format(folder_name)

    if not os.path.isdir(path) :
        path = "Error, no such directory!"

    return path


def get_image(path):
    img_path = ""

    if not path.startswith("Error"):
        image_list = list(os.listdir(path))
        choice = random.choice(image_list)
        img_path = os.path.join(path, choice)
    else: 
        img_path = "images/default.png"
    
    return img_path
    
def retrieve_image(character):
    path = folder_search(character)
    image = get_image(path)

    return image

    
