first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']


first_result = (
    len(f_word) - len(s_word)
    for f_word, s_word in zip(first, second)
    if len(f_word) != len(s_word)
)


second_result = (
    len(first[i]) == len(second[i])
    for i in range(len(first))
)


print(list(first_result))
print(list(second_result))
