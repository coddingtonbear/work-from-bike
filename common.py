import textwrap
from xml.etree.ElementTree import tostring

CAMPSITES = {
    'Fort Stevens State Park': {
        'coordinates': [
            46.181933,
            -123.955650,
        ],
    },
    'Big Eddy County Park': {
        'coordinates': [
            45.932151,
            -123.161201,
        ]
    },
    'Nehalem Bay State Park': {
        'coordinates': [
            45.687816,
            -123.935738,
        ]
    },
    'Cape Lookout State Park': {
        'coordinates': [
            45.345250,
            -123.971786,
        ]
    },
    'Perkins Creek Campground': {
        'coordinates': [
            46.084075,
            -123.164363
        ]
    },
    'Fan Creek Campground': {
        'coordinates': [
            45.291408,
            -123.493613
        ]
    },
    'Elk Bend Campground': {
        'coordinates': [
            45.282866,
            -123.540879
        ]
    },
    'Dovre Campground': {
        'coordinates': [
            45.316494,
            -123.479328
        ]
    },
    'Klaskanine River Rv Park': {
        'coordinates': [
            46.092891,
            -123.726482
        ]
    },
    'Champoeg State Park': {
        'coordinates': [
            45.250280,
            -122.895798
        ]
    },
    'Devil\'s Lake State Park': {
        'coordinates': [
            44.968355,
            -124.012593
        ]
    },
    'Beverly Beach State Park': {
        'coordinates': [
            44.730604,
            -124.054809
        ]
    },
    'South Beach State Park': {
        'coordinates': [
            44.606888,
            -124.063288
        ]
    },
    'Elk Creek Campground': {
        'coordinates': [
            45.608212,
            -123.466897
        ]
    },
    'Cape Perpetua Campground': {
        'coordinates': [
            44.281012,
            -124.102064
        ]
    },
    'Rock Creek Campground': {
        'coordinates': [
            44.185698,
            -124.112428
        ]
    },
    'Honeyman State Park': {
        'coordinates': [
            43.930666,
            -124.107696
        ]
    }
}


def format_description(text, **kwargs):
    return textwrap.dedent(
        text.format(**kwargs)
    ).strip()


def format_document(kml_file, namespace="http://www.opengis.net/kml/2.2"):
    """Remove namespace in the passed document in place."""
    doc = kml_file.etree_element()

    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]

    return tostring(doc)
