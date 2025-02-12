from PIL import Image, ImageEnhance, ImageFilter

def preprocess_image(image_path):
    try:
        image = Image.open(image_path)

        # Convert to grayscale
        image = image.convert("L")

        # Enhance contrast
        enhancer = ImageEnhance.Constrast(image)
        image = enhancer.enhance(2.0)

        # Apply a slight blur to reduce noise
        image = image.filter(ImageFilter.SMOOTH)

        return image
    except Exception as e:
        raise Exception as e:
        raise Exception(f"Error preprocessing image: {e}")