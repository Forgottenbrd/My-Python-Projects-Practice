from pathlib import Path


import qrcode


BASE_DIR = Path(__file__).resolve().parent


def get_user_input():
    return input("Enter the text or URL for the QR code: ").strip()


def get_file_name():
    return input("Enter the filename: ")


def dir_making(base_dir):
    OUTPUT_DIR = base_dir / "qrcodes"
    output_dir_path = OUTPUT_DIR.mkdir(exist_ok=True)
    return OUTPUT_DIR


def make_qrcode(input):
    return qrcode.make(input)


def save_qrcode(qr_code, output_dir_path, file_name):
    full_path = output_dir_path / f"{file_name}.png"
    qr_code.save(full_path)

def show_qrcode_status(file_name):
    print(f"QR code saved as {file_name}.png")


def main():
    input = get_user_input()
    file_name = get_file_name()
    dir_path = dir_making(BASE_DIR)
    qr_code = make_qrcode(input)
    save_qrcode(qr_code, dir_path, file_name)
    show_qrcode_status(file_name)


if __name__ == "__main__":
    main()
