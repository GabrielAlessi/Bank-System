import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ClienteIA {

    public boolean verificarFraude(double[] transacao) {
        try {
            URL url = new URL("http://localhost:5000/predizer_fraude");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json; utf-8");
            conn.setDoOutput(true);

            String jsonInputString = "{\"transacao\":" + java.util.Arrays.toString(transacao) + "}";

            try(OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int code = conn.getResponseCode();
            if (code == 200) {
                // Lógica para processar a resposta
                // Se a API retornar "fraude": true, retorna true
                return true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
