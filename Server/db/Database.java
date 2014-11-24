package core;

import java.sql.*;
import java.util.ArrayList;

import model.CharacterModel;
import model.UserModel;

public class Database {
	private Connection connect = null;
	private Statement statement = null;
	private PreparedStatement preparedStatement = null;
	private ResultSet resultSet = null;

	public Database() {
		// creates an account and character for the user
		System.out.println("Creating Connection");
		try {
			startConnection();
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("Connection Finished");
	}

	// // User_id from users table.
	public int getuid(String username) {
		int uid = 0;
		try {
			preparedStatement = connect
					.prepareStatement("SELECT user_id FROM users WHERE username=?");
			preparedStatement.setString(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				uid = rs.getInt("user_id");
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {

		}
		return uid;
	}

	// List of character_name through u_id.
	public ArrayList<String> char_name(String username, int team_id) {
		ArrayList<String> charnamelist = new ArrayList<String>();

		try {
			preparedStatement = connect.prepareStatement("SELECT user_id FROM users WHERE username=?");
			preparedStatement.setString(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			if (rs.next()) {
				int uid = rs.getInt("user_id");
				preparedStatement = connect
						.prepareStatement("select * from characters c inner join teams t on c.t_id = t.team_id where u_id = ? and t_id =?");
				preparedStatement.setInt(1, uid);
				preparedStatement.setInt(1, team_id);

				ResultSet rs1 = preparedStatement.executeQuery();
				while (rs1.next()) {

					String charname = rs.getString("char_name");
					charnamelist.add(charname);

				}
			}
		} catch (Exception e) {

		}
		return charnamelist;
	}

	public void startConnection() throws Exception {
		try {
			// this will load the MySQL driver, each DB has its own driver
			Class.forName("com.mysql.jdbc.Driver");
			// setup the connection with the DB.
			connect = DriverManager.getConnection(
					"jdbc:mysql://localhost/cs594db", "root", "abcd");
			System.out.println("Connection to DATABASE Success");
		} catch (Exception e) {
			System.out.println("Unable to Connect to DATABASE");
			throw e;
		}

	}

	// you need to close all three to make sure
	@SuppressWarnings("unused")
	private void close() {
		try {
			resultSet.close();
			statement.close();
			connect.close();
		} catch (Exception e) {
			// do something here if it doesnt close.
		}
	}

	// User Registration with unique user name validation
	public boolean createAccount(String username, String password) {
		String u = username.trim();

		try {
			if (hasAccount(u) == false)
				;
			{
				preparedStatement = connect
						.prepareStatement("INSERT INTO users (username, password,Isconnected) VALUES (?, ? ,?)");

				preparedStatement.setString(1, u);
				preparedStatement.setString(2, password);
				preparedStatement.setBoolean(3, false);
				if (preparedStatement.executeUpdate() != 0) {
					// it was added sucessfully
					System.out.println("added successfully");
					preparedStatement.close();

					preparedStatement.close();
				} else {
					// not so successful
					System.out.println("Could not create account");
				}
				preparedStatement.close();
			}
		} catch (Exception e) {

		}
		return true;
	}

	// Create Character with already exist character with user id
	public boolean CreateCharacter(Integer char_type, String char_name,String username, Integer t_id) {
		boolean status = false;
		preparedStatement = connect.prepareStatement("SELECT user_id FROM users WHERE username=?");
		preparedStatement.setString(1, username);
		ResultSet rs = preparedStatement.executeQuery();
		if (rs.next()) {
			int uid = rs.getInt("user_id");
		   try {
            preparedStatement = connect.prepareStatement("INSERT INTO characters (char_name,char_type,u_id,t_id) VALUES (?, ? ,?,?)");
			preparedStatement.setString(1, char_name);
			preparedStatement.setInt(2, char_type);
			preparedStatement.setInt(3, uid);
			preparedStatement.setInt(4, t_id);
			if (preparedStatement.executeUpdate() != 0) {
				// it was added sucessfully
				System.out.println("create successfully");
				status = true;
			} else {
				// not so successful
				System.out.println("Could not create  create");
				status = false;
			}

		} 
		
		catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {

				preparedStatement.close();
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		return status;
		}
	}

	// Login Interface or validation Method
	public boolean ValidateUser(String username, String password) {

		boolean status = false;

		try {
			preparedStatement = connect
					.prepareStatement("SELECT * FROM users WHERE username=? AND BINARY password=?");
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);

			ResultSet rs = preparedStatement.executeQuery();

			if (rs.next()) {
				status = true;
			}

		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			try {
				// resultSet.close();
				preparedStatement.close();
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
		return status;
	}

	// After User Login throw predefined team location to specific character
	public String[] GetcharacterLoc(String username, String password,
			Integer t_id) {
		// boolean result = false;
		String[] info = new String[5];
		String ui = null;
		String ci = null;
		try {
			preparedStatement = connect
					.prepareStatement("SELECT * FROM users WHERE username=? AND BINARY password=?");
			preparedStatement.setString(1, username);
			preparedStatement.setString(2, password);

			ResultSet rs = preparedStatement.executeQuery();
			if (rs.next()) {
				int uid = rs.getInt("user_id");
				PreparedStatement p2 = connect
						.prepareStatement("select * from characters where u_id=?");
				p2.setInt(1, uid);
				ResultSet rs1 = p2.executeQuery();
				if (rs1.next()) {
					PreparedStatement p3 = connect
							.prepareStatement("select * from teams where t_id=?");
					p3.setInt(1, t_id);
					ResultSet rs2 = p3.executeQuery();
					String xPos = String.valueOf(rs2.getDouble("start_x_pos"));
					String yPos = String.valueOf(rs.getDouble("start_y_pos"));
					String zPos = String.valueOf(rs.getDouble("start_z_pos"));

					ci = String.valueOf(rs1.getInt("c_id"));

					info[0] = ci;
					info[1] = ui;
					info[2] = xPos;
					info[3] = yPos;
					info[4] = zPos;
					p3.close();
					rs2.close();
				}

				p2.close();
				rs1.close();
			}

			rs.close();
			preparedStatement.close();
		} catch (Exception e) {

		}
		return info;
	}

	// Method for Unique user name validation
	public boolean hasAccount(String username) {
		boolean result = true;
		ArrayList<Integer> s = new ArrayList<Integer>();
		try {
			preparedStatement = connect.prepareStatement("SELECT * FROM users WHERE username=?");
			preparedStatement.setString(1, username);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				s.add(rs.getInt("user_id"));
			}
			if (s.size() == 0) {
				result = false;
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {

		}
		return result;
	}

	// Character validation method
	public boolean hasCharacter(Integer u_id) {
		boolean result = true;
		ArrayList<Integer> s = new ArrayList<Integer>();
		try {
			preparedStatement = connect
					.prepareStatement("SELECT * FROM charaters WHERE u_id=?");
			preparedStatement.setInt(1, u_id);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				s.add(rs.getInt("user_id"));
			}
			if (s.size() == 0) {
				result = false;
			}
			rs.close();
			preparedStatement.close();
		} catch (Exception e) {

		}
		return result;
	}

	// Get all connected users //
	public ArrayList<String> getConnectedusers() {
		ArrayList<String> s = new ArrayList<String>();
		try {
			preparedStatement = connect.prepareStatement("SELECT username FROM user WHERE Isconnected = true");
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				s.add(rs.getString("username"));
			}
		} catch (Exception e) {

		}
		return s;
	}

	 // Get all connected users id's //
	public ArrayList<Integer> getConnectedusers_Id() {
		ArrayList<Integer> s = new ArrayList<Integer>();
		try {
			preparedStatement = connect.prepareStatement("SELECT user_id FROM user WHERE Isconnected = true");
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				s.add(rs.getInt("user_id"));
			}
		} catch (Exception e) {

		}
		return s;
	}

	public String getUsername(int uid) {
		String result = "USERNAME#";
		try {
			preparedStatement = connect.prepareStatement("SELECT username FROM users WHERE user_id=?");
			preparedStatement.setInt(1, uid);
			ResultSet rs = preparedStatement.executeQuery();
			if (rs.next()) {
				result += rs.getString("username");
			} else {
				result += "0";
			}
		} catch (Exception e) {

		}
		return result;
	}
	
	// // List of All Online user in specific team characters
	public ArrayList<Integer> getAllConnectedCharacter(String uname, Integer team_num) {
		int uid = getuid(uname);
		ArrayList<Integer> onlinecharacter = new ArrayList<Integer>();
		try {
			preparedStatement = connect.prepareStatement("select * from characters c inner join users u on c.u_id = u.user_id where u_id =?, team_num = ?");
			preparedStatement.setInt(1, uid);
			preparedStatement.setInt(2, team_num);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				Integer c = rs.getInt("c_id");
                onlinecharacter.add(c);
				
			}
		} catch (Exception e) {

		}
		return onlinecharacter;
	}


	// List of characters through username
	public ArrayList<CharacterModel> getCharacterfromUser(String uname) {
		int uid = getuid(uname);
		ArrayList<CharacterModel> c = new ArrayList<CharacterModel>();
		try {
			preparedStatement = connect.prepareStatement("select *,t.team_num from characters c inner join teams t on c.t_id = t.team_id where u_id = ?");
			preparedStatement.setInt(1, uid);
			ResultSet rs = preparedStatement.executeQuery();
			while (rs.next()) {
				int tn = rs.getInt("team_num");

				c.add(new CharacterModel(rs.getInt("char_id"), rs
						.getInt("char_type"), uname, tn));

			}
		} catch (Exception e) {

		}
		return c;
	}

	public UserModel getUserbyUsername(String uname) {
		UserModel u = new UserModel();
		try {
			preparedStatement = connect
					.prepareStatement("SELECT * FROM users WHERE username=?");
			preparedStatement.setString(1, uname);
			ResultSet rs = preparedStatement.executeQuery();
			if (rs.next()) {
				u.setUserid(rs.getInt("user_id"));
				u.setUsername(uname);
				u.setPassword(rs.getString("password"));
				u.setIsConnected(rs.getBoolean("Isconnected"));
			}
		} catch (Exception e) {

		}
		return u;
	}

	public int getUid(String uname) {
		int result = 0;
		try {
			preparedStatement = connect
					.prepareStatement("SELECT user_id FROM users WHERE username=?");
			preparedStatement.setString(1, uname);
			ResultSet rs = preparedStatement.executeQuery();
			if (rs.next()) {
				result = rs.getInt("user_id");
			}
		} catch (Exception e) {

		}
		return result;
	}
}
