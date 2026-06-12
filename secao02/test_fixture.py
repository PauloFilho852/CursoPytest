import pytest
from fixture import somar

@pytest.fixture
def lista():
    return [1, 2, 3, 4, 5]

def test_somar(lista):
    resultado = somar(lista)
    assert resultado == 15, "Expected the sum of [1, 2, 3, 4, 5] to be 15"