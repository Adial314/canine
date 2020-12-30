# EXACTPOSITION TO DICT

def exactposition_to_dict(exactposition):
    """
    Converts a ExactPosition object to a dictionary.
    """

    # Initialize dict object
    processed = dict()

    # Process: bit_length
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: conjugate
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: denominator
    # Type: dict()
    processed['denominator'] = exactposition.denominator

    # Process: extension
    # Type: dict()
    processed['extension'] = exactposition.extension

    # Process: from_bytes
    # Type: <method>
    # Skipped, not sure how to convert

    # Process: imag
    # Type: dict()
    processed['imag'] = exactposition.imag

    # Process: numerator
    # Type: dict()
    processed['numerator'] = exactposition.numerator

    # Process: position
    # Type: dict()
    processed['position'] = exactposition.position

    # Process: real
    # Type: dict()
    processed['real'] = exactposition.real

    # Process: to_bytes
    # Type: <method>
    # Skipped, not sure how to convert

    # Return the processed dict
    return processed
