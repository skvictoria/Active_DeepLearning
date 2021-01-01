import PIL
from PIL import Image, ExifTags
import os
import cv2


for filename in os.listdir('./test'):

    try:
        image = Image.open((os.path.join('./test', filename)))

        new_filename = os.path.join('./test', filename)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] =='Orientation':
                break

        exif = image._getexif()

        image = cv2.imread((os.path.join('./test', filename)), cv2.IMREAD_COLOR)

        if exif[orientation]==3:
            img_rotate = cv2.rotate(image, cv2.ROTATE_180)
            cv2.imwrite(new_filename, img_rotate)
        elif exif[orientation] == 6:
            img_rotate = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(new_filename, img_rotate)
        elif exif[orientation] == 8:
            img_rotate = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(new_filename, img_rotate)

    except(PIL.UnidentifiedImageError, TypeError, AttributeError, KeyError, IndexError):
        pass
