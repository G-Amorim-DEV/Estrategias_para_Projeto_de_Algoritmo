import tkinter as tk
from tkinter import simpledialog, messagebox

def insertion_sort(cortes):
    messagebox.showinfo("1 - Passo", "Criar um algoritmo de ordenação.")
    for i in range(1, len(cortes)):
        chave = cortes[i]
        j = i - 1
        while j >= 0 and cortes[j] < chave:
            cortes[j + 1] = cortes[j]
            j -= 1
        cortes[j + 1] = chave

def realizar_corte():
    root = tk.Tk()
    root.withdraw() 

    messagebox.showinfo("2 - Passo", "Entrada de dados: comprimento da tora, quantidade de cortes e custo por metro cortado.")

    L = int(simpledialog.askstring("Entrada", "Digite o comprimento da tora (em metros): "))
    N = int(simpledialog.askstring("Entrada", "Digite a quantidade de cortes desejados: "))
    R = float(simpledialog.askstring("Entrada", "Digite o custo por metro de corte: "))

    cortes = []
    cortes_impossiveis = []

    messagebox.showinfo("3 - Passo", "Criar um laço de repetição com as medidas dos cortes que serão realizados.")
    for i in range(N):
        posicao = int(simpledialog.askstring("Entrada", f"Digite a posição do corte {i + 1}: "))
        if 0 < posicao < L:
            cortes.append(posicao)
        else:
            cortes_impossiveis.append(posicao)
            messagebox.showwarning("Aviso", f"O corte na posição {posicao} não pode ser feito, pois excede o comprimento da tora ou é inválido.")

    messagebox.showinfo("4 - Passo", "Verificar se o usuário deseja continuar com os cortes possíveis.")
    if cortes_impossiveis:
        resposta = simpledialog.askstring("Confirmação", "Deseja continuar com os cortes possíveis e ignorar os cortes impossíveis? (s/n): ").strip().lower()
        if resposta == 'n':
            messagebox.showinfo("Operação cancelada", "Operação cancelada.")
            return
        else:
            messagebox.showinfo("Informação", f"Cortes impossíveis: {cortes_impossiveis}. Serão ignorados.")

    if not cortes:
        messagebox.showinfo("Nenhum corte válido", "Não foi possível realizar nenhum corte válido.")
        resposta = simpledialog.askstring("Novo corte", "Você tem outra tora disponível para realizar o corte? (s/n): ").strip().lower()
        if resposta == 's':
            realizar_corte()
        else:
            messagebox.showinfo("Operação finalizada", "Operação finalizada sem realizar nenhum corte.")
        return

    messagebox.showinfo("5 - Passo", "Ordenando os cortes do maior para o menor.")
    insertion_sort(cortes)
    messagebox.showinfo("Cortes ordenados", f"Cortes ordenados: {cortes}")

    total = 0

    messagebox.showinfo("6 - Passo", "Calculando o custo total dos cortes.")
    for posicao in cortes:
        custo_corte = posicao * R
        total += custo_corte
        messagebox.showinfo("Custo parcial", f"Corte na posição {posicao}: custo parcial R${custo_corte:.2f}")

    if total < 50:
        total = 50.00

    messagebox.showinfo("7 - Passo", "Exibir o resultado final.")
    messagebox.showinfo("Resultado final", f"Custo total dos cortes: R${total:.2f}")

realizar_corte()
