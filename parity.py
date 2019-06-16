import argparse
import logging as log


import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a csv or xml?""")
    parser.add_argument("-f", "--file", help="""Path file to analyse""")
    return parser.parse_args()


def main():
    args = parse_arguments()
    try:
        if args.file == None:
            raise Warning('Argument -f not found. Please read help with -h')
        elif args.extension == None:
            raise Warning('Argument -e not found. Please read help with -h')
        else:
            if args.extension == "csv":
                c_an.launch_analysis(args.file)
            elif args.extension == "xml":
                x_an.launch_analysis(args.file)
            else:
                raise Warning('Argument -e not in list. Please read help with -h')
    except Warning as e:
        log.warning(e)
    except FileNotFoundError as e:
        log.warning(e)

if __name__ == "__main__":
    main()