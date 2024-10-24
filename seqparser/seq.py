# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    #creates a dictionary to map nucleotides from dna to rna 
    complements = {"A":"U", "C":"G", "G":"C", "T":"A"}
    #loops through input sequence and adds appropriate mapped nucleotide to complement sequence
    try:
        complement_seq = "".join(complements[aa] for aa in seq)
    except(KeyError):
        raise ValueError("Invalid nuceleotide in sequence only use A,C,G, or T")
    return complement_seq


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    #calls transcirbe function and reverses the string that is returned 
    return transcribe(seq)[::-1]
