from PIL import Image
import os


def new_image_from_original_size(width, height):
    return Image.new('RGB', (width, height), (255, 255, 255))


def generate_edged_image(filename):
    oImg = Image.open(filename)
    oWidth, oHeight = oImg.size
    ratio = oWidth/oHeight

    yOffset = 0
    xOffset = 0

    if ratio > 1.1:
        # image horizontale
        # format 4:3
        width = oWidth
        height = int(width * 3 / 4)
        yOffset = int(height / 2 - oHeight / 2)

    elif ratio < 0.9:
        # image verticale
        # format 4:5
        height = oHeight
        width = int(height * 4 / 5)
        xOffset = int(width / 2 - oWidth / 2)

    else:
        # image 1x1
        width = oWidth
        height = oHeight

    canvas = new_image_from_original_size(width, height)
    canvas.paste(oImg, (xOffset, yOffset))

    if not os.path.exists(export_directory):
        os.mkdir(export_directory)

    export_path = export_directory + "/" + filename[0:-4] + "_edged.jpg"
    publish_path = "./2.Published/" + filename[0:-4] + "_edged.jpg"

    if not os.path.exists(publish_path):
        if not os.path.exists(export_path):
            canvas.save(export_path, "JPEG")
            print("> Creates {}".format(export_path))
        else:
            print("{} already exists".format(export_path))
    else:
        print("{} already published".format(publish_path))

export_directory = "Edged"

imageFiles = [file for file in os.listdir(".") if file.endswith(".jpg")]
for file in imageFiles:
    generate_edged_image(file)
