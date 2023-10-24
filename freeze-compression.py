#!/usr/bin/env python3

import argparse
import os
import zipfile


def compress_file(input_file, output_zip):
    """指定されたファイルをZIP形式で圧縮します。"""
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        zipf.write(input_file, os.path.basename(input_file))
    print(f"ファイル {input_file} を {output_zip} に圧縮しました。")


def decompress_file(zip_file, output_dir):
    """指定されたZIPファイルを指定されたディレクトリに展開します。"""
    with zipfile.ZipFile(zip_file, 'r') as zipf:
        zipf.extractall(output_dir)
    print(f"ZIPファイル {zip_file} をディレクトリ {output_dir} に展開しました。")


def main():
    parser = argparse.ArgumentParser(description='ファイルの圧縮と展開を行うツールです。')
    subparsers = parser.add_subparsers(dest='command')

    # 圧縮のサブコマンド
    compress_parser = subparsers.add_parser('compress', help='ファイルを圧縮します。')
    compress_parser.add_argument('input_file', type=str, help='圧縮するファイルのパス。')
    compress_parser.add_argument(
        'output_zip', type=str, help='出力するZIPファイルのパス。')

    # 展開のサブコマンド
    decompress_parser = subparsers.add_parser(
        'decompress', help='ZIPファイルを展開します。')
    decompress_parser.add_argument(
        'zip_file', type=str, help='展開するZIPファイルのパス。')
    decompress_parser.add_argument(
        'output_dir', type=str, help='展開先のディレクトリのパス。')

    args = parser.parse_args()

    if args.command == 'compress':
        compress_file(args.input_file, args.output_zip)
    elif args.command == 'decompress':
        decompress_file(args.zip_file, args.output_dir)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
