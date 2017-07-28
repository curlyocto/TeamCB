import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

/**
 * Created by dan on 7/17/17.
 * This is the server side, listens on port 8990
 */
public class Server {

    /**Runs the server **/

    public static void main(String[] args) throws IOException {

        ServerSocket listener = new ServerSocket(8990);
        try{
            while(true){
                Socket socket  = listener.accept();
                try{
                    PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                    out.println("Hello, Dave");
                } finally{
                    socket.close();
                }
            }
        }
        finally {
            listener.close();
        }

    }

}
