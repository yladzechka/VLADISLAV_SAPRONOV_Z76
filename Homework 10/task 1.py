# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая выводит слово,
# имеющее максимальную длину (или список слов, если таковых несколько).


def longest_words(file):
    with open(file, encoding='utf-8') as text:
        item = text.read().split()
        max_length = len(max(item, key=len))
        check_words = [word for word in item if len(word) == max_length]
        return check_words


print(longest_words("article.txt"))


