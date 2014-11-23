package core;

import model.Player;
import dataAccessLayer.DAO;
import dataAccessLayer.PlayerDAO;

import java.sql.SQLException;
import java.util.Scanner;

public class Test {
	public static void main(String[] args) throws SQLException
	{
		Scanner userInput = new Scanner(System.in);
		Player player = null;
		String username;
		String password;
		int option = 1;
		
		if (DAO.getInstance() == null) {
            System.err.println("Failed to connect to database.");
            System.exit(-1);
        }
		
		while(option > 0)
		{
			System.out.print("1 - Create a character\n2 - Login character\n0 - Exit\n");
			option = userInput.nextInt();
			
			if (option == 1)
			{
				System.out.print("username: ");
				username = userInput.next();
				System.out.print("password: ");
				password = userInput.next();
				
				PlayerDAO.createAccount(username, password);
				System.out.println("Character Created.");
			}
			if (option == 2)
			{
				System.out.print("username: ");
				username = userInput.next();
				System.out.print("password: ");
				password = userInput.next();
				
				if(PlayerDAO.containsUsername(username))
				{
					player = PlayerDAO.getByUsername(username);
					if(player.getPassword().equals(password))
					{
						System.out.print("Welcome " + player.getUsername() + ", your id is " + player.getPlayer_id());
					}
					else
					{
						System.out.print("Your username or password was incorrect");
					}
				}
				else
				{
					System.out.print("Your username or password was incorrect");
				}
				System.out.println();
			}
		}
		
		if(player != null)
		{
			PlayerDAO.updateLogout(player.getPlayer_id(), 10, 10, 10, 10);
		}
		
		userInput.close();
	}
}
