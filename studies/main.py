Nome = (input("Digite seu nome: "))
Idade = 20
Altura = 1.67
Peso = 62
IMC = (Peso / Altura ** 2)
print(f"{Nome} tem {Idade} de idade e tem {Altura:.2f} altura e pesa {Peso}kg")

# Indice de Massa Corporal

print(f"Seu indice de massa corporal é {IMC:.4f}")

if IMC >= 25:
   print(f"{Nome}, você está acima do IMC normal!")

else:
    print(f"{Nome}, você está com IMC normal! Parabéns!")
