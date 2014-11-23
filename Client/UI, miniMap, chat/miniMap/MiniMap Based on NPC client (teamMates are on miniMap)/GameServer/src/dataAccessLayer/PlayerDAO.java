package dataAccessLayer;

//Java Imports
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

//Custom Imports
import model.Player;

public final class PlayerDAO {
	
	private PlayerDAO() {
    }
	
	public static int createAccount(String username, String password) throws SQLException {
        int player_id = -1;

        String query = "INSERT INTO `player` (`username`, `password`) VALUES (?, ?)";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query, Statement.RETURN_GENERATED_KEYS);
            pstmt.setString(1, username);
            pstmt.setString(2, password);
            pstmt.execute();

            ResultSet rs = pstmt.getGeneratedKeys();

            if (rs.next()) {
                player_id = rs.getInt(1);
            }

            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return player_id;
    }
	
	public static Player getByPlayerID(int player_id) throws SQLException {
        Player returnPlayer = null;

        String query = "SELECT * FROM `player` WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setInt(1, player_id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnPlayer = new Player(rs.getInt("player_id"));
                returnPlayer.setUsername(rs.getString("username"));
                returnPlayer.setPassword(rs.getString("password"));
                returnPlayer.setX(rs.getFloat("x"));
                returnPlayer.setY(rs.getFloat("y"));
                returnPlayer.setZ(rs.getFloat("z"));
                returnPlayer.setRotation(rs.getInt("rotation"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlayer;
    }
	
	public static Player getByUsername(String username) throws SQLException {
        Player returnPlayer = null;

        String query = "SELECT * FROM `player` WHERE `username` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, username);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                returnPlayer = new Player(rs.getInt("player_id"));
                returnPlayer.setUsername(rs.getString("username"));
                returnPlayer.setPassword(rs.getString("password"));
                returnPlayer.setX(rs.getFloat("x"));
                returnPlayer.setY(rs.getFloat("y"));
                returnPlayer.setZ(rs.getFloat("z"));
                returnPlayer.setRotation(rs.getInt("rotation"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlayer;
    }
	
	public static boolean containsUsername(String username) throws SQLException {
        boolean status = false;

        String query = "SELECT * FROM `player` WHERE `username` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, username);
            ResultSet rs = pstmt.executeQuery();

            status = rs.next();

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return status;
    }
	
	public static void updateLogout(int player_id, float x, float y, float z, float rotation) throws SQLException {
        String query = "UPDATE `player` SET `x` = ?, `y` = ?, `z` = ?, `rotation` = ? WHERE `player_id` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setFloat(1, x);
            pstmt.setFloat(2, y);
            pstmt.setFloat(3, z);
            pstmt.setFloat(4, rotation);
            pstmt.setInt(5, player_id);
            pstmt.execute();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }
    }
	
	public static Player getAccount(String username, String password) throws SQLException {
        Player returnPlayer = null;

        String query = "SELECT * FROM `player` WHERE `username` = ? AND `password` = ?";

        Connection connection = null;
        PreparedStatement pstmt = null;

        try {
            connection = DAO.getDataSource().getConnection();
            pstmt = connection.prepareStatement(query);
            pstmt.setString(1, username);
            pstmt.setString(2, password);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
            	returnPlayer = new Player(rs.getInt("player_id"));
                returnPlayer.setUsername(rs.getString("username"));
                returnPlayer.setPassword(rs.getString("password"));
                returnPlayer.setX(rs.getFloat("x"));
                returnPlayer.setY(rs.getFloat("y"));
                returnPlayer.setZ(rs.getFloat("z"));
                returnPlayer.setRotation(rs.getInt("rotation"));
            }

            rs.close();
            pstmt.close();
        } finally {
            if (connection != null) {
                connection.close();
            }
        }

        return returnPlayer;
    }

}
