import qrcode # install qrcode module 
import image  # install image module 
qr=qrcode.QRCode( version=15,box_size=10,border=5) #creating qr object
data="youtube.com" # data for qrcode
qr.add_data(data) #adding data qr code
qr.make(fit=True)
img=qr.make_image(fill="black", bacK_color="white") #adding qr to image 
img.save("test.png") #out qr code