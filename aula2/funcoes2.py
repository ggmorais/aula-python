# divisões, multiplações, adições e subtrações
# numero1, numero2, operacao

def calculadora(numero1, numero2, operacao):
    operacoes = ["+", "-", "/", "*"]

    if operacao not in operacoes:
        print("Operacao não valida!")

    resultado = eval(f"{numero1} {operacao} {numero2}")

    return resultado

# print(calculadora(2, 2, "+"))
# print(calculadora(5, 2, "-"))
# print(calculadora(5, 0, "/"))
# print(calculadora(5, 2, "*"))
# print(calculadora(5, 2, "&"))

