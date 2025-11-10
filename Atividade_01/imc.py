def calcular_imc(peso, altura):
    if altura == 0:
        raise ValueError("A altura não pode ser zero.")
    imc = peso / (altura ** 2)
    return round(imc, 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

