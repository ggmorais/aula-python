# divisões, multiplações, adições e subtrações
# numero1, numero2, operacao

def calculadora(operacao, *numeros):
    operacoes = ["+", "-", "/", "*"]

    if operacao not in operacoes:
        print("Operacao não valida!")

    # resultado = eval(f"{numero1} {operacao} {numero2}")
    resultado = 0

    for numero in numeros:
        resultado = eval(f"{resultado} {operacao} {numero}")

    return resultado

if __name__ == "__main__":
    res = calculadora("/", 1, 2, 3, 5, 6)
    print(res)

# "20 / 3 + 10 * (2 + 3)"
# print(calculadora(2, 2, "+"))
# print(calculadora(5, 2, "-"))
# print(calculadora(5, 0, "/"))
# print(calculadora(5, 2, "*"))
# print(calculadora(5, 2, "&"))

