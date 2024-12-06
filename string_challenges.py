# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1:])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowels = 'ауоиэыяюе'
count = 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

words = sentence.split()
for word in words:
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

words = sentence.split()
length = 0
for word in words:
    length += len(word)
print(length/len(words))