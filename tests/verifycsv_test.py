import unittest
from main import Validator
from main import is_valid_datetime
from main import is_non_empty_string


def test_nonempty_string():
    empty_string = "   "
    normal_string = " hello   "
    newline_string = "\n   "
    assert is_non_empty_string(empty_string) == False
    assert is_non_empty_string(normal_string) == True
    assert is_non_empty_string(newline_string) == False


class TestCSV(unittest.TestCase):
    # Fixture for common test data
    def setUp(self):
        self.common_data = {
            "rows": [
                {
                    "Project Name": "Ammen (Daniel) Papers.  Collection 811",
                    "Item ARK": "ark:/21198/z1zp5qrx",
                    "Parent ARK": "ark:/21198/zz000937vq",
                    "Item Status ID": "2",
                    "Item Status": "Completed",
                    "Object Type": "Page",
                    "File Name": "ammen/image/21198-zz000937vq_2407642_master.tif",
                    "Visibility": "open",
                    "viewingHint": "",
                    "Type.typeOfResource": "still image",
                    "Rights.rightsHolderContact": "",
                    "Rights.servicesContact": "",
                    "Subject": "",
                    "Name.photographer": "",
                    "Type.genre": "",
                    "Name.creator": "",
                    "Relation.isPartOf": "Daniel Ammen Papers (Collection 811). UCLA Library Special Collections, Charles E. Young Research Library.",
                    "Name.repository": "",
                    "Format.extent": "",
                    "Title": "back",
                    "Format.dimensions": "",
                    "Alt ID.local": "",
                    "Format.medium": "",
                    "AltTitle.descriptive": "",
                    "Description.note": "",
                    "Date.normalized": "",
                    "Finding Aid URL": "",
                    "Opac url": "",
                    "AltTitle.other": "",
                    "Bucketeer State": "succeeded",
                    "IIIF Access URL": "https://iiif.library.ucla.edu/iiif/2/ark%3A%2F21198%2Fz1zp5qrx",
                    "IIIF Manifest URL": "",
                }
            ],
            "validheaders": [
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
            ],
            "fields": [
                "Project Name",
                "Item ARK",
                "Parent ARK",
                "Item Status ID",
                "Item Status",
                "Object Type",
                "File Name",
                "Visibility",
                "viewingHint",
                "Type.typeOfResource",
                "Rights.rightsHolderContact",
                "Rights.servicesContact",
                "Subject",
                "Name.photographer",
                "Type.genre",
                "Name.creator",
                "Relation.isPartOf",
                "Name.repository",
                "Format.extent",
                "Title",
                "Format.dimensions",
                "Alt ID.local",
                "Format.medium",
                "AltTitle.descriptive",
                "Description.note",
                "Date.normalized",
                "Finding Aid URL",
                "Opac url",
                "AltTitle.other",
                "Bucketeer State",
                "IIIF Access URL",
                "IIIF Manifest URL",
            ],
            "file_extension": ".csv",
        }

    def test_correct_file(self):
        errors = []
        Validator.is_csv(
            self.common_data["file_extension"],
            self.common_data["rows"],
            self.common_data["fields"],
            self.common_data["validheaders"],
            errors,
        )
        self.assertEqual(errors, [])

    def test_incorrect_file_extension(self):
        incorrect_file_extension = ".pdf"
        errors = []
        Validator.is_csv(
            incorrect_file_extension,
            self.common_data["rows"],
            self.common_data["fields"],
            self.common_data["validheaders"],
            errors,
        )
        self.assertEqual(
            errors, ["Incorrect file extension (.pdf), please specify a .csv"]
        )

    def test_incorrect_headers(self):
        incorrect_fields = ["hello", "this", "is", "kati"]
        errors = []
        Validator.is_csv(
            self.common_data["file_extension"],
            self.common_data["rows"],
            incorrect_fields,
            self.common_data["validheaders"],
            errors,
        )
        self.assertEqual(errors, ["No valid header row exists in file"])

    def test_empty_file(self):
        empty_rows = []
        empty_fields = []
        errors = []
        Validator.is_csv(
            self.common_data["file_extension"],
            empty_rows,
            empty_fields,
            self.common_data["validheaders"],
            errors,
        )
        self.assertEqual(errors, ["File is empty"])


class TestDatetimeValid(unittest.TestCase):

    # Helper wrapper function to make setting up tests easier
    def datetime_valid_wrapper(self, date_str):
        row = {"Date.normalized": date_str}
        errors = []
        is_valid_datetime(row, 0, errors)
        return errors

    # individual tests below
    def test_single_valid_date(self):
        errors = self.datetime_valid_wrapper("2024-05-18")
        self.assertEqual(len(errors), 0)

    def test_single_invalid_date(self):
        errors = self.datetime_valid_wrapper("2024-5-18")  # month is only one digit
        self.assertNotEqual(len(errors), 0)

    def test_year(self):
        errors = self.datetime_valid_wrapper("1976")
        self.assertEqual(len(errors), 0)

    def test_year_range(self):
        errors = self.datetime_valid_wrapper(
            "1976-1988"
        )  # this should not be allowed in the date.normalized column
        self.assertNotEqual(len(errors), 0)

    def test_year_range_slash(self):
        errors = self.datetime_valid_wrapper("1976/1988")  # date range of only years
        self.assertEqual(len(errors), 0)

    def test_incorrect_year(self):
        errors = self.datetime_valid_wrapper("19761")  # Invalid year
        self.assertNotEqual(len(errors), 0)

    def test_year_month(self):
        errors = self.datetime_valid_wrapper("2004-05")
        self.assertEqual(len(errors), 0)

    def test_single_invalid_date(self):
        errors = self.datetime_valid_wrapper("2024-13-18")  # Invalid month
        self.assertNotEqual(len(errors), 0)

    def test_valid_date_range(self):
        errors = self.datetime_valid_wrapper("2021-01-01/2021-12-31")
        self.assertEqual(len(errors), 0)

    def test_invalid_date_range(self):
        errors = self.datetime_valid_wrapper(
            "2021-01-01/2021-13-31"
        )  # Invalid second date
        self.assertNotEqual(len(errors), 0)

    def test_invalid_format(self):
        errors = self.datetime_valid_wrapper("2024/01/18")  # Non-ISO format
        self.assertNotEqual(len(errors), 0)

    def test_empty_string(self):
        errors = self.datetime_valid_wrapper("")  # Empty string
        self.assertNotEqual(len(errors), 0)
