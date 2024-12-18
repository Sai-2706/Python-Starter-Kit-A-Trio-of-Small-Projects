import qrcode

data = "https://www.github.com/yourusername"  # Replace with your link/text
output_file = "qrcode.png"

# Generate QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Save QR code
img = qr.make_image(fill="black", back_color="white")
img.save(output_file)

print(f"QR Code saved as {output_file}")
