instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS users;',
    'DROP TABLE IF EXISTS stocks',
    'DROP TABLE IF EXISTS his_predictions',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE users (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(180) NOT NULL,
            nombre VARCHAR(40),
            apellido VARCHAR(40)
        );
    """,
    """
        CREATE TABLE stocks (
            symbol VARCHAR(6) PRIMARY KEY,
            name VARCHAR(30) NOT NULL 
        );
    """,
    """
        CREATE TABLE his_predictions (
            id INT PRIMARY KEY AUTO_INCREMENT,
            id_user INT NOT NULL,
            symbol VARCHAR(6) NOT NULL,
            date_created TIMESTAMP NOT NULL,
            date_prediction TIMESTAMP NOT NULL,
            price_created FLOAT NOT NULL,
            price_prediction FLOAT NOT NULL,
            FOREIGN KEY (id_user) REFERENCES users(id),
            FOREIGN KEY (symbol) REFERENCES stocks(symbol)
        );
    """
]

