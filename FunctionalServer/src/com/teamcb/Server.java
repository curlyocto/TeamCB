package com.teamcb;
import com.sun.org.apache.xpath.internal.SourceTree;

import java.net.*;
import java.io.*;


public  class Server {


    public static void main(String args[]) {


        try {
            //instantiate instance of java.net.ServerSocket and specifics port
            //Once server establishes it main socket server, creates new instance of ServerInstance

            ServerSocket server = new ServerSocket(8990);
           


            System.out.println("Server created, waiting for client");
            //returns Socket object once client connects
            Socket socket = server.accept();
            System.out.println("Client has connected");
            //Asks socket for input stream from client and prints out command
            InputStream inputStream = socket.getInputStream();
            InputStreamReader isReader = new InputStreamReader(inputStream);
            //Turning input stream into BufferedReader to make data easier to read one line at a time
            BufferedReader inputReader = new BufferedReader(isReader);
            System.out.println("Client wrote: " + inputReader.readLine());


            OutputStream outputStream = socket.getOutputStream();
            PrintWriter outputWriter = new PrintWriter(new OutputStreamWriter(outputStream));
            outputWriter.println("Hello from server");
            outputWriter.flush();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

