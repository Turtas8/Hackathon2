import json

FILE = 'users.json'

class RegisterMixin:
    def validate_password(self, password, password2):
        if len(password) < 0:
            raise ValueError('Пароль слишком короткий!')
        elif password.isdigit() or password.isalpha():
            raise ValueError('Пароль должен состоять из букв и цифр!')
        elif password != password2:
            raise ValueError('Пароли не совпали!')

    def register(self, username, password, password2):
        self.validate_password(password, password2)

        with open(FILE, 'r+') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                id = 1
                data = []

        # with open(FILE, 'w') as file:
            if data:
                is_username_used = any([x['username'] == username for x in data])
                if is_username_used:
                    json.dump(data, file)
                    raise ValueError('Такой username уже есть!')
            else:
                data.append({'id': id, 'username': username, 'password': password})
                json.dump(data, file)
                return {'status': 201, 'msg': 'Successfully registered!'}

class LoginMixin:
    def login(self, username, password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any([x['username'] == username for x in data])
            if not is_registered:
                raise Exception('Нет такого юзера!')
            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            if user_data['password'] != password:
                raise ValueError('Неверный пароль!')
            return {'status': 200, 'msg': 'Successfully logged in!', 'user': user_data['username']}

class User(RegisterMixin, LoginMixin):
    pass

user = User()
# print(user.register('JohnSnowNothing4567', 'qwerty1234', 'qwerty1234'))
# print(user.login('JohnSnowNothing4567', 'qwerty1234'))

# print(user.register('JohnSnowN234532454567', 'qerty1234', 'qerty1234'))
# print(user.login('JohnSnowN234532454567', 'qerty1234'))

print(user.register('JohnSnowN23453245456', 'qrerty1234', 'qrerty1234'))
print(user.login('JohnSnowN23453245456', 'qrerty1234'))

