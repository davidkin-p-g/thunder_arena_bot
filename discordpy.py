import imp
import discord

def check_memeber_voice(user_to_event, client):
    # id канала
    id_event_voice_channel=user_to_event[0][9]
    channel = client.get_channel(id_event_voice_channel)
    members = channel.voice_states.keys()
    print(f'{members}')
    # Определяем не пришедгих участников
    missing_members = []
    for user in user_to_event:
        if user[0] not in  members:
            missing_members.append(user[0])
    # Завершаем работу бота
    return missing_members

