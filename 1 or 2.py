while True:
    a = int(input("Яку дію потрібно зробити\n(1 - Слова із вашого текста в алфавітному порядку, 2 - Список кількості кожної букви в вашому тексті): "))

    if a == 1:
        text = input("Введіть текст: ")
        words = text.split()
        words = [word.lower() for word in words if word.isalpha() and len(word) >= 3]
        sorted_words = sorted(words)
        unique_words = list(set(sorted_words))
        print("Слова із вашого текста:")
        for word in unique_words:
            print(word)

    elif a == 2:
        text = input("Введіть текст: ")
        dic = {}
        e = 0 
        for i in text:
            if i.isalpha():
                i = i.upper()
                dic[i] = dic.get(i, 0) + 1
                e += 1
        print("Кількість кожної букви в тексті:")
        for letter, count in dic.items():
            print(f"{letter}: {count}")
        print(f"Загальна кількість букв у тексті: {e}")

    else:
        print("Неправильний ввід даних")
    c = int(input("Ще раз? (1 - Так, 2 - Ні): "))
    if c == 2:
        break
    else:
        continue