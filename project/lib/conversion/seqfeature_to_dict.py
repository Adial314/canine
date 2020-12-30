# SEQFEATURE TO DICT

from collections import OrderedDict
from lib.conversion.featurelocation_to_dict import *

def seqfeature_to_dict(seqfeature):
    """
    Converts a SeqFeature object to a dictionary.
    """

    # Initialized dict object
    processed = dict()

    # Process: extract
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: id
    # Type: string()
    processed['id'] = seqfeature.id

    # Process: location
    # Type: Object
    processed['location'] = featurelocation_to_dict(seqfeature.location)

    # Process: location_operator
    # Type: NoneType
    # Skipped.

    # Process: qualifiers
    # Type: OrderedDict()
    processed['qualifiers'] = dict(seqfeature.qualifiers)

    # Process: ref
    # Type: NoneType
    # Skipped.

    # Process: ref_db
    # Type: NoneType
    # Skipped.

    # Process: strand
    # Type: int()
    processed['strand'] = seqfeature.strand

    # Process: type
    # Type: string()
    processed['type'] = seqfeature.type
    
    # Return processed
    return processed
