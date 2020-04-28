#!/usr/bin/env python3 
import qrcode#importing qrcode in this program

print('what text you want to save')# printing the stff..
img = qrcode.make(input(':'))# taking the input and just giving it to the program
img.save('qr.jpeg')# now saving the file as QR.jpeg """ you can change the extention to png (I never tested other extention exept png) """ 
