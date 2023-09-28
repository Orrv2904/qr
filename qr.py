import qrcode

enlace = "https://github.com/Orrv2904"

codigo_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

codigo_qr.add_data(enlace)
codigo_qr.make(fit=True)

imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

imagen_qr.save("codigo_qr.png")
print("Código QR generado y guardado como 'codigo_qr.png'")