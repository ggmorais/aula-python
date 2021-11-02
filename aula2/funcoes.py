# divisões, multiplações, adições e subtrações
# numero1, numero2, operacao

def calculadora(numero1, numero2, operacao):
    resultado = 0

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "/":
        if numero2 == 0:
            print("Algum numero é zero!")
            return
        resultado = numero1 / numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    else:
        print("Operação invalida!")
        return

    return resultado

# print(calculadora(2, 2, "+"))
# print(calculadora(5, 2, "-"))
# print(calculadora(5, 0, "/"))
# print(calculadora(5, 2, "*"))
print(calculadora(5, 2, "&"))
