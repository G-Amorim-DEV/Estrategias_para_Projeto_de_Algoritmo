Desafios de Otimização: Estratégia Gulosa e Programação Dinâmica

Orientações:
Apenas as funções range() e len(), e o método .append(), podem ser usadas nas implementações;
Demais funções e bibliotecas do Python estão proibidas;
Execute as células com os casos de teste propostos para cada uma das funções desenvolvidas.

Implemente uma solução para os seguintes problemas:Transporte de pedras: Tomando N pedras onde cada uma tem peso 1kg maior que a anterior (pedra1=1kg, pedra2=2kg, pedra3=3kg, ..., pedraN=Nkg), determine a forma de transportá-las em um veículo com capacidade máxima de C (kg) por vez com o mínimo de deslocamentos.

A solução para este problema deve ser implementada com a estratégia gulosa.

Corte de toras:Considere uma tora de madeira de comprimento L (m), a qual desejamos cortá-la N vezes em posições determinadas pela lista [p1,p2,p3,...,pN]. Cada corte custa R reais por metro de tora a ser cortada, por exemplo se R=5 e L=10, o valor será R$ 50,00 independente do ponto de corte. Determine o valor total mínimo para os N cortes.

A solução para este problema deve ser implementada com a estratégia de programação dinâmica.

1. Transporte de Pedras (Estratégia Gulosa)
Descrição
Este código simula o transporte de pedras por um caminhão, utilizando a estratégia gulosa para minimizar o número de viagens necessárias. O programa organiza as pedras em viagens respeitando o limite de carga do caminhão.

Objetivo
Minimizar a quantidade de viagens necessárias, utilizando a estratégia gulosa.

Como Funciona:
Entrada de Dados: O programa solicita o peso da pedra mais leve, a quantidade total de pedras, o peso máximo que o caminhão pode carregar, e a diferença de peso entre as pedras.

Construção da Lista de Pedras: A partir dos dados fornecidos, o programa gera uma lista de pedras com pesos crescentes.

Ordenação das Pedras: As pedras são ordenadas de forma decrescente, para garantir que as mais pesadas sejam carregadas primeiro.

Distribuição nas Viagens: O programa distribui as pedras no caminhão respeitando o limite de peso, organizando as pedras de forma a minimizar o número de viagens.

Exibição dos Resultados: O programa exibe o número total de viagens e os detalhes de cada viagem.

Conclusão
Este código utiliza conceitos como laços de repetição, manipulação de listas, ordenação e verificação de condições. Ele otimiza a carga de um caminhão para minimizar o número de viagens necessárias, utilizando a estratégia gulosa.

2. Corte de Toras (Programação Dinâmica)
Descrição
Este código resolve o problema de cortar uma tora de madeira de comprimento L metros em posições específicas com o menor custo possível. Ele utiliza programação dinâmica para encontrar a sequência de cortes mais econômica.

Objetivo
Determinar o custo total mínimo para realizar os N cortes em uma tora de madeira, utilizando programação dinâmica.

Como Funciona:
Entrada de Dados: O usuário fornece o comprimento da tora, a quantidade de cortes desejados, e o custo por metro cortado.

Adicionando Cortes nas Extremidades: O código adiciona as posições 0 e L na lista de cortes, representando as extremidades da tora.

Ordenação dos Cortes: A lista de cortes é ordenada utilizando o algoritmo Selection Sort.

Programação Dinâmica: O programa preenche uma tabela de programação dinâmica, onde cada célula dp[i][j] representa o custo mínimo para cortar entre as posições i e j.

Cálculo do Custo Mínimo: A fórmula recursiva é aplicada para calcular o custo mínimo de corte entre cada par de cortes.

Conclusão
Este código aplica conceitos fundamentais de programação dinâmica, como a criação de uma tabela de DP e a busca de uma solução ótima para o problema do corte de toras.

3. Transporte de Pedras com Tkinter
Descrição
Este código simula o transporte de pedras utilizando a biblioteca Tkinter para interagir com o usuário através de uma interface gráfica. Ele segue os mesmos princípios da estratégia gulosa, mas com uma interface mais amigável.

Objetivo
Simular o transporte de pedras com uma interface gráfica e minimizar o número de viagens necessárias.

Como Funciona:
Entrada de Dados: O usuário insere os dados através de caixas de diálogo do Tkinter, como o peso da pedra mais leve, a quantidade total de pedras, o peso máximo do caminhão e a diferença de peso entre as pedras.

Construção da Lista de Pedras: A lista de pedras é gerada a partir dos dados fornecidos.

Ordenação das Pedras: As pedras são ordenadas em ordem decrescente de peso.

Distribuição nas Viagens: O código distribui as pedras nas viagens respeitando o limite de peso do caminhão.

Exibição dos Resultados: O número total de viagens e as pedras transportadas em cada viagem são exibidos em caixas de mensagem do Tkinter.

Conclusão
Este código utiliza Tkinter para criar uma interface gráfica interativa, tornando a experiência do usuário mais intuitiva. A lógica de transporte de pedras segue a estratégia gulosa, mas com a vantagem de ser mais acessível.

4. Corte de Toras com Tkinter
Descrição
Este código resolve o problema de corte de toras de madeira com a ajuda da programação dinâmica, apresentando os resultados através de uma interface gráfica utilizando o Tkinter.

Objetivo
Calcular o custo mínimo para realizar os cortes em uma tora de madeira, com interface gráfica para facilitar a interação do usuário.

Como Funciona:
Entrada de Dados: Através de caixas de diálogo, o usuário insere o comprimento da tora, o número de cortes e o custo por metro cortado.

Adicionando Cortes nas Extremidades: As posições 0 e L são adicionadas à lista de cortes.

Ordenação dos Cortes: A lista de cortes é ordenada em ordem crescente usando o algoritmo Selection Sort.

Programação Dinâmica: Uma tabela de programação dinâmica é preenchida para calcular o custo mínimo para realizar os cortes entre as posições selecionadas.

Exibição do Resultado: O programa exibe o custo mínimo dos cortes, informando o usuário sobre os detalhes do processo.

Conclusão
Este código aplica a programação dinâmica para otimização do custo de cortes e utiliza Tkinter para proporcionar uma experiência de usuário interativa e amigável. Ele permite visualizar de forma clara os resultados e interagir facilmente com a aplicação.

Conclusão Geral
Os códigos apresentados utilizam conceitos de otimização (estratégia gulosa e programação dinâmica) para resolver problemas práticos de transporte e corte de materiais. O uso da biblioteca Tkinter nos dois últimos códigos torna as aplicações mais acessíveis e fáceis de usar. Cada solução implementada foi projetada para ser eficiente e apresentar os resultados de maneira clara, garantindo uma experiência de usuário mais intuitiva.
