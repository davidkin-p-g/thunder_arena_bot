-- ------------------------------------
-- ПОЛЬЗОВАТЕЛИ
-- ------------------------------------

DELIMITER //
CREATE PROCEDURE add_user (in id_user bigint, in user_name varchar(100), in rating varchar(20), in rating_value int,
in role_1 varchar(10), in role_2 varchar(10), in role_3 varchar(10), in role_4 varchar(10), in role_5 varchar(10))
LANGUAGE SQL 
DETERMINISTIC 
BEGIN 
	INSERT INTO users(id, user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5) 
	VALUES (id_user, user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5);
END//

-- Проверка
-- call add_user(178963010751168516, "Suglinca1", "Золото 4", 400, "бот", "мид", "топ", "лес", "сап")

DELIMITER //
CREATE PROCEDURE edit_user (id_user bigint , user_name varchar(100), rating varchar(20), rating_value int,
role_1 varchar(10), role_2 varchar(10), role_3 varchar(10), role_4 varchar(10), role_5 varchar(10), ban bool) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Изменение пользователя' 
BEGIN 
	UPDATE users
    SET user_name = user_name , rating = rating, rating_value = rating_value, role_1 = role_1, 
		 role_2 = role_2, role_3 = role_3, role_4 = role_4, role_5 = role_5, ban = ban
	WHERE id = id_user;
END//
-- Проверка
-- call edit_user(178963010751168512, "Suglinca", "Золото 2", 400, "бот", "мид", "топ", "лес", "сап")

DELIMITER //
CREATE PROCEDURE check_user (in id_user bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Поиск пользователя' 
BEGIN 
	SELECT *
    FROM users
    WHERE id = id_user;
END//

-- Проверка
-- call check_user(178963010751168512, 'asd')

DELIMITER //
CREATE PROCEDURE all_users () 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Все пользователи' 
BEGIN 
	SELECT *
    FROM users;
END//

-- Проверка
-- call all_users()

DELIMITER //
CREATE PROCEDURE ban_user () 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Забаненые пользователи' 
BEGIN 
	SELECT *
    FROM users
    WHERE ban = TRUE;
END//

-- Проверка
-- call ban_user()

-- ------------------------------------
-- СОБЫТИЯ
-- ------------------------------------

DELIMITER //
CREATE PROCEDURE add_event (id_event bigint, type varchar(20), event_name varchar(100), event_description varchar(5000),
 date_start datetime) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Добавление нового события' 
BEGIN 
	INSERT events (id, date_add, date_start, type, event_name, event_description, status) 
	VALUES (id_event, now(), date_start, type, event_name, event_description, 1);
END//

-- Проверка
-- call add_event(now(), "Головомойка", "Топ Турик", 2) fuuu

DELIMITER //
CREATE PROCEDURE edit_event (id_event bigint , date_start datetime, type varchar(20), event_name varchar(100),
status int) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Изменение события' 
BEGIN 
	UPDATE events
    SET date_start = date_start , type = type, event_name = event_name, status = status
	WHERE id = id_event;
END//
-- Проверка
-- call edit_event(1, now(), "Головомойка2", "Топ Турик", 1)

DELIMITER //
CREATE PROCEDURE check_event (id_event bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Поиск события' 
BEGIN 
	SELECT *
    FROM events
    WHERE id = id_event;
END//

-- Проверка
-- call check_event(1)

-- ------------------------------------
-- СОБЫТИЯ + ПОЛЬЗОВАТЕЛИ
-- ------------------------------------

DELIMITER //
CREATE PROCEDURE add_user_to_event (id_ev bigint, id_us bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Добавление пары событие + пользователь' 
BEGIN 
DECLARE count_check INT;         
SET count_check = (SELECT count(*) FROM event_to_users where id_event = id_ev and id_user = id_us);
	IF ( count_check != 0) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Уже зарегестрирован';
	END IF;
	INSERT event_to_users (id_event, id_user) 
	VALUES (id_ev, id_us);
END//

-- Проверка
-- call add_user_to_event(1, 178963010751168513)

DELIMITER //
CREATE PROCEDURE delete_user_to_event (id_ev bigint, id_us bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Удаление пары событие + пользователь' 
BEGIN 
DECLARE count_check INT;         
SET count_check = (SELECT count(*) FROM event_to_users where id_event = id_ev and id_user = id_us);
	IF ( count_check = 0) THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Еще не зарегестрирован';
	END IF;
	DELETE FROM event_to_users 
    WHERE id_event = id_ev and id_user = id_us;
END//

-- Проверка
-- call delete_user_to_event(1, 178963010751168512)

DELIMITER //
CREATE PROCEDURE check_user_to_event (id_ev bigint, id_us bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Проверка регистрации на событие пользователя' 
BEGIN         
SELECT * 
FROM event_to_users 
WHERE id_event = id_ev and id_user = id_us;
END//

-- Проверка
-- call check_user_to_event(1, 178963010751168512)


DELIMITER //
CREATE PROCEDURE all_user_to_event (id_ev bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Проверка всех регистрированных на событие пользователей' 
BEGIN         
SELECT * 
FROM event_to_users 
WHERE id_event = id_ev;
END//

-- Проверка
-- call all_user_to_event(1)

DELIMITER //
CREATE PROCEDURE add_error (in id_user bigint, in channel varchar(200), in member varchar(200),
in command varchar(200),  in error varchar(200))
LANGUAGE SQL 
DETERMINISTIC 
BEGIN 
	INSERT INTO error_mes(id_user, channel, member, command, error) 
	VALUES (id_user, channel, member, command, error);
END//
