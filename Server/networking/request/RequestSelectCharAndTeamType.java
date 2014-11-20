package networking.request;

// Java Imports
import java.io.IOException;

import networking.response.ResponseLogin;
// Custom Imports
import utility.DataReader;

public class RequestSelectCharAndTeamType extends GameRequest {

    // Data
    private String charType;
    private String faction;
    // Responses
    private ResponseSelectCharAndTeamType responseSelectCharAndTeamType;

    public RequestSelectCharAndTeamType() {
        responses.add(responseSelectCharAndTeamType = new ResponseSelectCharAndTeamType());
    }

    @Override
    public void parse() throws IOException {
        this.charType = DataReader.readString(dataInput);
        //System.out.println("Requesting --------");
        //System.out.println("username: "+charType);
        this.faction = DataReader.readString(dataInput);
        //System.out.println("password: "+faction);
    }

    @Override
    public void doBusiness() throws Exception {
        responseLogin.setCharType(charType);
        responseLogin.setFaction(faction);
        
    }
}
