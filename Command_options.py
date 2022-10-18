# -*- coding: utf-8 -*-

import interactions

# Отции необходимые командам для предоставления информации о себе
options_registration_new=[
        interactions.Option(
            name='user_name',
            description = 'Имя пользователя на RU сервере с которым вы будете учавствовать в соревнованиях',
            type=interactions.OptionType.STRING,
            required=True
        ),
         interactions.Option(
            name='role_1',
            description = 'Роль №1 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_2',
            description = 'Роль №2 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_3',
            description = 'Роль №3 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_4',
            description = 'Роль №4 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='role_5',
            description = 'Роль №5 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
         interactions.Option(
            name='rating',
            description = 'Ваш нынешний уровень игры.',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Железо 4", value="Железо 4:0"),
                interactions.Choice(name="Железо 3", value="Железо 3:100"),
                interactions.Choice(name="Железо 2", value="Железо 2:200"),
                interactions.Choice(name="Железо 1", value="Железо 1:300"),
                interactions.Choice(name="Бронза 4", value="Бронза 4:400"),
                interactions.Choice(name="Бронза 3", value="Бронза 3:500"),
                interactions.Choice(name="Бронза 2", value="Бронза 2:600"),
                interactions.Choice(name="Бронза 1", value="Бронза 1:700"),
                interactions.Choice(name="Серебро 4", value="Серебро 4:800"),
                interactions.Choice(name="Серебро 3", value="Серебро 3:900"),
                interactions.Choice(name="Серебро 2", value="Серебро 2:1000"),
                interactions.Choice(name="Серебро 1", value="Серебро 1:1100"),
                interactions.Choice(name="Золото 4", value="Золото 4:1200"),
                interactions.Choice(name="Золото 3", value="Золото 3:1300"),
                interactions.Choice(name="Золото 2", value="Золото 2:1400"),
                interactions.Choice(name="Золото 1", value="Золото 1:1500"),
                interactions.Choice(name="Платина 4", value="Платина 4:1600"),
                interactions.Choice(name="Платина 3", value="Платина 3:1700"),
                interactions.Choice(name="Платина 2", value="Платина 2:1800"),
                interactions.Choice(name="Платина 1", value="Платина 1:1900"),
                interactions.Choice(name="Алмаз 4", value="Алмаз 4:2000"),
                interactions.Choice(name="Алмаз 3", value="Алмаз 3:2100"),
                interactions.Choice(name="Алмаз 2", value="Алмаз 2:2200"),
                interactions.Choice(name="Алмаз 1", value="Алмаз 1:2300"),
                interactions.Choice(name="Мастер+", value="Мастер+:2500"),
                ]
        )
    ]

options_rename=[
        interactions.Option(
            name='user_name',
            description = 'Новое имя пользователя на RU сервере с которым вы будете учавствовать в соревнованиях',
            type=interactions.OptionType.STRING,
            required=True
        ),
    ]

options_rating=[
        interactions.Option(
            name='rating',
            description = 'Ваш нынешний уровень игры.',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Железо 4", value="Железо 4:0"),
                interactions.Choice(name="Железо 3", value="Железо 3:100"),
                interactions.Choice(name="Железо 2", value="Железо 2:200"),
                interactions.Choice(name="Железо 1", value="Железо 1:300"),
                interactions.Choice(name="Бронза 4", value="Бронза 4:400"),
                interactions.Choice(name="Бронза 3", value="Бронза 3:500"),
                interactions.Choice(name="Бронза 2", value="Бронза 2:600"),
                interactions.Choice(name="Бронза 1", value="Бронза 1:700"),
                interactions.Choice(name="Серебро 4", value="Серебро 4:800"),
                interactions.Choice(name="Серебро 3", value="Серебро 3:900"),
                interactions.Choice(name="Серебро 2", value="Серебро 2:1000"),
                interactions.Choice(name="Серебро 1", value="Серебро 1:1100"),
                interactions.Choice(name="Золото 4", value="Золото 4:1200"),
                interactions.Choice(name="Золото 3", value="Золото 3:1300"),
                interactions.Choice(name="Золото 2", value="Золото 2:1400"),
                interactions.Choice(name="Золото 1", value="Золото 1:1500"),
                interactions.Choice(name="Платина 4", value="Платина 4:1600"),
                interactions.Choice(name="Платина 3", value="Платина 3:1700"),
                interactions.Choice(name="Платина 2", value="Платина 2:1800"),
                interactions.Choice(name="Платина 1", value="Платина 1:1900"),
                interactions.Choice(name="Алмаз 4", value="Алмаз 4:2000"),
                interactions.Choice(name="Алмаз 3", value="Алмаз 3:2100"),
                interactions.Choice(name="Алмаз 2", value="Алмаз 2:2200"),
                interactions.Choice(name="Алмаз 1", value="Алмаз 1:2300"),
                interactions.Choice(name="Мастер+", value="Мастер+:2500"),
                ]
        )
    ]

options_rerole=[
        interactions.Option(
            name='role_1',
            description = 'Роль №1 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
            interactions.Option(
            name='role_2',
            description = 'Роль №2 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
            interactions.Option(
            name='role_3',
            description = 'Роль №3 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
            interactions.Option(
            name='role_4',
            description = 'Роль №4 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
            interactions.Option(
            name='role_5',
            description = 'Роль №5 в списке ролей от самой желанной до самой нежеланной',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name="Верхняя Линия", value="Топ"),
                interactions.Choice(name="Лес", value="Лес"),
                interactions.Choice(name="Средняя Линия", value="Мид"),
                interactions.Choice(name="Нижняя линия", value="Бот"),
                interactions.Choice(name="Поддержка", value="Саппорт"),
            ]
        ),
    ]

options_start_event=[
    interactions.Option(
        name='event_type',
        description = 'Тип события',
        type=interactions.OptionType.STRING,
        required=True,
        choices=[
            interactions.Choice(name="Потасовка", value="Потасовка"),
            interactions.Choice(name="Командный", value="Командный"),
        ]
    ),
    interactions.Option(
            name='event_name',
            description = 'Название события',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name='event_description',
            description = 'Описание события',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name='event_date_start',
            description = 'Время старта события. Формат времени: YYYY-MM-DD hh:mm:ss',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]