import qrcode
from PIL import Image, ImageDraw, ImageFont

def create_qr_with_icon(url, icon_path, output_file="insta_qr.png", icon_size=None):
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)

        # Create QR code image
        qr_img = qr.make_image(fill_color=(135, 206, 250), back_color="transparent")

        # Load Facebook icon image
        try:
            icon_img = Image.open(icon_path)
        except FileNotFoundError:
            raise ValueError(f"Icon image not found: {icon_path}")

        # Determine icon size
        if not icon_size:
            qr_width, qr_height = qr_img.size
            icon_width, icon_height = icon_img.size
            max_icon_size = min(qr_width // 6, qr_height // 6)
            aspect_ratio = icon_width / icon_height
            if aspect_ratio > 1:
                icon_width = max_icon_size
                icon_height = int(max_icon_size / aspect_ratio)
            else:
                icon_height = max_icon_size
                icon_width = int(max_icon_size * aspect_ratio)
        else:
            icon_width, icon_height = icon_size

        # Resize icon image if necessary
        if icon_img.size != (icon_width, icon_height):
            icon_img = icon_img.resize((icon_width, icon_height), Image.ANTIALIAS)

        # Paste icon onto QR code image
        qr_width, qr_height = qr_img.size
        icon_left = (qr_width - icon_width) // 2
        icon_top = (qr_height - icon_height) // 2
        qr_img.paste(icon_img, (icon_left, icon_top), icon_img.convert("RGBA"))

        # Save combined image
        qr_img.save(output_file)

    except qrcode.exceptions.InvalidData:
        raise ValueError("Invalid URL provided.")

# Example usage (replace with your Facebook URL and icon path)
facebook_url = "https://www.facebook.com/riazulgalibniloy"
icon_path = "/content/facebookIcon.png"  # Replace with actual path

create_qr_with_icon(facebook_url, icon_path)
