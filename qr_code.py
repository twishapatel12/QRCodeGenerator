import qrcode as qr
img = qr.make("http://localhost/wordpress/")
img.save("travel_shuffle.png")