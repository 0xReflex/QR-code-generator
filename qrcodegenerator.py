import qrcode

print('what text you want to save')
img = qrcode.make(input(':'))
img.save('qr.jpeg')