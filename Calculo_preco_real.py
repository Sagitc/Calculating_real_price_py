import os

print('Bem-vindo ao programa que calcula o valor real da nota e dos produtos')
print('Troque "," por "."')
print('para sair do programa digite "sair".')

diferenca_nota = 0
user_answer = ""

while True:
    
    difer_total_prod = input('\ninsira o valor total dos produtos: ')
    if difer_total_prod == "sair":
        break
    difer_total_nota = input('Insira o valor total da nota: ')
    if difer_total_nota == "sair":
        break

    try:
        valor_prod = float(difer_total_prod)
        valor_nota = float(difer_total_nota)
    except:
        print("\nDigite apenas números, troque ',' por '.'")
        continue

    if valor_nota > valor_prod:
        diferenca_nota = ((valor_nota * 100)/valor_prod)-100
        print(f'\nHá um acréscimo de {diferenca_nota:,.0f}%')
    elif valor_nota < valor_prod:
        diferenca_nota = ((valor_nota * 100)/valor_prod)-100
        print(f'\nHá um desconto de {diferenca_nota:,.0f}%')
    else:
        print('\nNão houve desconto ou acréscimo nessa nota.')
        continue
    
    user_answer = input('\nDeseja calcular o preço real de cada produto? Sim ou Não.  ').lower()

    if user_answer == "sair":
        break
    elif user_answer == "sim":
        os.system('cls')
        print('\nDigite "sair" a qualquer momento para parar de calcular o preço real dos produtos.')

        while user_answer != "sair":

            user_answer = input('\nInforme o preço do produto: ')
            if user_answer == "sair":
                continue
            preco_prod = float(user_answer)
            user_answer = input('informe a quantidade que veio o produto: ')
            quant_prod = int(user_answer)

            preco_real_prod = (preco_prod/quant_prod)
            preco_real_prod = preco_real_prod + (preco_real_prod*(diferenca_nota/100))

            print(f'O preço real desse produto é: {preco_real_prod:,.2f}')
        else:
            break

    elif user_answer == "não":
        break
    else:
        print('Resposta inválida.')

