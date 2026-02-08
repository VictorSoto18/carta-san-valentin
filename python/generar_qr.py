import qrcode

# Pega aquí tu enlace público de GitHub Pages
url = "https://VictorSoto18.github.io/carta-san-valentin/"

# Crear QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Generar imagen
img = qr.make_image(fill_color="red", back_color="white")

# Guardar QR
img.save("carta_san_valentin_qr.png")

print("💖 QR creado: carta_san_valentin_qr.png")
