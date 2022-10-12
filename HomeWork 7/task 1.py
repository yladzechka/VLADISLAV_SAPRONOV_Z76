s = "Hello World"
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print("!" + second_word + ' ! ' + first_word + "!")  #Первый способ форматирования
print(f"!{second_word} ! {first_word}!")   #Второй способ
print("!{} ! {}!".format(second_word, first_word))   #Третий способ