-- This is a sql script to run to create the database.

CREATE TABLE `Users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) NOT NULL,
  `password` varchar(64) NOT NULL,
  `signup_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `salt` varchar(255) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `email` (`email`)
);
CREATE TABLE `Permissions` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `permission` varchar(20) NOT NULL DEFAULT 'User',
  PRIMARY KEY (`userid`,`permission`)
);
CREATE TABLE `Posts` (
  `userid` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `title` varchar(255) NOT NULL,
  `text` text NOT NULL,
  PRIMARY KEY (`userid`,`title`)
);
CREATE ALGORITHM=UNDEFINED DEFINER=`lewiscb`@`%` SQL SECURITY DEFINER VIEW `GetPermissions` AS select `Users`.`userid` AS `userid`,`Users`.`email` AS `email`,`Users`.`password` AS `password`,`Users`.`signup_date` AS `signup_date`,group_concat(`Permissions`.`permission` separator ', ') AS `permissions` from (`Users` left join `Permissions` on((`Permissions`.`userid` = `Users`.`userid`))) group by `Users`.`userid`;

CREATE TRIGGER `DefaultPermissionAdd` AFTER INSERT ON `Users`
 FOR EACH ROW INSERT INTO Permissions
	(userid, permission)
VALUES
	(NEW.userid, "user");

CREATE TRIGGER `DeletePermissions` AFTER DELETE ON `Users`
 FOR EACH ROW DELETE FROM Permissions
WHERE Permissions.userid = old.userid;

CREATE TRIGGER `DeletePosts` BEFORE DELETE ON `Users`
 FOR EACH ROW DELETE FROM Posts
WHERE Posts.userid = old.userid;