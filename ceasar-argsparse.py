import argparse

from ceaser_encryption import encrypt

def ceasar():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action='store_true')
    group.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('text', nargs='*')
    parser.add_argument('-k', '--key', type=int, default=1)
    args = parser.parse_args()

    text_string = ''.join(args.text)
    key = args.key
    if args.decrypt:
        key =-key
    cyphertext = encrypt(text_string, key)
    print(cyphertext)

if __name__ == '__main__':
    ceasar()
