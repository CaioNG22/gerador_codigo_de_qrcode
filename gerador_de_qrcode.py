import pyqrcode

import png

from pyqrcode import QRCode

site = input("Digite o site: ")

nome = input("Digite o nome do arquivo")

url = pyqrcode.create(site)

url.svg(f"{nome}.svg", scale=8)

url.png(f"{nome}.png", scale=6)
