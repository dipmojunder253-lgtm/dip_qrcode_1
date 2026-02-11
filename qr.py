import qrcode

qr = qrcode.QRCode(
    version=1,                # Controls the size (1 is 21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # About 7% correction
    box_size=10,              # Pixels per "box"
    border=4,                 # Thickness of the white border
)

qr.add_data("Your custom data here")
qr.make(fit=True)

# Create the image with custom colors
img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qr.png")