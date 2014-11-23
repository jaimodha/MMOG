This test client and the test server are very much a patch job.

Start the server by running the GameServer class.

The fake login I made takes a username, the type of character based on 0 for swordsman and 1 for axeman and the faction also a 0 or 1.  Also important is that the server doesn't check for username uniqueness but the client needs it so don't name two test guys the same thing.

The files that are meant to be used as our part of the network code are:
ResponseCharacterAttack.py
ResponseCharacterChangeHealth.py
ResponseCharacterMovement.py
RequestCharacterAttack.py
RequestCharacterChangeHealth.py
RequestMove.py

ResponseCharacterAttack.java
ResponseCharacterChangeHealth.java
ResponseCharacterMovement.java
RequestCharacterAttack.java
RequestCharacterChangeHealth.java
RequestMove.java

As a note I altered the CharacterModel class to work with the protocol.  May cause problems during integration.

For the ResponseCharacterAttack.py I put animateAttack as the place holder for making a character do an attack animation without calculating targets or anything.  So replace that with the function to do that animation.