# REFERENCE TO DICT

from lib.conversion.featurelocation_to_dict import *

def reference_to_dict(reference):
    """
    Converts a Reference object to a dictionary.
    """

    # Initialized dict object
    processed = dict()

    # Process: authors
    # Type: string()
    processed['authors'] = reference.authors
    
    # Process: comment
    # Type: string()
    processed['comment'] = reference.comment
    
    # Process: consrtm
    # Type: string()
    processed['consrtm'] = reference.consrtm
    
    # Process: journal
    # Type: string()
    processed['journal'] = reference.journal
    
    # Process: location
    # Type: FeatureLocation Object
    processed_locations = list()
    for location in reference.location:
        processed_locations.append(featurelocation_to_dict(location))
    processed['location'] = processed_locations
    
    # Process: medline_id
    # Type: string()
    processed['medline_id'] = reference.medline_id
    
    # Process: pubmed_id
    # Type: string()
    processed['pubmed_id'] = reference.pubmed_id
    
    # Process: title
    # Type: string()
    processed['title'] = reference.title

    # Return the processed dict
    return processed
