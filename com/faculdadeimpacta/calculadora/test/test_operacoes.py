import pytest
from com.faculdadeimpacta.calculadora.operacoes import Operacoes

def test_soma():
	operacoes = Operacoes()
	assert operacoes.soma([1,5]) == 6, "Should be 6"