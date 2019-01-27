import vk_api, config
from vk_api.keyboard import VkKeyboard
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id


def main():

    vk_session = vk_api.VkApi(token=str(config.bot_token))
    vk = vk_session.get_api()

    long_poll = VkBotLongPoll(vk_session, int(config.group_id))

    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button(label="70 руб. Американо мал. / Чай", color="primary")
    keyboard.add_line()
    keyboard.add_button(label="80 руб. Американо средний", color="primary")
    keyboard.add_line()
    keyboard.add_button(label="99 руб. Все остальное", color="primary")

    vk.messages.send(
        peer_id=(str(config.chat_id)),
        keyboard=keyboard.get_keyboard(),
        random_id=get_random_id(),
        message='Привет, выбери стоимость заказа'
    )

    for event in long_poll.listen():
        if event:
            print(event)

        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object['peer_id'] and event.object['peer_id'] == str(config.chat_id):
                print('id{} : {}'.format(event.obj.from_id, event.obj.text), end='\n')


if __name__ == '__main__':
    print("Bot started")
    main()

