import argparse
import csv
import os


class Validator:
    def __init__(self, path):
        _, self.file_extension = os.path.splitext(path)
        self.errors = []
        with open(path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            self.rows = [row for row in reader]
            self.fields = reader.fieldnames
            self.validheaders = [
                "item ark",
                "parent ark",
                "item status id",
                "item status",
                "object type",
                "file name",
                "item sequence",
                "duplicate",
                "delete in title",
                "thumbnail",
                "viewinghint",
                "text direction",
                "visibility",
                "iiif range",
                "type.typeofresource",
                "type.genre",
                "rights.copyrightstatus",
                "rights.statementlocal",
                "rights.servicescontact",
                "language",
                "coverage.geographic",
                "coverage.temporal",
                "subject",
                "alt id.local",
                "title",
                "name.creator",
                "alttitle.uniform",
                "relation.ispartof",
                "summary",
                "description.note",
                "date.creation",
                "date.normalized",
                "publisher.placeoforigin",
                "publisher.publishername",
                "name.subject",
                "name.photographer",
                "name.repository",
                "finding aid url",
                "opac url",
                "bucketeer state",
                "iiif access url",
                "iiif manifest url",
                "media.width",
                "media.height",
                "media.duration",
                "media.format",
                "waveform",
                "license",
            ]

    def is_csv(self):

        # Check file extension is .csv

        if self.file_extension.lower() != ".csv":
            self.errors.append(
                f"Incorrect file extension ({file_extension}), please specify a .csv"
            )

        # Check if the file is empty
        if not self.rows:
            self.errors.append("File is empty")
            return 0

        # Check that a header row exists with valid header names
        found_item = 0
        for item in self.fields:
            if item.lower() in self.validheaders:
                found_item += 1

        if found_item == 0:
            self.errors.append("No valid header row exists in file")

    def validate(self):
        self.is_csv()
        if self.errors:
            print("Your file contains these errors: ", self.errors)
        else:
            print("There are no errors in your file!")


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
