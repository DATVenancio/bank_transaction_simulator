def luhn_validation(numero):
    # Verifica se a string tem 12 dígitos
    if len(numero) != 12 or not numero.isdigit():
        return False
    
    # Converte a string em uma lista de inteiros
    digitos = [int(digito) for digito in numero]

    # Aplica o algoritmo de Luhn
    for i in range(0, 12, 2):
        digitos[i] *= 2
        if digitos[i] > 9:
            digitos[i] -= 9

    # Verifica se a soma dos dígitos é um múltiplo de 10
    return sum(digitos) % 10 == 0

# Exemplo de uso
numero_valido = "123456789015"  # Substitua isso pela sua string de 12 dígitos
if luhn_validation(numero_valido):
    print("O número é válido!")
else:
    print("O número não é válido.")