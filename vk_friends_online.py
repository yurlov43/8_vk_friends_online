import getpass
import vk


APP_ID = 6298275


def get_user_login():
    return input('Введите логин: ')


def get_user_password():
    return getpass.getpass('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        scope='friends',
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    ids_friends_online = api.friends.getOnline(online_mobile=1)
    friends_online = []
    if ids_friends_online['online']:
        friends_online += api.users.get(
            user_ids=ids_friends_online['online'])
    if ids_friends_online['online_mobile']:
        friends_online += api.users.get(
            user_ids=ids_friends_online['online_mobile'])
    return friends_online


def output_friends_to_console(friends_online):
    print('Друзья online:')
    for number, friend in enumerate(friends_online, start=1):
        print('{}{}. {} {}'.format(
            '\t', number, friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
