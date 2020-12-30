# QUERY NCBI

from Bio import Entrez, SeqIO


def query_ncbi(user, database, term, format):
    """
    Queries records from the selected NCBI database according to the
    search term provided. Returns files formatted in the file_format
    selected by the user.
    
    Input:
        user - the string email of the user making the request
        database - the string name of the selected NCBI database
        term - the string search term conforming to the NCBI query
            guidelines
        file_format - the string abbreviation for the returned
            record format
            
    Output:
        A list of SeqRecord objects
    
    Example:
        query_ncbi("nucleotide", 'CRT[Gene Name] AND "Plasmodium falciparum"[Organism]', "gb")
    """
    
    # Set user email
    Entrez.email = user

    # Reach for the genome terms in the desired database
    handle = Entrez.esearch(db=database, term=term)
    record_list = Entrez.read(handle)

    # Override the return maximum if more records will be returned
    if record_list['RetMax'] < record_list['Count']:
        handle = Entrez.esearch(db=database, term=term, retmax=record_list['Count'])
        record_list = Entrez.read(handle)

    # Retrieve all records with matching IDs
    id_list = record_list['IdList']
    handle = Entrez.efetch(db=database, id=id_list, rettype=format, retmax=record_list['Count'])

    # Read and parse results
    records = list(SeqIO.parse(handle=handle, format=format))
    
    # Format response
    response = dict()
    response['count'] = len(records)
    response['records'] = records
    
    # Return results
    return response
