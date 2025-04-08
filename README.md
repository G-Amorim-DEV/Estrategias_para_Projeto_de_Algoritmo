Desafios de Otimização: Estratégia Gulosa e Programação Dinâmica

Orientações:
Apenas as funções range() e len(), e o método .append(), podem ser usadas nas implementações;
Demais funções e bibliotecas do Python estão proibidas;
Execute as células com os casos de teste propostos para cada uma das funções desenvolvidas.

Implemente uma solução para os seguintes problemas:Transporte de pedras: Tomando N pedras onde cada uma tem peso 1kg maior que a anterior (pedra1=1kg, pedra2=2kg, pedra3=3kg, ..., pedraN=Nkg), determine a forma de transportá-las em um veículo com capacidade máxima de C (kg) por vez com o mínimo de deslocamentos.

A solução para este problema deve ser implementada com a estratégia gulosa.

Corte de toras:Considere uma tora de madeira de comprimento L (m), a qual desejamos cortá-la N vezes em posições determinadas pela lista [p1,p2,p3,...,pN]. Cada corte custa R reais por metro de tora a ser cortada, por exemplo se R=5 e L=10, o valor será R$ 50,00 independente do ponto de corte. Determine o valor total mínimo para os N cortes.

A solução para este problema deve ser implementada com a estratégia de programação dinâmica.

Projeto: Corte de Toras e Transporte de Pedras
Este repositório contém diversos scripts que simulam o processo de corte de toras e transporte de pedras, com implementação em várias linguagens de programação (Python, Java, e Tkinter). Cada script possui uma funcionalidade específica, seja para calcular o custo dos cortes ou organizar o transporte das pedras de acordo com limitações de peso.

Estrutura do Repositório

1. Corte_de_toras.py
Este script em Python realiza os seguintes passos:

Entrada de dados: Solicita ao usuário o comprimento da tora, a quantidade de cortes e o custo por metro cortado.

Validação de cortes: Os cortes inválidos são verificados e descartados.

Ordenação dos cortes: Utiliza o algoritmo de ordenação Insertion Sort para organizar os cortes do maior para o menor.

Cálculo do custo: Calcula o custo total dos cortes e garante que o valor mínimo do custo seja de 50.

Exibição do resultado final: Mostra o custo total dos cortes.

2. Corte_de_toras_tkinter.py
Uma versão do script Corte_de_toras.py, mas com interface gráfica utilizando Tkinter. Este script segue os mesmos passos do script anterior, mas com a interface visual para entrada de dados e exibição dos resultados.

3. Transporte_de_Pedras.java
Este script em Java simula o transporte de pedras, seguindo os seguintes passos:

Entrada de dados: Solicita o peso da pedra mais leve, a quantidade de pedras, o limite de peso do caminhão e a diferença de peso entre as pedras.

Construção da lista de pedras: Gera a lista de pedras com base nos dados fornecidos.

Ordenação das pedras: Ordena as pedras de forma decrescente de peso.

Distribuição das pedras nas viagens: As pedras são distribuídas nas viagens de acordo com o limite de peso do caminhão.

Exibição dos resultados: Exibe a quantidade de viagens necessárias e os detalhes sobre as pedras transportadas.

4. Transporte_de_Pedras_JOptionPane.java
Uma versão do Transporte_de_Pedras.java que utiliza o JOptionPane para interação com o usuário, exibindo mensagens de entrada de dados e resultados de forma mais amigável.

5. Transporte_de_pedras.py
Este script em Python simula o transporte de pedras, seguindo os seguintes passos:

Entrada de dados: Solicita o peso da pedra mais leve, a quantidade de pedras, o limite de peso do caminhão e a diferença de peso entre as pedras.

Construção da lista de pedras: Gera a lista de pedras com base nos dados fornecidos.

Ordenação das pedras: Ordena as pedras de forma decrescente de peso.

Distribuição das pedras nas viagens: As pedras são distribuídas nas viagens de acordo com o limite de peso do caminhão.

Exibição dos resultados: Exibe a quantidade de viagens necessárias e os detalhes sobre as pedras transportadas.

6. Transporte_de_pedras_tkinter.py
Versão do script Transporte_de_pedras.py com interface gráfica utilizando Tkinter. A lógica permanece a mesma, mas agora o script permite ao usuário interagir por meio de uma janela gráfica.

Funcionalidades
Algoritmos de Ordenação: Os scripts utilizam o algoritmo de Insertion Sort para ordenar os cortes ou pedras.

Entrada de Dados: Os usuários fornecem dados como peso, quantidade e limites através de entradas no console ou na interface gráfica (Tkinter ou JOptionPane).

Exibição de Resultados: Os resultados, como custo dos cortes ou quantidade de viagens, são exibidos diretamente na interface ou no console.
