import os
import logging as log

log.basicConfig(level=log.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)

    try:
        with open(path_to_file, 'r') as file:
            preview = file.readline()
        log.debug(preview)
    except FileNotFoundError as e:
        log.critical("Le fichier csv est absent. {e}".format(e=e))

def main():
    launch_analysis('current_mps.csv')


if __name__ == "__main__":
    main()