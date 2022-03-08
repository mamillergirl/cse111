from names import make_full_name, \
    extract_family_name, extract_given_name
from address import extract_state, extract_zipcode, extract_city

import pytest


def test_make_full_name():
    assert make_full_name("Betty", "Brown") == "Brown; Betty"
    assert make_full_name("Lionel", "Messi") == "Messi; Lionel"

def test_extract_family_name(): 
    assert extract_family_name("Brown; Betty") == "Brown"
    assert extract_family_name("Messi; Lionel") == "Messi"

def test_extract_given_name():
    assert extract_given_name("Brown; Betty") == "Betty"
    assert extract_given_name("Messi; Lionel") == "Lionel"
def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
def test_extract_state() :
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

pytest.main(["-v", "--tb=line", "-rN", __file__])
