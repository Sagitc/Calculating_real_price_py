import os

def clearTerminal():
    os.system('cls')

def apresentation():
    clearTerminal()
    print('Bem-vindo ao programa que calcula o valor real da nota e dos produtos')
    print('Troque "," por "."')
    print('para sair do programa digite "sair".')

def exitProgram(answer):
    if answer == "sair":
        return quit()

def resultCalculation(valor_produtos, valor_nota):
    try:
        if float(valor_nota) > float(valor_produtos):
            result = ((float(valor_nota) * 100)/float(valor_produtos))-100
            return result
        elif float(valor_nota) < float(valor_produtos):
            result = ((float(valor_nota) * 100)/float(valor_produtos))-100
            return result
        else:
            return print('\nNão houve desconto ou acréscimo nessa nota.')
    except:
        return print('\nTroque "," por "."')

def taxesProducts(preco_produto, quantidade_produto, diferenca_nota):
    result = (preco_produto/quantidade_produto)
    result = result + (result*(diferenca_nota/100))
    return result

apresentation()

while True:
    
    total_produtos = input('\ninsira o valor total dos produtos: ')
    exitProgram(total_produtos)
    total_nota = input('Insira o valor total da nota: ')
    exitProgram(total_nota)

    result = resultCalculation(total_produtos, total_nota)

    if result == None:
        continue
    else:
        if result < 0:
            print(f'\nHouve um desconto de {result:,.0f}%')
        else:
            print(f'\nHouve um acréscimo de {result:+,.0f}%')
    
    user_answer = input('\nDeseja calcular o preço real de cada produto? Sim ou Não.  ').lower()

    exitProgram(user_answer)

    if user_answer == "sim" or user_answer == "yes" or user_answer == "y" or user_answer == "s":
        clearTerminal()

        print('\nDigite "sair" a qualquer momento para parar de calcular o preço real dos produtos.')

        while user_answer != "sair":

            user_answer = input('\nInforme o preço do produto: ')
            exitProgram(user_answer)
            preco_prod = float(user_answer)

            user_answer = input('informe a quantidade que veio o produto: ')
            exitProgram(user_answer)
            quant_prod = int(user_answer)

            preco_real = taxesProducts(preco_prod, quant_prod, result)

            print(f'O preço real desse produto é: {preco_real:,.2f}')
        else:
            break

    elif user_answer == "não" or user_answer == "nao" or user_answer == "no" or user_answer == "n":
        apresentation()
        continue
    else:
        print('\nResposta inválida.')
        break

