import qrcode
import colorama
from colorama import Style, Fore
import os

colorama.init()

link = input("Enter link: ")
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=4)
qr.make(fit=True)
qr.add_data(link)


qr.add_data(link)

image= qr.make_image(fill_color="black", back_color="white")
import os

output_folder = os.path.join(os.getcwd(), "output-qr-4-u")
os.makedirs(output_folder, exist_ok=True)
image.save(os.path.join(output_folder, "qr_code.png"))

print(Fore.LIGHTYELLOW_EX + f"Successfully generated QR code for {link}" + Style.RESET_ALL)