# -*- coding: utf-8 -*-

import interactions


# Кнокпи для события
button_participate_event = interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Участвовать",
    custom_id="participate_event",
)

button_participate_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Участвовать",
    custom_id="participate_event_disabled",
    disabled=True
)

button_participate_event_check= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Список участников",
    custom_id="participate_event_check",
)

button_participate_event_check_team= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Список Команд",
    custom_id="participate_event_check_team",
)

button_leave_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Уйти",
    custom_id="leave_event",
)

button_leave_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Уйти",
    custom_id="leave_event_disabled",
    disabled=True
)

button_start_dm_mess= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Рассылка",
    custom_id="start_dm_mess",
)

button_start_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Запустить",
    custom_id="start_event",
)

button_end_event= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Завершить",
    custom_id="end_event",
)
button_end_event_disabled= interactions.Button(
    style=interactions.ButtonStyle.SECONDARY,
    label="Завершено",
    custom_id="end_event_disabled",
    disabled=True
)


row = interactions.ActionRow(
    components=[button_participate_event, button_participate_event_check, button_leave_event, button_start_dm_mess]
)
row1 = interactions.ActionRow(
    components=[button_participate_event_disabled, button_participate_event_check_team, button_leave_event_disabled, button_end_event]
)
row2 = interactions.ActionRow(
    components=[button_participate_event_disabled, button_participate_event_check_team, button_leave_event_disabled, button_end_event_disabled]
)
row0_5 = interactions.ActionRow(
    components=[button_participate_event, button_participate_event_check, button_leave_event, button_start_event]
)