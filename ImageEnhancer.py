import os
from PIL import Image, ImageEnhance 

def ImgEnhancer(input_image_path):
    try:
        with Image.open(input_image_path) as original_img:
            enhanced_img = ImageEnhance.Color(original_img).enhance(1.5)
            enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(1.5)
            enhanced_img = ImageEnhance.Sharpness(enhanced_img).enhance(1.5)
            enhanced_img.show()
            original_img.show()
            enhanced_img.save(f"{os.getenv('USERPROFILE')}\\Downloads\\EnhancedImg.jpg", "JPEG", optimize=True)
    except:
        pass
           