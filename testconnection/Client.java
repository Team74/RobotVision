package testconnection;

import java.net.*;
import java.io.*;

public class Client {
    private Socket socket = null;
    private DataInputStream response = null;
    private DataOutputStream request = null;

    public Client(String _adress, int _port) {
        try {
            socket = new Socket(_adress, _port);
            System.out.println("Connected");
            response = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            request = new DataOutputStream(socket.getOutputStream());
        } catch(UnknownHostException u) {
            System.out.println(u);
        } catch(IOException io) {
            System.out.println(io);
        }

        String line = "";

        while (!line.equals("Over")) {
            try {
                line = System.console().readLine();
                System.out.printf("Read line and got: %s%n", line);
                request.writeUTF(line);
                request.flush();
                System.out.printf("Requested: %s%n", line);
                System.out.printf("Recieved: %s%n", response.readLine());
            } catch(IOException io) {
                System.out.println(io);
            }
        }

        try {
            response.close();
            request.close();
            socket.close();
        } catch (IOException io) {
            System.out.println(io);
        }
    }

    public static void main(String args[]) {
        Client client = new Client("chaoticpi.local", 9999);
    }
}