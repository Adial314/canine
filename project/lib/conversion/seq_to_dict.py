# SEQ TO DICTSEQ

from lib.conversion.seqfeature_to_dict import *

def seq_to_dict(seq):
    """
    Converts a Seq object to a dictionary.
    """

    # Initialize dict object
    processed = dict()

    # Process: reverse_complement
    # Type: <method>
    # Skipped, not sure how to convert
    
    # Process: alphabet
    # Type: <method>
    # Skipped.

    # Process: back_transcribe
    # Type: <method>
    # Skipped.

    # Process: complement
    # Type: <method>
    # Skipped.

    # Process: count
    # Type: <method>
    # Skipped.

    # Process: count_overlap
    # Type: <method>
    # Skipped.

    # Process: endswith
    # Type: <method>
    # Skipped.

    # Process: find
    # Type: <method>
    # Skipped.

    # Process: lower
    # Type: <method>
    # Skipped.

    # Process: lstrip
    # Type: <method>
    # Skipped.

    # Process: reverse_complement
    # Type: <method>
    # Skipped.

    # Process: rfind
    # Type: <method>
    # Skipped.

    # Process: rsplit
    # Type: <method>
    # Skipped.

    # Process: rstrip
    # Type: <method>
    # Skipped.

    # Process: split
    # Type: <method>
    # Skipped.

    # Process: startswith
    # Type: <method>
    # Skipped.

    # Process: strip
    # Type: <method>
    # Skipped.

    # Process: tomutable
    # Type: <method>
    # Skipped.

    # Process: tostring
    # Type: <method>() --> string()
    processed['tostring'] = seq.tostring()

    # Process: transcribe
    # Type: <method>
    # Skipped.

    # Process: translate
    # Type: <method>
    # Skipped.

    # Process: ungap
    # Type: <method>
    # Skipped.

    # Process: upper
    # Type: <method>
    # Skipped.

    # Return processed
    return processed
