import random
import argparse
import sys

def main():
    """This is DNAnexus coding test version1
    Main will take two arguments for reading.
    It will then print that line to stdout


    Args:
         (1) data_file_name: the file it will be read from
         (2) line_number: the nth-1 number of line to read

    :return: from data_file_name input, line_number-1 line,
             it will print out that line.
    """

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

if __name__ == '__main__':
    main()
