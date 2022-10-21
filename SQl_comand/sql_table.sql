CREATE TABLE users
(
	id bigint primary key,
    user_name varchar(100) not null,
    rating varchar(20) not null,
    rating_value int not null,
    role_1 varchar(10) not null,
    role_2 varchar(10) not null,
    role_3 varchar(10) not null,
    role_4 varchar(10) not null,
    role_5 varchar(10) not null,
    ban bool default(0),
    discord_name varchar(100) not null
    
);
-- status: 1 - запущен Идет регистрация 2-  Регистрация закончена начинаются игры 0 - Событие завершено 4 - проверка пользователей в канаде перед началом
CREATE TABLE events
(
	id bigint primary key,
    date_add datetime,
    date_start datetime,
    type varchar(20),
    event_name varchar(100),
    event_description varchar(5000),
    status int,
    id_event_role bigint,
    id_event_text_channel bigint,
    id_event_voice_channel bigint,
    id_event_category_channel bigint,
    id_role_team_arr varchar(5000),
    id_channel_team_arr varchar(5000)
    
);

CREATE TABLE event_to_users
(
	id int primary key  auto_increment,
    id_user bigint not null,
    id_event bigint not null,
    team varchar(100),
    role varchar(10),
    reserve bool default(0),
    foreign key (id_user) references users(id),
    foreign key (id_event) references events(id)
    
);

CREATE TABLE error_mes
(
	id int primary key  auto_increment,
    id_user bigint not null,
    channel varchar(200) not null,
    member varchar(200) not null,
    command varchar(200) not null,
    error varchar(200) not null,
    date_ad datetime 
    
);