import java.util.HashMap;
import java.util.Map;

public class Banco {
    private Map<String, ContaBancaria> contas = new HashMap<>();

    public void criarConta(String numeroConta, String titular, double saldoInicial) {
        contas.put(numeroConta, new ContaBancaria(numeroConta, titular, saldoInicial));
    }

    public ContaBancaria buscarConta(String numeroConta) {
        return contas.get(numeroConta);
    }

    public void deletarConta(String numeroConta) {
        contas.remove(numeroConta);
    }
}
