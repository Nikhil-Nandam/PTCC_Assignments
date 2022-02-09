# This is an empty python file
# where you have to add your code to
# rename the same file that is 
# present with different names
# to something like file1.pdf,
# file2.pdf, ...., filen.pdf!
# The ______ library need to be used
# 
# Good Luck!!!

import os

path = 'assignment 2/files1/'

pdfs = os.listdir(path)

for i in range(len(pdfs)):
    pdf_path = path + pdfs[i]
    renamed_pdf = path + f'file{i}.pdf'
    os.rename(pdf_path, path + f'file{i}.pdf')