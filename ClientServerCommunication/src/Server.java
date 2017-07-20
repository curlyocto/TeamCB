import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Created by dan on 7/17/17.
 * This is the server side, listens on port 8990
 */
public class Server {


    public static void main(String[] args) throws IOException {
       // int portNumber = Integer.parseInt(args[0]);

        try {

            {
                ServerSocket serverSocket = new ServerSocket(8900);
                Socket clientSocket = serverSocket.accept();
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            }

        }catch(IOException e){
            System.out.println(e);
        }


    }
}
