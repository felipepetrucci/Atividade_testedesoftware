import pytest
from imc import calcular_imc, classificar_imc

def test_calculo_imc_valor():
    assert calcular_imc(70, 1.75) == 22.86

def test_arredondamento_imc():
    resultado = calcular_imc(70, 1.75)
    assert isinstance(resultado, float)
    assert len(str(resultado).split(".")[1]) <= 2

def test_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_classificacao_abaixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_classificacao_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_classificacao_obesidade_grau_I():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificacao_obesidade_grau_II():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_classificacao_obesidade_grau_III():
    assert classificar_imc(45.0) == "Obesidade grau III"
