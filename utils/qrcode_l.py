import qrcode
# qr = qrcode.QRCode(
#     border=0,
# )
# qr.add_data('xinxingzhao')
# qr.make(fit=True)

# img = qr.make_image()
# img.save('xinxingzhao.png')

img = qrcode.make("hehe", border=1)
img.save('xinxingzhao.png')
