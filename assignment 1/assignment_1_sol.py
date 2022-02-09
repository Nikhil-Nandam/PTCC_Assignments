# This is an empty python file
# where you have to add your code to
# read the content of the 3 qrcodes
# provided and print them using python
# and _______, _____ libraries!
# 
# Good Luck!!!

import os
import cv2

path = 'assignment 1/qrcodes/'
qrcodes = os.listdir(path)

d = cv2.QRCodeDetector()

for qrcode in qrcodes:
    file_path = path + qrcode
    val, _, _ = d.detectAndDecode(cv2.imread(file_path))
    print(f"Decoded text from {qrcode} ", val)