# FEATURE TO DICT

from lib.conversion.exactposition_to_dict import *

def featurelocation_to_dict(featurelocation):
    """
    Converts a FeatureLocation object to a dictionary.
    """

    # Initialized dict object
    processed = dict()

    # Process: end
    # Type: ExactPosition Object
    processed['end'] = exactposition_to_dict(featurelocation.end)

    # Process: extract
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: nofuzzy_end
    # Type: int()
    processed['nofuzzy_end'] = featurelocation.nofuzzy_end

    # Process: nofuzzy_start
    # Type: int()
    processed['nofuzzy_start'] = featurelocation.nofuzzy_start

    # Process: parts
    # Type: Object, self

    # Process: ref
    # Type: NoneType
    # Skipped.

    # Process: ref_db
    # Type: NoneType
    # Skipped.

    # Process: start
    # Type: ExactPosition Object
    processed['start'] = exactposition_to_dict(featurelocation.start)

    # Process: strand
    # Type: string()
    processed['strand'] = featurelocation.strand

    # Return the processed dict
    return processed
