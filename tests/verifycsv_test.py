from main import Validator


def test_verifycsv():

    # correct csv file
    file_extension = ".csv"
    rows = [
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
    ]
    fields = [
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
    ]
    validheaders = [
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
    errors = []
    Validator.is_csv(file_extension, rows, fields, validheaders, errors)
    assert errors == []

    # wrong file extension
    file_extension = ".pdf"
    errors = []
    Validator.is_csv(file_extension, rows, fields, validheaders, errors)
    assert errors == ["Incorrect file extension (.pdf), please specify a .csv"]

    # invalid header row
    file_extension = ".csv"
    fields = ["hello", "this", "is", "kati"]
    errors = []
    Validator.is_csv(file_extension, rows, fields, validheaders, errors)
    assert errors == ["No valid header row exists in file"]

    # empty csv file
    rows = []
    fields = []
    errors = []
    Validator.is_csv(file_extension, rows, fields, validheaders, errors)
    assert errors == ["File is empty"]
