import random
import string
import urllib.request
import argparse


class MarkovChain:
    def __init__(self, order):
        self.order = order
        self.prefix_dict = {}

    def train(self, text):
        words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
        prefixes = [''] * self.order
        for word in words:
            self.prefix_dict.setdefault(tuple(prefixes), set()).add(word)
            prefixes.pop(0)
            prefixes.append(word)

    def generate(self, seed, length):
        prefixes = list(seed.lower().split())
        result = seed
        while len(result.split()) < length:
            suffixes = self.prefix_dict.get(tuple(prefixes))
            if suffixes is None:
                break
            word = random.choice(list(suffixes))
            result += ' ' + word
            prefixes.pop(0)
            prefixes.append(word)
        return result


def main():
    parser = argparse.ArgumentParser(description='Generate text using a Markov chain model')
    parser.add_argument('seed', type=str, help='the starting text for the generated output')
    parser.add_argument('length', type=int, help='the desired length of the generated output in words')
    parser.add_argument('--order', type=int, default=2, help='the order of the Markov chain model (default: 2)')
    args = parser.parse_args()

    url = 'http://www.gutenberg.org/files/1342/1342-0.txt'
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')

    mc = MarkovChain(order=args.order)
    mc.train(text)

    generated_text = mc.generate(args.seed, args.length)
    print(generated_text)


if __name__ == '__main__':
    main()
