import barcode
from barcode.writer import ImageWriter
import argparse

# コマンドライン引数の解析
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, default='./barcode',
                    help='Output file name.')
parser.add_argument('-t', '--target', type=str, default='123456789012',
                    help='The data to encode in the barcode.')
parser.add_argument('-b', '--barcode_type', type=str, default='ean13',
                    help='The type of barcode to generate. Example: ean13, code128.')
args = parser.parse_args()


def create_barcode(output, target, barcode_type):
    try:
        barcode_class = barcode.get_barcode_class(barcode_type)
        code = barcode_class(target, writer=ImageWriter())
        code.save(f'{output}')
        print(f'Barcode saved to {output}.png')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    create_barcode(args.output, args.target, args.barcode_type)
