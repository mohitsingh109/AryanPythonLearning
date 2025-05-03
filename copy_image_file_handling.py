# "rb" = (Reading a binary file) (.csv, .xlsx, .jpg, .png)

def read_image(path):
    with open(path, "rb") as original_file:
        return original_file.read()

def copy_image(path, data):
    with open(path, "wb") as copy_file:
        copy_file.write(data)

original_image_data = read_image('picture.jpg')
copy_image('copy_picture.jpg', original_image_data)