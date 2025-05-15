import qrcode
from PIL import Image

# Data for the QR code
LibID = input("Text for the QR code:\n")
# data = "UBNQUS9GU6CK"

# Generate the QR code
qr = qrcode.QRCode(
    version=3,  # Adjust version for more data or higher resolution
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data(LibID)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Load the logo
logo = Image.open("../../Logo/Thumbnail.png")  # Replace with the path to your logo

# Resize the logo
logo_size = min(qr_img.size) // 4  # Logo size as a fraction of QR code size
logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

# Calculate the position and create a white box
qr_width, qr_height = qr_img.size
logo_width, logo_height = logo.size
logo_position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

# Create a white rectangle (clearing space for the logo)
box_x1, box_y1 = logo_position
box_x2, box_y2 = box_x1 + logo_width, box_y1 + logo_height
white_box = Image.new("RGB", (logo_width, logo_height), "white")
qr_img.paste(white_box, (box_x1, box_y1))

# Paste the logo onto the white box
qr_img.paste(logo, logo_position, mask=logo if logo.mode == "RGBA" else None)

# Save the final image
title = input("title:")
filename = f"{title}-{LibID}"
qr_img.save(f"{filename}.png")

print(qr_img.print_ascii())
print(f"saved as '{filename}.png'")
