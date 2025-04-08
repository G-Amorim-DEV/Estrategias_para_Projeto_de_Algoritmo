import javax.swing.*;
import java.util.ArrayList;
import java.util.List;

public class TransportePedras {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> realizarTransporte());
    }

    public static void realizarTransporte() {
        // 1º Passo: Entrada de dados
        JOptionPane.showMessageDialog(null, "1 - Passo: Entrada de dados para o peso da pedra mais leve, quantidade de pedras, limite de peso do caminhão e diferença de peso entre as pedras.");

        // Entrada de dados
        int inicio = Integer.parseInt(JOptionPane.showInputDialog("Digite o peso da pedra mais leve: "));
        int quantidades = Integer.parseInt(JOptionPane.showInputDialog("Digite a quantidade de pedras que serão transportadas: "));
        int limite = Integer.parseInt(JOptionPane.showInputDialog("Digite o peso máximo que o caminhão pode transportar: "));
        int pesoPedra = Integer.parseInt(JOptionPane.showInputDialog("Digite a diferença de peso entre as pedras: "));

        // 2º Passo: Construção da lista de pedras
        JOptionPane.showMessageDialog(null, "2 - Passo: Construção da lista de pedras utilizando os dados fornecidos.");
        List<Integer> pedras = new ArrayList<>();
        for (int i = 0; i < quantidades; i++) {
            pedras.add(inicio + i * pesoPedra);
        }

        // 3º Passo: Ordenação das pedras em ordem decrescente de peso
        JOptionPane.showMessageDialog(null, "3 - Passo: Ordenação das pedras em ordem decrescente de peso.");
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

        // 4º Passo: Distribuição das pedras em viagens
        JOptionPane.showMessageDialog(null, "4 - Passo: Distribuição das pedras em viagens com base no limite de peso do caminhão, realizando a soma do peso das pedras transportadas em cada viagem.");
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

        // 5º Passo: Exibição dos resultados
        JOptionPane.showMessageDialog(null, "5 - Passo: Exibição dos resultados: quantidade de viagens e detalhes sobre as pedras transportadas.");
        for (int i = 0; i < viagens.size(); i++) {
            int pesoTotal = 0;
            for (int pedra : viagens.get(i)) {
                pesoTotal += pedra;
            }
            JOptionPane.showMessageDialog(null, "Viagem " + (i + 1) + ": Pedras transportadas - " + viagens.get(i) + " (Peso total: " + pesoTotal + ")");
        }

        JOptionPane.showMessageDialog(null, "Resultado: A quantidade de viagens necessárias para transportar as " + quantidades + " pedras é de " + deslocamentos + " viagens.");
    }
}
