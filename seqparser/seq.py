# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    complements = {"A":"U", "C":"G", "G":"C", "U":"A"}
    complement_seq = ""
    for aa in seq:
        complement_seq += complements[aa]


def reverse_transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA then reverses
    the strand
    """
    return transcribe(seq)[::-1]
