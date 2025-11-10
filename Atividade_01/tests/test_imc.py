import pytest
from imc import calcular_imc, classificar_imc


# ---- Testes do cálculo do IMC ----

def test_calcular_imc_valor_correto():
    assert calcular_imc(70, 1.75) == 22.86

def test_calcular_imc_duas_casas_decimais():
    resultado = calcular_imc(80, 1.80)
    assert isinstance(resultado, float)
    assert len(str(resultado).split(".")[1]) <= 2  # confere arredondamento

def test_calcular_imc_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

# ---- Testes da classificação do IMC ----

def test_classificar_imc_abaixo_do_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_classificar_imc_peso_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificar_imc_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_classificar_imc_obesidade_grau_I():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificar_imc_obesidade_grau_II():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_classificar_imc_obesidade_grau_III():
    assert classificar_imc(45.0) == "Obesidade grau III"
