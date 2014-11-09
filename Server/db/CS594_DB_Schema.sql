-- Users table to keep track of users details of game.  

CREATE TABLE users
(
   user_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(20) NOT NULL,
   password VARCHAR(40) NOT NULL,
   email VARCHAR(80) NOT NULL,
   t_id integer references teams(team_id)
);

-- Teams which user can select at login 

CREATE TABLE teams
(
   team_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
   team_name VARCHAR(40) NOT NULL
);

-- Characters table to access all the information related to character

CREATE TABLE characters
(
  char_id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  char_name VARCHAR(255),
  char_type VARCHAR(255),
  char_location float,
  u_id integer not null references users(user_id)
);