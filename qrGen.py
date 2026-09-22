import qrcode

qr = qrcode.QRCode()

while True:
    print("1. Generate a QR Code "
        "2. Close ")
    
    choice = input("")

    if choice == "1":
        data = input("Link/Image URL: ").strip()
        name = input("Filename: ").strip()
        if data and name:
            qr.add_data(data)
            img = qr.make_image()
            img.save(name + ".png")
            print("QR Code generated.")
        else:
            print("Both fields are required")
        continue
    elif choice == "2":
        break
    else:
        print("Invalid Choice")
    break