import qrcode

# Define el enlace que deseas codificar en el QR
enlace = "https://github.com/Orrv2904"

# Crea un objeto QRCode
codigo_qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Agrega el enlace al código QR
codigo_qr.add_data(enlace)
codigo_qr.make(fit=True)

# Crea una imagen del código QR
imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo
imagen_qr.save("codigo_qr.png")

print("Código QR generado y guardado como 'codigo_qr.png'")
