from main import Validator
import pytest
import unittest


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
