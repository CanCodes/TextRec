try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def textRecog(imageFile):
        text = pytesseract.image_to_string(Image.open(imageFile))
        return text