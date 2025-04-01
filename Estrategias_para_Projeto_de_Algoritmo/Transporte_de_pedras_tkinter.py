import tkinter as tk
from tkinter import simpledialog, messagebox

def realizar_transporte():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("1 - Passo", "Entrada de dados para o peso da pedra mais leve, quantidade de pedras, limite de peso do caminhão e diferença de peso entre as pedras.")

    inicio = int(simpledialog.askstring("Entrada", "Digite o peso da pedra mais leve: "))
    quantidades = int(simpledialog.askstring("Entrada", "Digite a quantidade de pedras que serão transportadas: "))
    limite = int(simpledialog.askstring("Entrada", "Digite o peso máximo que o caminhão pode transportar: "))
    peso_pedra = int(simpledialog.askstring("Entrada", "Digite a diferença de peso entre as pedras: "))

    messagebox.showinfo("2 - Passo", "Construção da lista de pedras utilizando os dados fornecidos.")
    pedras = []
    for i in range(quantidades):
        pedras.append(inicio + i * peso_pedra)
        messagebox.showinfo(f"Pedra {i+1}", f"Peso = {pedras[i]}")

    messagebox.showinfo("3 - Passo", "Ordenação das pedras em ordem decrescente de peso.")
    for i in range(len(pedras) - 1):
        max_idx = i
        for j in range(i + 1, len(pedras)):
            if pedras[j] > pedras[max_idx]:
                max_idx = j
        pedras[i], pedras[max_idx] = pedras[max_idx], pedras[i]
        messagebox.showinfo(f"Após troca {i+1}", f"Lista de pedras: {pedras}")

    messagebox.showinfo("4 - Passo", "Distribuição das pedras em viagens com base no limite de peso do caminhão, realizando a soma do peso das pedras transportadas em cada viagem.")
    deslocamentos = 0
    viagens = []

    while len(pedras) > 0:
        carga_atual = 0
        pedras_na_viagem = []
        i = 0

        while i < len(pedras):
            if carga_atual + pedras[i] <= limite:
                carga_atual += pedras[i]
                pedras_na_viagem.append(pedras[i])
                pedras.pop(i)
                messagebox.showinfo(f"Adicionada pedra de peso {pedras[i]}", f"Carga atual: {carga_atual}")
            else:
                i += 1

        if len(pedras_na_viagem) > 0:
            viagens.append(pedras_na_viagem)
            deslocamentos += 1
            messagebox.showinfo(f"Viagem {deslocamentos}", f"Pedras transportadas: {pedras_na_viagem} (Peso total: {carga_atual})")

    messagebox.showinfo("5 - Passo", "Exibição dos resultados: quantidade de viagens e detalhes sobre as pedras transportadas.")
    for i in range(len(viagens)):
        peso_total = 0
        for pedra in viagens[i]:
            peso_total += pedra
        messagebox.showinfo(f"Viagem {i + 1}", f"Pedras transportadas - {viagens[i]} (Peso total: {peso_total})")

    messagebox.showinfo("Resultado", f"A quantidade de viagens necessárias para transportar as {quantidades} pedras é de {deslocamentos} viagens.")

root = tk.Tk()
root.withdraw()  
realizar_transporte()
