import random

#Based on this code: https://replit.com/@Joao-FelipeFe10/Password-Generator?v=1

print("*** Bem vindo ao PassWord Generator! ****\nPara gerar a sua senha, por gentileza informe abaixo:")

length_letters = int(input("Qual a quantidade de letras irá usar?\n"))
length_numbers = int(input("Qual a quantidade de números irá usar?\n"))
length_symbols = int(input("Qual a quantidade de símbolos irá usar?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q' ,'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q' ,'R', 'S', 'T', 'U', 'V', 'W', 'X' ,'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

menu = int(input("Selecione o tipo de senha:\n(1) para letras + números + símbolos\n(2) para aleatória\n"))

password = ""

for i in range(0, length_letters):
    password = password+letters[randint(0, len(letters)-1)]
for i in range(0, length_numbers):
    password = password+numbers[randint(0, len(numbers)-1)]
for i in range(0, length_symbols):
    password = password+symbols[randint(0, len(symbols)-1)]
    
if menu==1:
    print(f"Senha:{password}")
elif menu==2:
    password = "".join(sample(password,len(password)))
    print(f"Senha:{password}")
else: 
    print("Opção inválida!")
