import click

from ceasar_encryption import encrypt

@click.command()
@click.argument('text', nargs=-1)
@click.option('--decrypt/--encrypt', '-d/-e')
@click.option('--key', '-k', default=1)
def ceaser(text, decrypt, key):
    text_string = ''.join(text)
    if decrypt:
        key = -key
    cyphertext = encrypt(text_string, key)
    click.echo(cyphertext)

if __name__ == '__main__':
    ceaser()
