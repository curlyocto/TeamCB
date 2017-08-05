import java.io.*;
import java.net.Socket;
import java.nio.Buffer;

public class Client {


    public static void main(String args[]) {
        try {
            //Starts socket and looks for host on same machine, with port id
            Socket client = new Socket("localhost", 8990);

            //Asking socket for an output stream
            OutputStream outputStream = client.getOutputStream();

            //Using PrintWriter for ease of one line at a time
            //Writing lines reader from BufferedReader to socket via PrintWriter
            PrintWriter outputWriter = new PrintWriter(new OutputStreamWriter(outputStream));

            InputStream inputStream = client.getInputStream();
            BufferedReader inputReader = new BufferedReader(new InputStreamReader(inputStream));
            BufferedReader cmdReader = new BufferedReader(new InputStreamReader(System.in));
            for(;;){
                System.out.print("Command> ");
                String line = cmdReader.readLine();
                outputWriter.println(line);
                outputWriter.flush();
                if(line.equalsIgnoreCase("exit")){
                    break;
                }

                line  = inputReader.readLine();
                System.out.println("Server wrote: " + line);
            }
            client.close();


        } catch (IOException e) {
            System.out.println(e);
                    }

    }
}
