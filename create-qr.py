import qrcode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, default='./qrcode.png',
                    help='Output file name.',)
parser.add_argument('-t', '--target', type=str, default='https://github.com/lincolnloop/python-qrcode',
                    help='Controls the size of the QR code. Select 1 to 40.',)
parser.add_argument('-v', '--version', type=int, default=None,
                    help='Controls the size of the QR code. Select 1 to 40.',)
parser.add_argument('-e', '--error', type=str, default='L',
                    help='Controls error correction used for QR codes. Select L M Q H.',)
parser.add_argument('-bs', '--boxsize', type=int, default=20,
                    help='Controls how many pixels each box in the QR code.',)
parser.add_argument('-bd', '--border', type=int, default=4,
                    help='Controls how many boxes thick the border should be.',)
parser.add_argument('-fc', '--fillcolor', type=str, default='black',
                    help='Change the painting color of the QR.',)
parser.add_argument('-bc', '--backcolor', type=str, default='white',
                    help='Change the background color of the QR.',)
args = parser.parse_args()


def create_qr(output, target, version, error, boxsize, border, fillcolor, backcolor):
    try:
        error_correction_levels = {
            'L': qrcode.constants.ERROR_CORRECT_L,
            'M': qrcode.constants.ERROR_CORRECT_M,
            'Q': qrcode.constants.ERROR_CORRECT_Q,
            'H': qrcode.constants.ERROR_CORRECT_H,
        }

        qr = qrcode.QRCode(
            version=version,
            error_correction=error_correction_levels[error],
            box_size=boxsize,
            border=border,
        )
        qr.add_data(target)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fillcolor, back_color=backcolor)
        img.save(output)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    create_qr(args.output, args.target, args.version, args.error, args.boxsize,
              args.border, args.fillcolor, args.backcolor)
