## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
   salario = float(input('Digite o valor do salario: '))
aumento = float(input('Digite o valor do aumento em porcentagem: '))

aumento_calculado = salario * aumento / 100
salario_calculado = salario + aumento_calculado

print('O valor do aumento é de R$ %.2f.' % aumento_calculado)
print('O novo salario é de R$ %.2f.' % salario_calculado)



if __name__ == '__main__':
    main()
