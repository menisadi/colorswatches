import unittest
from tempfile import NamedTemporaryFile
from PIL import Image
from colorswatches.swatch_generator import create_color_swatches, parse_hex_codes


class TestSwatchGenerator(unittest.TestCase):
    def test_swatch_creation(self):
        """Test that the image is created with the correct dimensions."""
        hex_codes = ["#FF5733", "#33FF57", "#3357FF"]
        create_color_swatches(
            hex_codes, swatch_size=50, scale=2, output_path="test_output.png"
        )
        img = Image.open("test_output.png")
        self.assertEqual(img.size, (340, 160))  # Expected dimensions based on the input

    def test_swatch_creation_from_file(self):
        """Test that swatches are correctly generated from a file input."""
        # Create a temporary file with hex codes
        with NamedTemporaryFile("w", delete=False) as tmp:
            tmp.write("#FF5733\n#33FF57\n#3357FF\n")
            tmp_path = tmp.name

        # Read hex codes from the file
        hex_codes = parse_hex_codes(tmp_path)
        self.assertEqual(
            len(hex_codes), 3
        )  # Check if the correct number of hex codes was read

        # Generate color swatches and check the output image
        output_path = "test_output_file.png"
        create_color_swatches(
            hex_codes, swatch_size=50, scale=2, output_path=output_path
        )
        img = Image.open(output_path)
        self.assertEqual(img.size, (340, 160))  # Expected dimensions based on the input

        # Clean up generated image file (optional)
        import os

        os.remove(output_path)


if __name__ == "__main__":
    unittest.main()
