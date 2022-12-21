-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
CREATE TABLE
    IF NOT EXISTS IS601_S_Attributes(
        id int AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(30),
        value int,
        user_id int,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
        UNIQUE KEY (name, user_id)
    )