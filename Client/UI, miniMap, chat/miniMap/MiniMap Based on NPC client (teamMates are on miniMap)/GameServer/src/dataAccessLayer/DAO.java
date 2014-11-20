package dataAccessLayer;

// Java Imports
import javax.sql.DataSource;

// Library Imports
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

/**
 * The DAO class manages the database connection for executing queries. Uses the
 * GameDB class to create the connection.
 */
public final class DAO {

    private static DAO dao; // References DAO instance
    private GameDB gameDB;
    private DataSource datasource;

    /**
     * Initialize the DAO and create the connection to the database.
     */
    private DAO() {
        System.out.println("\n----------INITIATING DB CONNECTION-----------\n");
        // Configures the database connection
        ApplicationContext beanFactory= new ClassPathXmlApplicationContext("dataAccessLayer/SpringForDB.xml");
        gameDB = (GameDB) beanFactory.getBean("gameDB");

        // Stores the data source to execute queries
        datasource = gameDB.getDataSource();
        System.out.println("\n----------SUCCESSFULLY FINISHED SETTING UP DB CONNECTION-----------\n");
    }

    /**
     * Instantiates the DAO on first execution and return the instance.
     *
     * @return the instance of the DAO
     */
    public static DAO getInstance() {
        if (dao == null) {
            dao = new DAO();
        }

        return dao;
    }

    /**
     * Gets the data source.
     *
     * @return the data source
     */
    public static DataSource getDataSource() {
        return dao.datasource;
    }
}