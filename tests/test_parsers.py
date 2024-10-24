# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)
import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

#test if valid fasta files parses correctly 
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    aparser = FastaParser('data/test.fa')
    for record in aparser:
        if '>' not in record[0]:
            assert False
        if not all(char in 'ACGT' for char in record[1]):
            assert False
    
    assert True 
    
#test if valid fastq file parses correctly 
def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    qparser = FastqParser('data/test.fq') 
    for record in qparser:
        if '@' not in record[0]:
            assert False
        if not all(char in 'ACGT' for char in record[1]):
            assert False
    assert True
    
#test if valid fasta files parses correctly 
def test_FastaParser_InvalidEntry():
    aparser = FastaParser('data/negtest.fa')
    with pytest.raises(TypeError):
        for record in aparser:
            pass
    

#test if valid fasta files parses correctly 
def test_FastqParser_InvalidEntry():
    qparser = FastqParser('data/negtest.fq')
    with pytest.raises(TypeError):
        for record in qparser:
            pass

def test_FastqParser_InvalidEntry2():
    qparser = FastqParser('data/negtest2.fq')
    with pytest.raises(TypeError):
        for record in qparser:
            pass
