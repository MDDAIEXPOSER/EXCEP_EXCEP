"""
Пользователь вводит логин. Программа должна проверить все ли символы являются строчными. Если нет, выбросить ошибку.
Если ошибки не произошло писать фразу "Логин добавлен в базу". В не зависимости от того была ли ошибка должно печататься
"Я выучил исключения"
"""

def validate_login(login):
    for symbols in str(login):
        if type(symbols) == str:
            try:
                print('Login added')
                print('Исключил отсутствие исключений')
            except:
                print('Nope')

def main():
    validate_login(32423)
    validate_login('whiuwhfwlo')

if __name__ == "__main__":
    main()
