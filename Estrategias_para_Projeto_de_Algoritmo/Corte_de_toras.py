def insertion_sort(cortes):
    print("1 - Passo: Criar um algoritmo de ordenação.")
    for i in range(1, len(cortes)):
        chave = cortes[i]
        j = i - 1
        while j >= 0 and cortes[j] < chave:
            cortes[j + 1] = cortes[j]
            j -= 1
        cortes[j + 1] = chave

def realizar_corte():
    print("2 - Passo: Entrada de dados: comprimento da tora, quantidade de cortes e custo por metro cortado.")

    L = int(input("Digite o comprimento da tora (em metros): "))
    N = int(input("Digite a quantidade de cortes desejados: "))
    R = float(input("Digite o custo por metro de corte: "))

    cortes = []
    cortes_impossiveis = []

    print("3 - Passo: Criar um laço de repetição com as medidas dos cortes que serão realizados.")
    for i in range(N):
        posicao = int(input(f"Digite a posição do corte {i + 1}: "))
        if 0 < posicao < L:
            cortes.append(posicao)
        else:
            cortes_impossiveis.append(posicao)
            print(f"Aviso: O corte na posição {posicao} não pode ser feito, pois excede o comprimento da tora ou é inválido.")

    print("4 - Passo: Verificar se o usuário deseja continuar com os cortes possíveis.")
    if cortes_impossiveis:
        resposta = input("Deseja continuar com os cortes possíveis e ignorar os cortes impossíveis? (s/n): ").strip().lower()
        if resposta == 'n':
            print("Operação cancelada.")
            return
        else:
            print(f"Cortes impossíveis: {cortes_impossiveis}. Serão ignorados.")


    if not cortes:
        print("Não foi possível realizar nenhum corte válido.")
        resposta = input("Você tem outra tora disponível para realizar o corte? (s/n): ").strip().lower()
        if resposta == 's':
            realizar_corte()
        else:
            print("Operação finalizada sem realizar nenhum corte.")
        return

    print("5 - Passo: Ordenando os cortes do maior para o menor.")
    insertion_sort(cortes)
    print(f"Cortes ordenados: {cortes}")

    total = 0

    print("6 - Passo: Calculando o custo total dos cortes.")
    for posicao in cortes:
        custo_corte = posicao * R
        total += custo_corte
        print(f"Corte na posição {posicao}: custo parcial R${custo_corte:.2f}")

    if total < 50:
        total = 50.00

    print("7 - Passo: Exibir o resultado final.")
    print(f"Custo total dos cortes: R${total:.2f}")

realizar_corte()
