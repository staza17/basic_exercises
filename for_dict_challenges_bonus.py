"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": str(uuid.uuid4()),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


if __name__ == "__main__":
    generated_messages = generate_chat_history()
    print(generated_messages)

    users_id = []
    for message in generated_messages:
        users_id.append(message['sent_by'])
    users_id = list(dict.fromkeys(users_id))

    def count_largest(dictionary):
        largest = 0
        largest_item = 0
        for key, value in dictionary.items():
            if largest < value:
                largest = value
                largest_item = key
            elif largest == value:
                largest_item = f'{largest_item}, {key}'
        return largest_item

    def count_includes(info, key1, key2):
        object_count = {}
        if key2 == '':
            key2 = key1
        for object in info:
            count = 0
            searched_item = object[key1]
            for item in info:
                if searched_item == item[key2]:
                    count += 1
            object_count[object[key1]] = count
        return object_count

    def get_spammer_id(info):
        message_count = count_includes(info, 'sent_by', '')
        spammer_id = count_largest(message_count)
        return spammer_id

    def get_discussed_id(info):
        replies_count = {}
        for author in users_id:
            replies_count[author] = 0
        replied_messages = count_includes(info, 'id', 'reply_for')
        for key, value in replied_messages.items():
            for message in generated_messages:
                if key == message['id']:
                    author_id = message['sent_by']
                    replies_count[author_id] += value
        return count_largest(replies_count)

    def get_mostseen_id(info):
        messages_seen_by = {}
        for id in users_id:
            seen_by = []
            for message in info:
                if id == message['sent_by']:
                    for item in message['seen_by']:
                        seen_by.append(item)
            seen_by = list(set(seen_by))
            messages_seen_by[id] = len(seen_by)
        return count_largest(messages_seen_by)

    def get_popular_time(info):
        messages_time = {
            'утром': 0,
            'днем': 0,
            'вечером': 0
        }
        time_list12 = []
        time_list12_18 = []
        time_list18 = []
        for message in info:
            if int(message['sent_at'].strftime('%H')) < 12:
                time_list12.append(message['id'])
            elif 12 < int(message['sent_at'].strftime('%H')) <= 18:
                time_list12_18.append(message['id'])
            elif 18 < int(message['sent_at'].strftime('%H')):
                time_list18.append(message['id'])
        messages_time['утром'] = len(time_list12)
        messages_time['днем'] = len(time_list12_18)
        messages_time['вечером'] = len(time_list18)
        return count_largest(messages_time)

    def get_tred_id(info):
        messages_id = {}
        for message in info:
            count = 0
            id = message['id']
            search_id = id
            while True:
                for item in info:
                    if search_id == item['reply_for']:
                        count += 1
                        search_id = item['id']
                break
            messages_id[id] = count
        return count_largest(messages_id)

    print(f'Айди пользователя, который написал больше всех сообщений: {get_spammer_id(generated_messages)}')
    print(f'Айди пользователя, на сообщения которого больше всего отвечали: {get_discussed_id(generated_messages)}')
    print(f'Айди пользователей, сообщения которых видело больше всего уникальных пользователей: {get_mostseen_id(generated_messages)}')
    print(f'В чате больше всего сообщений: {get_popular_time(generated_messages)}')
    print(f'Идентификаторы сообщений, которые стали началом для самых длинных тредов (цепочек ответов): {get_tred_id(generated_messages)}')


