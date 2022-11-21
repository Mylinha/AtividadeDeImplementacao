
z = 's'

while(z == 's'):

    x = int(input(" Somar = 1\n Subitrair = 2\n Mutiplicaçao = 3\n divisao = 4\n O que voçe quer?  "))

    if(x == 1):
        num1 =  int(input("Digite um numero: "))
        num2 =  int(input("Digite um numero: "))

        print(f"{num1} + {num2} = {num1 + num2}")

    elif(x == 2):
        num1 =  int(input("Digite um numero: "))
        num2 =  int(input("Digite um numero: "))

        print(f"{num1} - {num2} = {num1 - num2}")
    elif(x == 3):
        num1 =  int(input("Digite um numero: "))
        num2 =  int(input("Digite um numero: "))

        print(f"{num1} x {num2} = {num1 * num2}")
    elif(x == 4):
        num1 =  int(input("Digite um numero: "))
        num2 =  int(input("Digite um numero: "))

        print(f"{num1} / {num2} = {num1 / num2}")

    else:

        print("Opçao nao existente")
    z = input('Digite "s" para continuar' )   
