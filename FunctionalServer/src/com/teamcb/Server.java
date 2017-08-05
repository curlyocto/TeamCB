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

            for(;;){
                Socket socket = server.accept();
                new ServerInstance(socket).run();
            }
            /*
            System.out.println("Server created, waiting for client");
            //returns Socket object once client connects
            Socket socket = server.accept();
            System.out.println("Client has connected");

          */
    } catch (IOException e) {
            e.printStackTrace();
        }


    }

}
