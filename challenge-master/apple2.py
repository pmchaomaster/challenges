import os
import re
import argparse

# set the directory you want to start from

rootdir ='/home/peter1/pcdir'




def main():
    """ Main will run user specific request of a root directory.

    Args:
        root_dir: test root directory a user entered.
        keyword: to match the file pattern

    """

    parser = argparse.ArgumentParser(description='Run from root directory')
    parser.add_argument("root_directory",
                        type=str,
                        help="The test root directory to run from")

    args = parser.parse_args()
    root_dir = parser.root_directory
    #keyword = re.findall9r'[a-zA-Z]+_TestResult.*
    matches = []
    for root, dirnames, filenames in os.walk('root_dir'):
        for filename in fnmatch.filter(filenames, keyword):
            matches.append(os.path.join(root, filename))

    for dirName, subdirList, fileList in os.walk(rootdir):
        print('Found directory %s' % dirName)
        print('========================')
        for fname in fileList:
            print('\t%s' % fname)

    print ("-") * 70
    print ("\nAll Done")



if __name__ == '__main__':
    main()
