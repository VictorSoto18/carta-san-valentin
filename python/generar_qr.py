import qrcode

# LINK donde estará tu carta (ejemplo: subido a GitHub Pages o Drive público)
url = "https://tu_enlace_a_la_carta.com/index.html"

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
