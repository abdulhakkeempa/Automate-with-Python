from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
#give the path your template certificate (either png or jpeg)
template_certificate_path = 'template file path'
#give the path your csv file.
df = pd.read_csv('csv - file path')
#change the font and font size if needed.
font = ImageFont.truetype('arial.ttf',40)
for index,j in df.iterrows():
    img = Image.open(template_certificate_path)
    draw = ImageDraw.Draw(img)
    #(xy) = x and y cordinate in the image where the text starts printing.
    #(fill) = text color.
    draw.text(xy=(155,450),text='{}'.format(j['name']),fill=(17,110,158),font=font)
    #all the files will be saved in the folder certificates created in the path you gave.
    #file name will be that of the name printed.
    #change the .pdf to any other file format preferably.
    img.save('path where you want to save the certificates \certificates/{}.pdf'.format(j['name']))