from main import *

for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text.lower()

            user_id = str(event.user_id)
            msg = event.text.lower()

            if request == 'start':
                creating_database()
                bot.write_msg(user_id, f'Приветствую! {bot.name(user_id)}')
                bot.find_user(user_id)
                bot.write_msg(event.user_id,
                              f'На основании данных, из вашего профиля, для вас подобрана пара! Далее для просмотра напишите "next"')

            elif request == 'next':
                for i in iteration:
                    offset += 1
                    bot.find_persons(user_id, offset)
                    break

            else:
                bot.write_msg(event.user_id, 'Введите "start", бот соберет базу, для просмотра ввести "next" ')
