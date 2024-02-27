from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./Input Image"
path_out = "./Output Image"

# for filename in os.listdir(path):
#     img = Image.open(f"{path}/{filename}")
#     if img.mode=='RGBA':
#         img = img.convert('RGB')
#         img.save(f'{path}/{filename}_converted.jpg')
#     else:
#         pass

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    if img.mode=='RGBA':
        img = img.convert('RGB')
        img.save(f'{path}/{filename}_converted.jpg')
    else:
        pass

    edit = img.filter(ImageFilter.SHARPEN)

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    
    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{path_out}/{clean_name}_edited.jpg')

    print("Edited Successfully")
