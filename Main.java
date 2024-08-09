public class Main {

    public static void main(String[] args) {
        ClienteIA clienteIA = new ClienteIA();
        double[] transacaoExemplo = {5000.0, 100.0, 50.0, 1.0, 0.0}; // Exemplo de uma transação

        boolean ehFraude = clienteIA.verificarFraude(transacaoExemplo);
        System.out.println("A transação é uma fraude? " + ehFraude);
    }
}
