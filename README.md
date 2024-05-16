# ColorSwatches
*Colors Watches Generator*

ColorSwatches is a Python tool that allows you to generate an image of color swatches from hex codes provided via a command line or a file.

## Installation
*Not yet available*

## Usage
To use ColorSwatches, you can provide hex codes directly through the command line or via a file:

```bash
colorswatches #HEX1 #HEX2 #HEX3
colorswatches -f path/to/file.txt
```
it can also be used by importing as a module:

```python
from colorswatches.swatch_generator import create_color_swatches

hex_codes = [
    "#1F1F28", "#DCD7BA", "#72A7BC", "#C8C093", "#2D4F67",
    "#16161D", "#C34043", "#76946A", "#C0A36E", "#7E9CD8",
    "#957FB8", "#6A9589", "#727169", "#E82424", "#98BB6C",
    "#E6C384", "#7FB4CA", "#938AA9", "#7AA89F",
]
create_color_swatches(hex_codes, 80, 2)
```

This will create and save an image with the specified color swatches.

## Features
Generate color swatches with corresponding hex codes.
Customize the size and scale of swatches.
Output the result as a PNG image.

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

