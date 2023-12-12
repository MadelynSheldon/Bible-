from PIL import Image, ImageDraw
import random

def generate_art():
    width, height = 400, 200
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Example: Draw a random rectangle
    x = random.randint(0, width - 100)
    y = random.randint(0, height - 100)
    width_rect = random.randint(20, 100)
    height_rect = random.randint(20, 100)

    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw.rectangle([x, y, x + width_rect, y + height_rect], fill=color)

    # Save the generated image
    image.save("generative_art.png")

if __name__ == "__main__":
    generate_art()
