import random
import argparse
import sys


def read_random(line,data_file):
    data_read_array = {}

    try:
        lineNumber = ln
        with open(fn) as dfn:
            for n,line  in enumerate(dfn):
                if n+1 == ln:
                    data_read_array[ln]=line
                    sys.stdout.write(data_read_array[ln])
    except Exception as e:
        print ("Line number not valid:"),e


def take_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file_name",
                        type=str,
                        default='data_file1.txt',
                        help='Example: If you want to read from\
                                    file data_file1.txt: "DNAnexuse1.py data_file1.txt')
    parser.add_argument("line_number",
                        type=int,
                        default=0,
                        help="The desired line number")
    args = parser.parse_args()
    ln = args.line_number
    fn = args.data_file_name
    return (ln,fn)

def main():
    # The main method
    line,data_file=take_input()
    read_random(line,data_file)





if __name__ == '__main__':
    main()
