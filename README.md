🚀 Desafios de Otimização: Estratégia Gulosa e Programação Dinâmica
📌 Regras de Implementação
Apenas as funções range() e len(), e o método .append() podem ser utilizados.

O uso de outras funções e bibliotecas do Python está proibido.

Execute os casos de teste propostos para validar as implementações.

🏗️ Problemas
1️⃣ Transporte de Pedras (Estratégia Gulosa)
Dado um conjunto de N pedras, onde cada pedra possui um peso crescente (pedra1 = 1kg, pedra2 = 2kg, ..., pedraN = Nkg), determine a maneira mais eficiente de transportá-las em um veículo com capacidade máxima de C kg por viagem, minimizando o número de deslocamentos.

🔹 Objetivo: Minimizar a quantidade de viagens necessárias.
🔹 Restrição: Implementação utilizando a estratégia gulosa.

2️⃣ Corte de Toras (Programação Dinâmica)
Dada uma tora de madeira de comprimento L metros, deseja-se cortá-la N vezes em posições específicas definidas por uma lista [p1, p2, p3, ..., pN]. Cada corte tem um custo fixo por metro de tora a ser cortada.

🔹 Objetivo: Determinar o custo total mínimo para realizar os N cortes.
🔹 Restrição: Implementação utilizando programação dinâmica.

Documento de Apresentação dos Códigos 
Introdução 
Neste documento, apresentamos uma breve explicação sobre cada um dos códigos 
contidos nos arquivos listados. Os códigos abordam diferentes aspectos de programação e 
podem ser utilizados em projetos variados.

1. Corte de Toras 
●  Descrição: 
●  Este código é responsável por simular o processo de corte de toras de madeira. 
●  Pode incluir funcionalidades como: 
●  Definição de tamanhos de toras. 
●  Cálculo de quantidade de toras cortadas. 
●  Registro de dados sobre o corte.

Explicação do Código: Transporte de Pedras 
O objetivo deste código é simular o transporte de pedras por um caminhão, organizando as 
pedras em viagens de forma eficiente, considerando o peso limite do veículo. O programa é 
dividido em cinco passos principais:

1 - Entrada de Dados 
O usuário fornece quatro informações essenciais: 
● Peso da pedra mais leve (valor inicial da sequência de pesos das pedras) 
● Quantidade de pedras a serem transportadas 
● Peso máximo que o caminhão pode carregar 
● Diferença de peso entre as pedras (incremento sucessivo de peso) 
Esses valores são lidos usando a função input() e convertidos para int.

2 - Construção da Lista de Pedras 
Com os dados fornecidos, criamos uma lista chamada pedras, onde cada elemento 
representa o peso de uma pedra, calculado com a seguinte fórmula: 
Esse processo é realizado dentro de um laço for.

3 - Ordenação das Pedras (Decrescente) 
Antes de distribuir as pedras no caminhão, é necessário ordená-las em ordem decrescente 
de peso. Isso garante que as pedras mais pesadas sejam consideradas primeiro, permitindo 
um melhor aproveitamento do limite de carga do caminhão. 
A ordenação é feita manualmente utilizando o Selection Sort, onde percorremos a lista e 
encontramos o maior valor para trocar com a posição inicial do laço.

4 - Distribuição das Pedras nas Viagens 
Agora, organizamos as pedras em viagens respeitando o limite de peso do caminhão: 

1. Criamos a variável carga_atual para somar o peso das pedras carregadas.
    
2. Usamos um laço while para percorrer a lista de pedras.
   
3. Para cada pedra, verificamos se seu peso somado à carga_atual não ultrapassa 
o limite do caminhão.

4. Se puder ser transportada, a pedra é adicionada à carga e removida da lista.
   
5. Quando nenhuma outra pedra puder ser adicionada, a carga é registrada como uma 
viagem e o processo recomeça até que todas as pedras tenham sido transportadas. 
Cada viagem concluída é armazenada na lista viagens, e a contagem total de viagens é 
registrada na variável deslocamentos.

5 - Exibição dos Resultados 
No final, exibimos: 
● O número total de viagens necessárias. 
● O conjunto de pedras transportadas em cada viagem, bem como o peso total 
transportado. 
A saída no console apresenta um resumo claro do processo.

Conclusão 
Este código utiliza conceitos importantes de programação, como: 
● Laços de repetição (for e while) 
● Manipulação de listas (adição e remoção de elementos) 
● Ordenação de elementos (Selection Sort) 
● Uso de estruturas condicionais (if para verificar limites de peso) 
Esse método garante que o transporte das pedras seja feito de maneira organizada e 
eficiente, minimizando o número de viagens necessárias para a entrega.
 
2. Corte de Toras com Tkinter 
● Descrição: 
● Este código é uma versão do anterior, mas com uma interface gráfica desenvolvida 
em Tkinter. 
● Funcionalidades adicionais podem incluir: 
● Interação do usuário através de botões e entradas. 
● Visualização dos resultados em tempo real. 
● Melhor usabilidade para quem não está familiarizado com a linha de comando.

Explicação do Código: Transporte de Pedras com Tkinter 
O objetivo deste programa é simular o transporte de pedras por um caminhão, utilizando a 
biblioteca Tkinter para interagir com o usuário por meio de caixas de diálogo e mensagens 
informativas. O programa segue uma estrutura organizada em cinco passos principais:

1 - Entrada de Dados 
O usuário fornece quatro informações essenciais: 
● Peso da pedra mais leve 
● Quantidade total de pedras a serem transportadas 
● Peso máximo suportado pelo caminhão 
● Diferença de peso entre as pedras 
A captura desses valores é feita por meio de caixas de diálogo 
simpledialog.askstring(), onde os dados digitados são convertidos para int.

2 - Construção da Lista de Pedras 
Com os valores inseridos, o programa cria uma lista pedras, armazenando os pesos das 
pedras de acordo com a seguinte fórmula: 
Peso da pedra=Peso inicial+(Posic¸a˜o×Diferenc¸a de peso)\text{Peso da pedra} = 
\text{Peso inicial} + (\text{Posição} \times \text{Diferença de peso}) 
Essa lista é preenchida em um laço for.

3 - Ordenação das Pedras (Decrescente) 
Para otimizar o transporte, as pedras são ordenadas em ordem decrescente de peso, 
garantindo que as mais pesadas sejam carregadas primeiro. A ordenação é realizada 
utilizando o algoritmo Selection Sort, onde encontramos o maior elemento da lista e o 
posicionamos corretamente.

4 - Distribuição das Pedras nas Viagens
O programa distribui as pedras respeitando o limite de peso do caminhão:

1. Cria uma variável carga_atual para somar o peso das pedras carregadas na 
viagem.

2. Percorre a lista pedras e verifica se cada pedra pode ser adicionada sem 
ultrapassar o limite.

3. Se puder, a pedra é adicionada à carga e removida da lista.
   
4. Quando nenhuma outra pedra puder ser adicionada, a carga é registrada e inicia-se 
uma nova viagem. 
As viagens concluídas são armazenadas na lista viagens e contabilizadas na variável 
deslocamentos.

5 - Exibição dos Resultados 
Os resultados são exibidos em caixas de diálogo messagebox.showinfo(), incluindo: 
● O número total de viagens necessárias. 
● As pedras transportadas em cada viagem e o peso total carregado. 

Conclusão 
Este código demonstra o uso de Tkinter para criar interfaces interativas, permitindo ao 
usuário inserir dados e visualizar os resultados de forma mais intuitiva. Além disso, aplica 
conceitos importantes como: 
● Laços de repetição (for e while) 
● Manipulação de listas (adição e remoção de elementos) 
● Ordenação manual (Selection Sort) 
● Uso de condições (if) para verificar limites de peso 
● Interação com interface gráfica (Tkinter) 
Esse método melhora a experiência do usuário e torna o programa mais dinâmico.

3. Transporte de Pedras 
● Descrição: 
● Este código simula o transporte de pedras, possivelmente em um contexto de 
construção ou mineração. 
● Funcionalidades podem incluir: 
● Cálculo de peso total das pedras. 
● Planejamento de rotas de transporte. 
● Registro de tempo e recursos utilizados.

Explicação do Código: Otimização de Cortes em uma Tora 
O objetivo deste programa é calcular o custo mínimo para cortar uma tora de madeira em 
pontos definidos pelo usuário, utilizando programação dinâmica para encontrar a melhor 
sequência de cortes. A estrutura do código segue os seguintes passos:

1 - Entrada de Dados 
O usuário fornece três informações principais: 
● Comprimento total da tora (L) 
● Quantidade de cortes desejados (N) 
● Custo por metro cortado (R) 
Após isso, o usuário informa as posições exatas onde deseja realizar os cortes. Caso algum 
corte esteja fora dos limites da tora (é menor que zero ou maior que L), ele será descartado 
com uma mensagem de aviso.

2 - Adicionando Cortes nas Extremidades 
Para facilitar os cálculos, são adicionadas as posições 0 (início da tora) e L (fim da tora) na 
lista de cortes. Assim, garantimos que a tora sempre seja considerada em sua totalidade.
 
3 - Ordenação dos Cortes 
A lista de cortes é organizada em ordem decrescente utilizando o algoritmo Selection 
Sort. Essa ordenação auxilia no processamento posterior, garantindo que os cortes sejam 
analisados corretamente.

4 - Programação Dinâmica para Encontrar o Custo Mínimo 
Aqui, utilizamos programação dinâmica para calcular o custo mínimo de corte. 
● Criamos uma matriz dp de tamanho (N+2) x (N+2), onde cada elemento 
dp[i][j] representa o custo mínimo para cortar a tora entre os cortes i e j. 
● O preenchimento da tabela ocorre considerando todos os tamanhos de segmentos 
possíveis, do menor para o maior. 
● Para cada intervalo (i, j), buscamos o melhor ponto intermediário k que minimize 
o custo total. 
A fórmula de recursão utilizada é: 
dp[i][j]=min ((cortes[j]−cortes[i])×R+dp[i][k]+dp[k][j])dp[i][j] = \min ( (cortes[j] - cortes[i]) \times 
R + dp[i][k] + dp[k][j] )

5 - Verificação de Viabilidade e Exibição do Resultado 
● Se algum corte for inválido por ultrapassar os limites da tora, ele será ignorado. 
● Caso não seja possível realizar todos os cortes, o programa oferece a opção de 
continuar os cortes restantes em outra tora. 
● Se todos os cortes forem válidos, o programa exibe o custo mínimo necessário 
para realizar os cortes desejados.

Conclusão 
Este código aplica conceitos importantes da computação: 
● Entrada e validação de dados para garantir que os cortes estejam dentro dos 
limites. 
● Ordenação (Selection Sort) para organizar os cortes. 
● Programação Dinâmica para calcular a solução ótima. 
● Uso de estrutura condicional (if) para verificar viabilidade dos cortes. 
● Recursividade para lidar com cortes restantes, permitindo que o usuário decida se 
deseja continuar em outra tora. 
Esse algoritmo é amplamente utilizado na otimização de processos industriais, como corte 
de chapas e barras de materiais.

4. Transporte de Pedras com Tkinter 
● Descrição: 
● Assim como o código anterior, este também possui uma interface gráfica em Tkinter. 
● Funcionalidades adicionais podem incluir: 
● Interface amigável para entrada de dados. 
● Exibição de resultados e gráficos sobre o transporte. 
● Facilitação da interação do usuário com o sistema.

Explicação do Código: Otimização de Cortes em uma Tora (Interface Gráfica - Tkinter) 
O objetivo deste programa é calcular o custo mínimo para cortar uma tora de madeira em 
pontos definidos pelo usuário, utilizando programação dinâmica para encontrar a melhor 
sequência de cortes. Neste código, utilizamos a biblioteca Tkinter para tornar a interação 
mais intuitiva por meio de janelas gráficas. A estrutura do código segue os seguintes 
passos:

1 - Entrada de Dados 
O usuário insere os seguintes valores através de caixas de diálogo: 
● Comprimento total da tora (L) 
● Quantidade de cortes desejados (N) 
● Custo por metro cortado (R) 
Em seguida, informa as posições dos cortes. Se um corte estiver fora dos limites da tora 
(menor que zero ou maior que L), ele é descartado e um aviso é exibido.

2 - Adicionando Cortes nas Extremidades 
Para facilitar os cálculos, são adicionadas as posições 0 (início da tora) e L (fim da tora) na 
lista de cortes. Isso garante que a tora seja considerada em sua totalidade.

3 - Ordenação dos Cortes 
A lista de cortes é organizada em ordem decrescente utilizando o algoritmo Selection 
Sort, garantindo que os cortes sejam analisados corretamente.

4 - Programação Dinâmica para Encontrar o Custo Mínimo 
Criamos uma matriz dp de tamanho (N+2) x (N+2), onde dp[i][j] representa o custo 
mínimo para cortar a tora entre os cortes i e j. O preenchimento da matriz segue a lógica: 
● Para cada intervalo (i, j), buscamos o melhor ponto intermediário k que minimize 
o custo total. 
● A fórmula utilizada é: 
dp[i][j]=min ((cortes[j]−cortes[i])×R+dp[i][k]+dp[k][j])dp[i][j] = \min ( (cortes[j] - cortes[i]) \times 
R + dp[i][k] + dp[k][j] ) 
Isso permite encontrar a sequência de cortes mais econômica.

5 - Verificação de Viabilidade e Exibição do Resultado 
● Se um corte for inválido, um alerta é exibido. 
● Caso não seja possível realizar todos os cortes, o programa oferece a opção de 
continuar os cortes restantes em outra tora. 
● Se todos os cortes forem viáveis, o programa exibe o custo mínimo necessário 
para realizar os cortes desejados. 
Toda a interação com o usuário ocorre por meio de janelas messagebox e simpledialog 
da biblioteca Tkinter, tornando o programa mais amigável.

Conclusão 
Este código aplica conceitos fundamentais de otimização e programação dinâmica, além 
de utilizar interface gráfica (GUI) para aprimorar a experiência do usuário.

Conceitos abordados: 
● Entrada e validação de dados via interface gráfica 
● Ordenação (Selection Sort) 
● Programação Dinâmica para encontrar o custo mínimo 
● Estruturas condicionais (if) para validar cortes 
● Recursividade para lidar com cortes pendentes 
Essa abordagem é utilizada em indústrias para otimizar cortes de madeira, chapas 
metálicas e outros materiais, reduzindo desperdícios e custos.

Conclusão 
Os códigos apresentados são exemplos práticos de como a programação pode ser aplicada 
em diferentes cenários. A utilização de interfaces gráficas, como o Tkinter, demonstra a 
importância da usabilidade em aplicações, tornando-as acessíveis a um público mais amplo. 
Durante a apresentação, será possível discutir cada um dos códigos em mais detalhes e 
responder a perguntas da turma. 
