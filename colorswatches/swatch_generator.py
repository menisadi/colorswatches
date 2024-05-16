import argparse
import logging
from PIL import Image, ImageDraw, ImageFont
from math import sqrt, ceil


def create_color_swatches(
    hex_codes,
    swatch_size=80,
    scale=1,
    output_path="color_swatches_with_codes.png",
    show_image=True,
):
    """
    Generates an image of color swatches with corresponding hex codes.

    Parameters:
        hex_codes (list of str): A list of color hex codes.
        swatch_size (int): Width and height of each color swatch in pixels.
        scale (int): Factor by which to scale the swatch size and padding.

    Saves:
        An image file containing the color swatches.
    """
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
    try:
        font = ImageFont.truetype("RobotoMono.ttf", font_size)
    except IOError:
        logging.warning("RobotoMono.ttf not found, using default font.")
        font = ImageFont.load_default()

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

    try:
        image.save(output_path)
        if show_image:
            image.show()
    except Exception as e:
        logging.error(f"Failed to save or display image: {e}")


def parse_hex_codes(file_path=None):
    """
    Parses a file containing hex codes into a list.
    Hex codes in the file can be separated by spaces and/or new lines.

    Parameters:
        file_path (str): The path to the file containing the hex codes.

    Returns:
        list of str: A list of hex codes.
    """
    hex_codes = []
    with open(file_path, "r") as file:
        content = file.read()
        # Split the content by any whitespace and filter out empty strings
        hex_codes = [code for code in content.split() if code.strip()]
    return hex_codes


def main():
    parser = argparse.ArgumentParser(
        description="Generate an image of color swatches from hex codes."
    )
    parser.add_argument("hex_codes", nargs="*", help="List of hex color codes.")
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Path to a file containing hex codes, one per line.",
    )
    parser.add_argument(
        "-s", "--size", type=int, default=80, help="Size of each color swatch."
    )
    parser.add_argument(
        "-sc",
        "--scale",
        type=int,
        default=1,
        help="Scale factor for the swatch size and padding.",
    )
    parser.add_argument(
        "-d",
        "--display",
        action="store_true",
        help="Display the image after generating it.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="color_swatches_with_codes.png",
        help="Output image file path.",
    )
    args = parser.parse_args()

    if args.file:
        hex_codes = parse_hex_codes(args.file)
    else:
        hex_codes = args.hex_codes

    if not hex_codes:
        logging.error(
            "No hex codes provided. Please specify hex codes directly or through a file."
        )
        parser.print_help()
        return

    create_color_swatches(
        hex_codes,
        swatch_size=args.size,
        scale=args.scale,
        output_path=args.output,
        show_image=args.display,
    )


if __name__ == "__main__":
    main()
