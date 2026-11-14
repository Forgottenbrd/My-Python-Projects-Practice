import qrcode


def get_user_input():
    '''Getting the user input.
    '''
    return input("Enter the text or URL for the QR code: ")

def get_file_name():
    return input("Enter the filename: ")

def make_qrcode(input, filename):
    qr = qrcode.make(input)
    qr.save(filename)
  
def main():
    input = get_user_input()
    filename = get_file_name()
    make_qrcode(input, filename)

if __name__ == "__main__":
    main()

