-- create user for sql with permissions to replica
CREATE USER IF NOT EXISTS `holberton_user`@`localhost` IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO `holberton_user`@`localhost`;
