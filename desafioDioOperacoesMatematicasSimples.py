#Solicitar como entrada dois números e depois vamos realizar uma operação simples.

number1 = int(input("Digite um número: "));
number2 = int(input("Digite outro número: "));
operacao = input("Digite a operação que deseja realizar(+, -, *, /): ");

if operacao == '+':
    print("Resultado igual a: ", number1 + number2);
elif operacao == '-':
    print("Resultado igual a: ", abs(number1 - number2));
elif operacao == '*':
    print("Resultado igual a: ", number1 * number2);
elif operacao == '/':
    if number2 ==0:
        print("Não é possível dividir por zero!" );
    else:
        print("Resultado igual a: ", number1 / number2);
else:
    print("Operador Invalido: ");

