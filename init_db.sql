REATE DATABASE cooperative_db
    DEFAULT CHARACTER SET utf8mb4    DEFAULT COLLATE utf8mb4_general_ci;


 IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON cooperative_db.* TO 'semyon_petrosyan'@'localhost' IDENTIFIED BY '1234';
FLUSH PRIVILEGES;

