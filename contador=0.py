print("calculadora:")
operacao=""
while operacao!="sair":
    operacao=input("Qual opração deseja realizar:")
    if operacao=="soma":
         primeiro_numero=int(input("digite o primeiro numero:"))
         segundo_numero=int(input("digite o segundo numero:"))
         resultado=primeiro_numero+segundo_numero
         print(resultado)
    elif operacao=="subtraçao":
         primeiro_numero=int(input("digite o primeiro numero:"))
         segundo_numero=int(input("digite o segundo numero:"))
         resultado=primeiro_numero-segundo_numero
         print(resultado)
    elif operacao=="multiplicaçao":
           primeiro_numero=int(input("digite o primeiro numero:"))
           segundo_numero=int(input("digite o segundo numero:"))
           resultado=primeiro_numero*segundo_numero
           print(resultado)
    elif operacao=="divisao":
            primeiro_numero=int(input("digite o primeiro numero:"))
            segundo_numero=int(input("digite o segundo numero:"))
            resultado=primeiro_numero/segundo_numero
            print(resultado)
print("tchau!!")