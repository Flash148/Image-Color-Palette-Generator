from PIL import Image, ImageDraw
import numpy as np

def create_test_image():
    """Create a simple test image with known colors"""
    # Create a 200x200 image
    img = Image.new('RGB', (200, 200))
    draw = ImageDraw.Draw(img)
    
    # Draw colored rectangles with known colors
    draw.rectangle([0, 0, 100, 100], fill=(255, 0, 0))      # Red
    draw.rectangle([100, 0, 200, 100], fill=(0, 255, 0))    # Green
    draw.rectangle([0, 100, 100, 200], fill=(0, 0, 255))    # Blue
    draw.rectangle([100, 100, 200, 200], fill=(255, 255, 0)) # Yellow
    
    # Save the test image
    img.save('test_image.jpg')
    print("Test image created: test_image.jpg")
    return 'test_image.jpg'

if __name__ == "__main__":
    create_test_image()