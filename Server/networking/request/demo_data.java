package networking.request;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;


public class demo_data {

	public static void main(String[] args) {
		
		
		Queue queueA = new LinkedList();
		int protocol_id = 0 ;
		try {
	         File file = new File("src/demo.txt");
	         Scanner scanner = new Scanner(file);
	         while (scanner.hasNextLine()) {
	          
	        	 String print = scanner.nextLine();
	           queueA.add(print);
	         }
	         scanner.close();
	       } catch (FileNotFoundException e) {
	         e.printStackTrace();
	       }

		// save protocol number in protocol_id
		
		if (protocol_id==101){
			// call RequestLogin	
		}
		if (protocol_id==102){
			// call RequestLogout
		}
		if (protocol_id==103){
			// call RequestRegister
		}
		if (protocol_id==104){
			// call RequestCreateCharacter
		}
		if (protocol_id==105){
			// call RequestChat
		}
		if (protocol_id==106){
			// call RequestMove
		}
		if (protocol_id==107){
			// call RequestAttack
		}
		if (protocol_id==108){
			// call RequestHealth
		}
		if (protocol_id==111){
			// call RequestControlPointState
		}
		if (protocol_id==112){
			// call RequestControlPointCap
		}
		if (protocol_id==301){
			// call RequestHeartBeat
		}
}
}
