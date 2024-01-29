import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Ошибка: Выберите хотя бы один тип символов для пароля.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Добро пожаловать в генератор паролей!")

    length = int(input("Введите длину пароля: "))
    use_uppercase = input(
        "Использовать буквы верхнего регистра? (y/n): ").lower() == 'y'
    use_lowercase = input(
        "Использовать буквы нижнего регистра? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special_chars = input(
        "Использовать специальные символы? (y/n): ").lower() == 'y'

    password = generate_password(
        length, use_uppercase, use_lowercase, use_digits, use_special_chars)

    if password:
        print("Ваш сгенерированный пароль: ", password)


if __name__ == "__main__":
    main()
# keke