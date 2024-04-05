base_pimamide = []
numero_tijolos = int(input("Digite o número de tijolos na base da pirâmide: "))

print("Digite os valores dos tijolos da base da pirâmide:")
for i in range(numero_tijolos):
    valor = int(input('Informe um valor para o tijolo: '))
    base_pimamide.append(valor)

piramide = [base_pimamide]
while len(base_pimamide) > 1:
    nova_camada = []
    for i in range(len(base_pimamide) - 1):
        nova_camada.append(base_pimamide[i] + base_pimamide[i+1])
    piramide.insert(0, nova_camada)
    base_pimamide = nova_camada

for nivel in piramide:
    print(nivel)