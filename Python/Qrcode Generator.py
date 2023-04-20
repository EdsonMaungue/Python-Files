# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 08:45:10 2023

@author: Edson
"""

# install all the libraries needed
# create a function that collects a text and converts it to a qrcode
# save the qrcode as an image
#run the function 


import qrcode



def generate_qrcode(text):
        
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="Black", back_color="white")
        img.save("qrimg1.png")
        

url = input("Enter your url: ")        

generate_qrcode(url)