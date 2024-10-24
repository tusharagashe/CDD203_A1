# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)
import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

#test if postiive case input works as intended 
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """
    test_seq = 'ACGT'
    expected = 'UGCA'
    assert transcribe(test_seq) == expected
    
#test if empty input returns empty output
def test_transcribe_empty():
    test_seq = ''
    expected = ''
    assert transcribe(test_seq) == expected

#test if invalid string returns error 
def test_transcribe_invalid_string():
    test_seq = 'AHFE'
    expected = ''
    with pytest.raises(KeyError):
        transcribe(test_seq)

#test if postive case input works as intended 
def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """
    test_seq = 'ACGT'
    expected = 'ACGU'
    assert reverse_transcribe(test_seq) == expected
    
#test if empty input returns empty output
def test_reverse_transcribe_empty():
    test_seq = ''
    expected = ''
    assert reverse_transcribe(test_seq) == expected

#test if invalid string returns error 
def test_reverse_transcribe_invalid_string():
    test_seq = 'AHFE'
    expected = ''
    with pytest.raises(KeyError):
        reverse_transcribe(test_seq)


