import string
import secrets
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--digit", type=int,
                    help="number of digits", default=12)
args = parser.parse_args()


def pass_gene(digit):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for x in range(digit))


if __name__ == "__main__":
    print(pass_gene(args.digit))
