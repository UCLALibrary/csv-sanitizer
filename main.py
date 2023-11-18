import argparse
import csv

class Validator():
    def __init__(self, path):
        self.path = path

    def validate(self):
        with open(self.path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

def main():
    # read csv path from command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="Path to the csv file")
    args = parser.parse_args()

    # create instance of validator 
    validator = Validator(args.csv_path)
    validator.validate()

if __name__ == "__main__":
    main()
