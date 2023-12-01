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
            name VARCHAR(50) NOT NULL 
        );
    """,
    # Modificar la tabla agregar: 
    """
        CREATE TABLE his_predictions (
            id INT PRIMARY KEY AUTO_INCREMENT,
            id_user INT NOT NULL,
            symbol VARCHAR(6) NOT NULL,
            date_created TIMESTAMP NOT NULL,
            price_created FLOAT NOT NULL,
            
            price_pred_open_30_1 FLOAT,
            price_pred_close_30_1 FLOAT,
            price_pred_max_30_1 FLOAT,
            price_pred_min_30_1 FLOAT,

            price_pred_open_30_3 FLOAT,
            price_pred_close_30_3 FLOAT,
            price_pred_max_30_3 FLOAT,
            price_pred_min_30_3 FLOAT,


            price_pred_open_30_7 FLOAT,
            price_pred_close_30_7 FLOAT,
            price_pred_max_30_7 FLOAT,
            price_pred_min_30_7 FLOAT,


            price_pred_open_07_1 FLOAT,
            price_pred_close_07_1 FLOAT,
            price_pred_max_07_1 FLOAT,
            price_pred_min_07_1 FLOAT,

            price_pred_open_07_3 FLOAT,
            price_pred_close_07_3 FLOAT,
            price_pred_max_07_3 FLOAT,
            price_pred_min_07_3 FLOAT,


            price_pred_open_07_7 FLOAT,
            price_pred_close_07_7 FLOAT,
            price_pred_max_07_7 FLOAT,
            price_pred_min_07_7 FLOAT,

            FOREIGN KEY (id_user) REFERENCES users(id),
            FOREIGN KEY (symbol) REFERENCES stocks(symbol)
        )
    """,
    """
        INSERT INTO stocks (symbol, name) VALUES
            ('GOOGL', 'Alphabet Inc.'),
            ('AMZN', 'Amazon.com Inc.'),
            ('AAPL', 'Apple Inc.'),
            ('MSFT', 'Microsoft Corporation'),
            ('TSLA', 'Tesla, Inc.'),
            ('JPM', 'JPMorgan Chase & Co.'),
            ('V', 'Visa Inc.'),
            ('NVDA', 'NVIDIA Corporation'),
            ('PYPL', 'PayPal Holdings, Inc.'),
            ('DIS', 'The Walt Disney Company');
    """,
    """
        INSERT INTO users (username, email, password, nombre, apellido) VALUES
            ('user', 'user@gmail.com', 'scrypt:32768:8:1$dlRVcZNvwWPLgAO2$d7a47c0d6787b0d55b4ad375b31e4e63e7f903403ce19d3ab668de8ab75fc32478901645c73e70c27f0a642060389972c1b183dabe8f1a5bbe6e9d8621a94eab', 'user', 'user')
    """
]

