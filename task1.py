import argparse
from collections import Counter


def count_letters(s, minimum=1):
    s = s.replace(" ", "")
    return{k:v for k, v in Counter(s).items() if v >=minimum}



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("letters", 
                        type=str,
                        metavar="Some Text",
                        help="enter some text to be evaluated")

    parser.add_argument("--minimum",
                        type=int,
                        dest="mini",
                        help="minimum number of arguments")


    args = parser.parse_args()
    print(args.mini)
    result = count_letters(args.letters, args.mini)

    print(result)