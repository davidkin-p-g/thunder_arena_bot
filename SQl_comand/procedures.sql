-- ------------------------------------
-- ПОЛЬЗОВАТЕЛИ
-- ------------------------------------

DELIMITER //
CREATE PROCEDURE add_user (in id_user bigint, in user_name varchar(100), in rating varchar(20), in rating_value int,
in role_1 varchar(10), in role_2 varchar(10), in role_3 varchar(10), in role_4 varchar(10), in role_5 varchar(10),
in discord_name varchar(100))
LANGUAGE SQL 
DETERMINISTIC 
BEGIN 
	INSERT INTO users(id, user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, discord_name) 
	VALUES (id_user, user_name, rating, rating_value, role_1, role_2, role_3, role_4, role_5, discord_name);
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
CREATE PROCEDURE edit_user_discord_name (id_user bigint ,discord_name varchar(100)) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Изменение дискорд имени пользователя пользователя' 
BEGIN 
	UPDATE users
    SET discord_name = discord_name 
	WHERE id = id_user;
END//
-- Проверка
-- call edit_user(178963010751168512, "вап")

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
CREATE PROCEDURE check_user_to_me (in id_user bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'информация о пользователе' 
BEGIN 
	SELECT *,(DATE(e.date_start)-DATE(now()))*86400  + (HOUR(e.date_start)-HOUR(now()))*3600 + (MINUTE(e.date_start)-MINUTE(now()))*60 + (SECOND(e.date_start) - SECOND(now())) as sec
    FROM users as u
	left JOIN event_to_users as eu on eu.id_user = u.id
    left JOIN events as e on eu.id_event = e.id
    WHERE u.id = id_user
    Order by e.status DESC, sec;
END//

-- Проверка
-- call check_user_to_me(178963010751168512)

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
 date_start datetime, id_event_role bigint, id_event_text_channel bigint, id_event_voice_channel bigint, id_event_category_channel bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Добавление нового события' 
BEGIN 
	INSERT events (id, date_add, date_start, type, event_name, event_description, status, id_event_role, id_event_text_channel, id_event_voice_channel, id_event_category_channel) 
	VALUES (id_event, now(), date_start, type, event_name, event_description, 1, id_event_role, id_event_text_channel, id_event_voice_channel, id_event_category_channel);
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
-- call check_event(1009290709418909777)

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
CREATE PROCEDURE edit_reserve_user_to_event (id_us bigint, id_ev bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Отметка о посмещении в запас' 
BEGIN 
	UPDATE event_to_users
    SET reserve = 1
    WHERE id_user = id_us and id_event = id_ev;
END//

-- Проверка
-- нет

DELIMITER //
CREATE PROCEDURE edit_team_role_user_to_event (id_us bigint, id_ev bigint, team varchar(100), role varchar(10)) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Отметка о роли и команде' 
BEGIN 
	UPDATE event_to_users
    SET team = team, role = role
    WHERE id_user = id_us and id_event = id_ev;
END//

-- Проверка
-- нет

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
FROM event_to_users as eu 
JOIN users as u on eu.id_user = u.id
JOIN events as e on eu.id_event = e.id
WHERE id_event = id_ev;
END//

-- Проверка
-- call all_user_to_event(1009281495585800274)

DELIMITER //
CREATE PROCEDURE all_user_to_event_team (id_ev bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Проверка всех регистрированных на событие пользователей по командам' 
BEGIN         
SELECT * 
FROM event_to_users as eu 
JOIN users as u on eu.id_user = u.id
JOIN events as e on eu.id_event = e.id
WHERE id_event = id_ev
ORDER BY team;
END//

-- Проверка
-- call all_user_to_event_team(1009310514985324627)

DELIMITER //
CREATE PROCEDURE add_error (id_user bigint, channel varchar(200), member varchar(200), command varchar(200), error varchar(200))
LANGUAGE SQL 
DETERMINISTIC 
BEGIN 
	INSERT INTO error_mes(id_user, channel, member, command, error, date_ad) 
	VALUES (id_user, channel, member, command, error, NOW());
END//

DELIMITER //
CREATE PROCEDURE check_user_to_me_new (in id_user bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'информация о пользователе' 
BEGIN 
SELECT u.id, u.user_name, u.rating, u.rating_value, u.role_1, u.role_2, u.role_3, u.role_4, u.role_5, u.discord_name,
e.id, e.event_name, team, role, status,
(DATE(e.date_start)-DATE(now()))*86400  + (HOUR(e.date_start)-HOUR(now()))*3600 + (MINUTE(e.date_start)-MINUTE(now()))*60 + (SECOND(e.date_start) - SECOND(now())) as sec
FROM users as u
left JOIN event_to_users as eu on eu.id_user = u.id
left JOIN events as e on eu.id_event = e.id
WHERE u.id = id_user
Order by e.status DESC, sec;
END//

DELIMITER //
CREATE PROCEDURE all_user_to_event_new (id_ev bigint) 
LANGUAGE SQL 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Проверка всех регистрированных на событие пользователей' 
BEGIN         
SELECT u.id, e.event_name, u.user_name, u.rating, u.role_1, u.role_2, u.role_3, u.role_4, u.role_5, e.id_event_voice_channel
FROM event_to_users as eu 
JOIN users as u on eu.id_user = u.id
JOIN events as e on eu.id_event = e.id
WHERE id_event = id_ev;
END//

-- Проверка
-- call all_user_to_event(1009281495585800274)


DELIMITER //
CREATE PROCEDURE all_user_to_event_team_new (id_ev bigint) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Проверка всех регистрированных на событие пользователей по командам' 
BEGIN         
SELECT u.id, e.event_name, u.user_name, team, u.rating, u.rating_value, role
FROM event_to_users as eu 
JOIN users as u on eu.id_user = u.id
JOIN events as e on eu.id_event = e.id
WHERE id_event = id_ev
ORDER BY team;
END//

-- Проверка
-- call all_user_to_event_team(1009310514985324627)

DELIMITER //
CREATE PROCEDURE add_arr_id_to_event (id_event bigint , id_role_team_arr varchar(5000), id_channel_team_arr varchar(5000)) 
LANGUAGE SQL 
DETERMINISTIC 
SQL SECURITY DEFINER 
COMMENT 'Изменение события' 
BEGIN 
	UPDATE events
    SET id_role_team_arr = id_role_team_arr , id_channel_team_arr = id_channel_team_arr
	WHERE id = id_event;
END//
