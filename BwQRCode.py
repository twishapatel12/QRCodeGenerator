import qrcode as qr
img = qr.make("https://www.google.com/maps/place/Tirth+Construction/@22.3185057,73.2124321,18z/data=!4m6!3m5!1s0x395fcf46a30d738d:0x6c2df2ff5359df71!8m2!3d22.3184608!4d73.2126599!16s%2Fg%2F11kjpry9mp")
img.save("tirth_construction.png")
