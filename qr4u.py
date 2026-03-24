import qrcode
import colorama
from colorama import Style, Fore

colorama.init()

link = input("Enter link: ")
qr= qrcode.QRCode()

qr.add_data(link)

image= qr.make_image()
image.save("output/qr_code.png")
print(Fore.LIGHTYELLOW_EX + f"Successfully generated QR code for {link}" + Style.RESET_ALL)