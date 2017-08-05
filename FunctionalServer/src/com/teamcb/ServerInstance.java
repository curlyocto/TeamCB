package com.teamcb;

import java.io.*;
import java.net.Socket;

public class ServerInstance {

    Socket socket;
    private boolean terminate = false;



    public ServerInstance(Socket s){
        socket = s;
    }


    //Reads a line and echos it back, if line is string exit , terminate is set to true
public void process(BufferedReader input, PrintWriter output) throws IOException{
        String line = input.readLine();
        //Echo the line back
    output.println("Echo: "+line);
    //Flush so data is sent
    output.flush();

    if(line.equalsIgnoreCase("exit")){
        terminate = true;
        System.out.println("Connection terminated");
    }
}

    public void run(){

        try {

            //Asks socket for input stream from client and prints out command
            InputStream inputStream = socket.getInputStream();
          BufferedReader inputReader = new BufferedReader(new InputStreamReader(inputStream));
          OutputStream outputStream = socket.getOutputStream();
          PrintWriter outputWriter = new PrintWriter(new OutputStreamWriter(outputStream));
          //Keeps calling method process until the class variable terminate becomes true
          while(!terminate){
              process(inputReader, outputWriter);
          }
          socket.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
        }
    }

