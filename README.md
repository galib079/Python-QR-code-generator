Python QR Code Generator with Custom Icon
=========================================

This Python script generates QR codes with a custom icon embedded in the center, offering a personalized touch to your QR code generation needs. It's a simple yet effective tool for encoding URLs into QR codes and enhancing them with custom icons.

Features
--------

*   **URL Customization**: Encode any URL into a QR code with ease.
    
*   **Custom Icon Integration**: Add a personalized touch by embedding a custom icon into the QR code.
    
*   **Automatic Scaling**: The script automatically scales the icon to fit perfectly within the QR code.
    
*   **Size Customization**: Optionally specify the desired size of the icon for further customization.
    
*   **Error Handling**: Gracefully handles errors such as invalid URLs and missing icon images.
    

Usage
-----

1.  **Installation**: Clone the repository or download the script directly.
    
2.  bashCopy codepip install qrcode pillow
    
3.  bashCopy codepython qr\_code\_generator.py
    
4.  **Customization**: Replace the placeholder URL and icon path with your desired values in the script. Optionally, specify the output file name and the desired size of the icon.
    
5.  **Output**: The generated QR code with the custom icon will be saved as specified in the script.
    

Example
-------

```python
import qr_code_generator

# Replace with your URL and icon path
url = "https://www.example.com"
icon_path = "path/to/your/custom_icon.png"

qr_code_generator.create_qr_with_icon(url, icon_path, output_file="custom_qr_code.png", icon_size=(100, 100))
'''

Requirements
------------

*   Python 3.x
    
*   **qrcode** library
    
*   **PIL** (Python Imaging Library)
    

Contributions
-------------

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

License
-------

This project is licensed under the MIT License.
