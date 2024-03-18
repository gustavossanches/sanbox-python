texto = "Este é o texto que vai ser utilizado no exercício!"
caractere = '--'
while(len(caractere) > 1):  
    caractere = str(input("Digite um caractere (apenas um): "))

if caractere in texto:
    print(f'O caractere "{caractere}" está presente no texto!')
else:
    print(f'O caractere "{caractere}" NÃO está presente no texto!')
print(texto)
