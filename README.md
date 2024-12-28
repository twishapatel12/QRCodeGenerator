# QR Code Generation Project

## Overview
This project demonstrates two methods of generating QR codes using Python. The first method uses the `qrcode` library to create a simple QR code, while the second method uses the same library along with `PIL` to generate a customized QR code with specified colors.

## Features
- **Simple QR Code Generation**: Creates a basic QR code and saves it as an image file.
- **Customized QR Code Generation**: Generates a QR code with specified fill and background colors, and saves it as an image file.

## Skills Used
- Python
- QR Code Generation
- Image Processing
- Python Imaging Library (PIL)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-generation-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd qr-code-generation-project
   ```
3. Install the required packages:
   ```bash
   pip install qrcode[pil]
   ```

## Usage
### Simple QR Code Generation
1. Open the `simple_qr.py` file and replace the empty string in `qr.make("")` with your desired data.
2. Run the script to generate the QR code:
   ```bash
   python simple_qr.py
   ```
3. The QR code image will be saved as `twishapatel.png`.

### Customized QR Code Generation
1. Open the `custom_qr.py` file and replace the URL in `qr.add_data("http://localhost/wordpress/")` with your desired data.
2. Modify the `fill_color` and `back_color` parameters to customize the QR code colors.
3. Run the script to generate the customized QR code:
   ```bash
   python custom_qr.py
   ```
4. The customized QR code image will be saved as `colorQR1.png`.

## Example
### Simple QR Code
```python
import qrcode as qr
img = qr.make("https://example.com")
img.save("example.png")
```

### Customized QR Code
```python
from turtle import fillcolor
import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("https://example.com")
qr.make(fit=True)

img = qr.make_image(fill_color="yellow", back_color="green")
img.save("custom_example.png")
```

## Acknowledgements
- Python Software Foundation
- Libraries used: `qrcode`, `PIL`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
