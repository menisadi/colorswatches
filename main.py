from PIL import Image, ImageDraw, ImageFont
from math import sqrt, ceil


def create_color_swatches(hex_codes, swatch_size=80, scale=1):
    # Scale up dimensions for higher resolution
    swatch_size_scaled = swatch_size * scale
    padding = 10 * scale

    # Calculate dimensions based on number of colors
    colors_per_row = int(ceil(sqrt(len(hex_codes))))
    num_rows = (
        len(hex_codes) + colors_per_row - 1
    ) // colors_per_row  # Ceiling division
    width = colors_per_row * (swatch_size_scaled + padding) + padding
    height = num_rows * (swatch_size_scaled + padding) + padding

    # Create an image with a white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    font_size = int(10 * scale)
    font = ImageFont.truetype("RobotoMono.ttf", font_size)

    # Finally, draw each color swatch and write the hex code
    x, y = padding, padding
    for hex_code in hex_codes:
        draw.rectangle(
            [x, y, x + swatch_size_scaled, y + swatch_size_scaled],
            fill=hex_code,
        )
        text_color = (
            "white" if int(hex_code[1:], 16) < 0xAAAAAA else "black"
        )  # Pick white or black color to ensure text visibility
        # Adjust text position based on scale
        draw.text(
            (x + scale * 5, y + swatch_size_scaled - scale * 20),
            hex_code,
            font=font,
            fill=text_color,
        )
        x += swatch_size_scaled + padding
        if x > width - swatch_size_scaled - padding:
            x = padding
            y += swatch_size_scaled + padding

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
create_color_swatches(hex_codes, 80, 2)
