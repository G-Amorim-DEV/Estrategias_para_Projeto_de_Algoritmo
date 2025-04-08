import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TransportePedras {

    public static void main(String[] args) {
        realizarTransporte();
    }

    public static void realizarTransporte() {
        // Passo 1: Entrada de dados
        System.out.println("1 - Passo: Entrada de dados para o peso da pedra mais leve, quantidade de pedras, limite de peso do caminhão e diferença de peso entre as pedras.");
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o peso da pedra mais leve: ");
        int inicio = scanner.nextInt();
        
        System.out.print("Digite a quantidade de pedras que serão transportadas: ");
        int quantidades = scanner.nextInt();
        
        System.out.print("Digite o peso máximo que o caminhão pode transportar: ");
        int limite = scanner.nextInt();
        
        System.out.print("Digite a diferença de peso entre as pedras: ");
        int pesoPedra = scanner.nextInt();

        // Passo 2: Construção da lista de pedras
        System.out.println("2 - Passo: Construção da lista de pedras utilizando os dados fornecidos.");
        List<Integer> pedras = new ArrayList<>();
        for (int i = 0; i < quantidades; i++) {
            pedras.add(inicio + i * pesoPedra);
        }

        // Passo 3: Ordenação das pedras em ordem decrescente de peso
        System.out.println("3 - Passo: Ordenação das pedras em ordem decrescente de peso.");
        for (int i = 0; i < pedras.size() - 1; i++) {
            int maxIdx = i;
            for (int j = i + 1; j < pedras.size(); j++) {
                if (pedras.get(j) > pedras.get(maxIdx)) {
                    maxIdx = j;
                }
            }
            // Troca as pedras
            int temp = pedras.get(i);
            pedras.set(i, pedras.get(maxIdx));
            pedras.set(maxIdx, temp);
        }

        // Passo 4: Distribuição das pedras em viagens
        System.out.println("4 - Passo: Distribuição das pedras em viagens com base no limite de peso do caminhão, realizando a soma do peso das pedras transportadas em cada viagem.");
        int deslocamentos = 0;
        List<List<Integer>> viagens = new ArrayList<>();

        while (!pedras.isEmpty()) {
            int cargaAtual = 0;
            List<Integer> pedrasNaViagem = new ArrayList<>();
            int i = 0;

            while (i < pedras.size()) {
                if (cargaAtual + pedras.get(i) <= limite) {
                    cargaAtual += pedras.get(i);
                    pedrasNaViagem.add(pedras.get(i));
                    pedras.remove(i);
                } else {
                    i++;
                }
            }

            if (!pedrasNaViagem.isEmpty()) {
                viagens.add(pedrasNaViagem);
                deslocamentos++;
            }
        }

        // Passo 5: Exibição dos resultados
        System.out.println("5 - Passo: Exibição dos resultados: quantidade de viagens e detalhes sobre as pedras transportadas.");
        for (int i = 0; i < viagens.size(); i++) {
            int pesoTotal = 0;
            for (int pedra : viagens.get(i)) {
                pesoTotal += pedra;
            }
            System.out.println("Viagem " + (i + 1) + ": Pedras transportadas - " + viagens.get(i) + " (Peso total: " + pesoTotal + ")");
        }

        System.out.println("Resultado: A quantidade de viagens necessárias para transportar as " + quantidades + " pedras é de " + deslocamentos + " viagens.");

        scanner.close();
    }
}
