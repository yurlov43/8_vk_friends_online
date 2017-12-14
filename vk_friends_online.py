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
    return api.friends.getOnline(online_mobile=1)


def output_friends_to_console(friends_online):
    print('Друзья online с компьютера:')
    for friend in friends_online['online']:
        print(friend)
    print('Друзья online с телефона:')
    for friend in friends_online['online_mobile']:
        print(friend)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
