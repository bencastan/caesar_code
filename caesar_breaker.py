import click
import enchant

from tqdm import tqdm

from ceasar_encryption import encrypt

@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    required=True
)
@click.option(
    '--output_file',
    type=click.File('w'),
    required=True
)
def caesar_breaker(input_file, output_file):
    cyphertext = input_file.read()
    english_dictionnary = enchant.Dict("en_US")
    best_number_of_english_words = 0
    for key in tqdm(range(26)):
        plaintext = encrypt(cyphertext, -key)
        number_of_english_words = 0
        for word in plaintext.split(' '):
            if word and english_dictionnary.check(word):
                number_of_english_words += 1
        if number_of_english_words > best_number_of_english_words:
            best_number_of_english_words = number_of_english_words
            best_plaintext = plaintext
            best_key = key
    click.echo(f'The most likely encryption key is {best_key}. It gives the following plaintext:\n\n{best_plaintext[:1000]}...')
    output_file.write(best_plaintext)

if __name__ == '__main__':
    caesar_breaker()
