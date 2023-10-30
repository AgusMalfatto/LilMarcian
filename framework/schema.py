instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    # Agregar drop table de las tablas
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE user (
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(120) NOT NULL
        )
    """
    # Agregar esquemas de las tablas
]

