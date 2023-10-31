import pytest
from tp5funciones import *
#1
@pytest.mark.parametrize('num_dni, res', [
    ('45360529', True),
    ('46473413', True),
    ('24266896', True),
])
def test_dni(num_dni, res):
    assert dni(num_dni) == res

#2
@pytest.mark.parametrize('chain, res', [
    ("hola mundo", 5),
    ("orne la mejor", 5),
    ("dormir", 6)
])
def test_last_word_length(chain, res):
    assert last_word_length(chain) == res

