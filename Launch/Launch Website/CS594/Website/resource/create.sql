--for creating the database
drop table if exists users_website;
drop table if exists articles;
create table users_website(
username varchar(255) primary key,
password varchar(255)
);

CREATE TABLE `articles` (
`article_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `article_title` varchar(255) NOT NULL,
  `article_content` text NOT NULL,
  `article_timestamp` int(11) NOT NULL
);

INSERT INTO `articles` (`article_id`, `article_title`, `article_content`, `article_timestamp`) VALUES
(7, 'HI', 'This is the first topic.', 1418196906),
(9, 'sknd', 'lksnd', 1418236396),
(11, 'hey', 'there', 1418259043);

CREATE TABLE `dusers` (
`user_id` int(11) NOT NULL auto_increment primary key,
  `user_name` varchar(255) NOT NULL,
  `user_password` varchar(255) NOT NULL
);

INSERT INTO `dusers` (`user_id`, `user_name`, `user_password`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3'),
(2, 'jay', '2f79f3cd6f3d3d0ffdd14e61cf2d059c'),
(6, 'gaurav', '1630937c3d00b4f4b153599d93469963');