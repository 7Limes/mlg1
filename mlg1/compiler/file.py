from io import BytesIO
from PIL import Image


def img_to_simg(img: Image.Image) -> list[int]:
    simg_data = [img.width, img.height]
    for i in range(img.height):
        for j in range(img.width):
            pixel = img.getpixel((j, i))
            pixel_int = pixel[2]
            pixel_int <<= 8
            pixel_int |= pixel[1]
            pixel_int <<= 8
            pixel_int |= pixel[0]
            simg_data.append(pixel_int)
    return simg_data


def get_parsed_file_size(file_bytes: bytes, file_extension: str) -> int:
    if file_extension.lower() in {'.png', '.jpg', '.bmp'}:
        img = Image.open(BytesIO(file_bytes))
        return len(img_to_simg(img))
    return len(file_bytes)