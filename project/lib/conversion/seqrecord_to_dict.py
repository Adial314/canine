# SEQRECORD TO DICT

from lib.conversion.seqfeature_to_dict import *
from lib.conversion.seq_to_dict import *
from lib.conversion.reference_to_dict import *

def seqrecord_to_dict(seqrecord):
    """
    Converts a SeqRecord object to a dictionary.
    """

    # Initialize dict object
    processed = dict()

    # Process: annotations
    # Type: dict()
    processed_references = list()
    for reference in seqrecord.annotations['references']:
        processed_references.append(reference_to_dict(reference))
    seqrecord.annotations['references'] = processed_references
    seqrecord.annotations['structured_comment']['Assembly-Data'] = dict(seqrecord.annotations['structured_comment']['Assembly-Data'])
    seqrecord.annotations['structured_comment'] = dict(seqrecord.annotations['structured_comment'])
    processed['annotations'] = seqrecord.annotations

    # Process: dbxrefs
    # Type: list()
    processed['dbxrefs'] = seqrecord.dbxrefs

    # Process: description
    # Type: string()
    processed['description'] = seqrecord.description

    # Process: features
    # Type: list(SeqFeature Object)
    processed_features = list()
    for seqfeature in seqrecord.features:
        processed_features.append(seqfeature_to_dict(seqfeature))
    processed['features'] = processed_features

    # Process: format
    # Type: <method>("fasta") --> string()
    processed['format'] = seqrecord.format("fasta")

    # Process: id
    # Type: string()
    processed['id'] = seqrecord.id

    # Process: letter_annotations
    # Type: dict()
    processed['letter_annotations'] = seqrecord.letter_annotations

    # Process: lower
    # Type: <method>() --> SeqRecord Object
    # Skipped, not sure how to convert

    # Process: name
    # Type: string()
    processed['name'] = seqrecord.name

    # Process: reverse_complement
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: seq
    # Type: Seq() object
    processed['seq'] = seq_to_dict(seqrecord.seq)

    # Process: upper
    # Type: <method>
    # Skipped, not sure how to convert

    # Return processed
    return processed
