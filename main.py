from math import sqrt, ceil
from PIL import Image, ImageDraw, ImageFont


def create_color_swatches(hex_codes, swatch_size=80):
    # Calculate dimensions based on number of colors
    colors_per_row = int(
        ceil(sqrt(len(hex_codes)))
    )  # Adjust this to fit more or fewer swatches per row
    num_rows = (
        len(hex_codes) + colors_per_row - 1
    ) // colors_per_row  # Ceiling division
    padding = 10
    width = colors_per_row * (swatch_size + padding) + padding
    height = num_rows * (swatch_size + padding) + padding

    # Create an image with a white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        font = ImageFont.load_default()

    # Draw each color swatch and write the hex code
    x, y = padding, padding
    for hex_code in hex_codes:
        draw.rectangle([x, y, x + swatch_size, y + swatch_size], fill=hex_code)
        text_color = (
            "white" if int(hex_code[1:], 16) < 0xAAAAAA else "black"
        )  # Ensuring text visibility
        draw.text(
            (x + 5, y + swatch_size - 20), hex_code, font=font, fill=text_color
        )
        x += swatch_size + padding
        if x > width - swatch_size - padding:
            x = padding
            y += swatch_size + padding

    # Save and show the image
    image.save("color_swatches_with_codes.png")
    image.show()


# Example usage
hex_codes = [
    "#1F1F28",
    "#DCD7BA",
    "#72A7BC",
    "#C8C093",
    "#2D4F67",
    "#16161D",
    "#C34043",
    "#76946A",
    "#C0A36E",
    "#7E9CD8",
    "#957FB8",
    "#6A9589",
    "#727169",
    "#E82424",
    "#98BB6C",
    "#E6C384",
    "#7FB4CA",
    "#938AA9",
    "#7AA89F",
]
create_color_swatches(hex_codes, 80)  # You can change the swatch size
