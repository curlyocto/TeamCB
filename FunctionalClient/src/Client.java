import java.io.*;
import java.net.Socket;

public class Client {


    public static void main(String args[]) {
        try {
            //Starts socket and looks for host on same machine, with port id
            Socket client = new Socket("localhost", 8990);

            //Asking socket for an output stream
            OutputStream outputStream = client.getOutputStream();
            OutputStreamWriter oswriter = new OutputStreamWriter(outputStream);
            //Using PrintWriter for ease of one line at a time
            PrintWriter outputWriter = new PrintWriter(oswriter);
            outputWriter.println("Hello from client");
            //flushes Java I/O buffer to make sure output is sent
            outputWriter.flush();

            InputStream inputStream = client.getInputStream();
            BufferedReader inputReader = new BufferedReader(new InputStreamReader(inputStream));
            System.out.println("Server wrote: " + inputReader.readLine());

        } catch (IOException e) {
            System.out.println(e);
                    }

    }
}
