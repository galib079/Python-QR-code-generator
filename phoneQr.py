import qrcode

# URL to open when scanning the QR code
phone = "+8801518337015"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(phone)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color=(135, 206, 250), back_color="transparent")

# Save the image to a file
img.save("phone_qr_code.png")
