import qrcode

def qrcodeimg(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="magenta", back_color="white")
    img.show()
