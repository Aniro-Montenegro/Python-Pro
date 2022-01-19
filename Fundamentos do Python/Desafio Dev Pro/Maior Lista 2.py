maior= float(input("Digite um valor"))

for _ in range(4):
    maior =max(maior,float(input("Digite um valor")))
print(f"O maior numero é: {maior}")