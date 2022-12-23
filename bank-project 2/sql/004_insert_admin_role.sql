-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
INSERT INTO
    IS601_Roles (
        id,
        name,
        description,
        is_active
    )
VALUES (-1, 'Admin', 'A super user', 1) ON DUPLICATE KEY
UPDATE name = name;

-- prevents this from failing after first insert