from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from collections import Counter

ruAlphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
enAlphabet = "abcdefghijklmnopqrstuvwxyz"

ruFreq = {'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.70, 'д': 2.98, 'е': 8.45, 'ё': 0.04, 'ж': 0.94, 'з': 1.65, 'и': 7.35,
           'й': 1.21, 'к': 3.49, 'л': 4.40, 'м': 3.21, 'н': 6.70, 'о': 10.97, 'п': 2.81, 'р': 4.73, 'с': 5.47,
           'т': 6.26, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48, 'ч': 1.44, 'ш': 0.73, 'щ': 0.36, 'ъ': 0.04, 'ы': 1.90,
           'ь': 1.74, 'э': 0.32, 'ю': 0.64, 'я': 2.01}
enFreq = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97,
           'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33,
           't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07}

"""ПРОВЕРКА НА ПРИНАДЛЕЖНОСТЬ ВСЕХ БУКВ СООБЩЕНИЯ АЛФАВИТУ"""
def alphabetFind(alphabet, string):
    for i in string:
        if i.isalpha():
            if i not in alphabet:
                return False
    return True

"""ФОРМАТИРОВАНИЕ СООБЩЕНИЯ"""
def format(mes):
    res = ""
    mes = mes.lower()
    for i in mes:
        if i.isalpha():
            res += i
    return res

"""РАЗДЕЛЕНИЕ СООБЩЕНИЯ НА N СТРОК"""
def split(mes, n):
    arr = []
    for i in range(n):
        arr.append(mes[i:len(mes):n])
    return arr

"""ФОРМУЛА ИНДЕКС СОВПАДЕНИЯ"""
def ic(mes, alphabet):
    sum = 0
    for i in range(len(alphabet)):
        sum += (mes.count(alphabet[i])*(mes.count(alphabet[i]) - 1))/(len(mes)*(len(mes) - 1))
    return sum

"""ПОИСК ДЛИНЫ КЛЮЧА"""
def find_key_len(mes, alphabet):
    mes = format(mes)
    array = []
    for i in range(1, 10):
        arr = split(mes, i)
        average_sum = 0
        for j in arr:
            f = ic(j, alphabet)
            average_sum += f
        array.append(average_sum/(len(arr)))
    return array.index(max(array)) + 1

"""ФУНКЦИИ ДЛЯ ЧАСТОТНОГО АНАЛИЗА"""
def decrypt(mes, key, alphabet):
    output = ""
    for k in mes:
        if not k.isalpha():
            output += k
            continue
        index = alphabet.index(k.lower())
        c = alphabet[index - key % (len(alphabet) - 1)]
        output += c
    return output

def difference(t, alphabet, freq):
    counter = Counter(t)
    return sum([abs(counter.get(letter, 0) * 100 / len(t) - freq[letter]) for letter in alphabet])

def break_cipher(mes, alphabet, freq): #индекс наименьшей разницы
    a = [difference(decrypt(mes, x, alphabet), alphabet, freq) for x in range(1, len(alphabet))]
    return a.index(min(a)) + 1

"""САМЫЙ ПОПУЛЯРНЫЙ ЭЛЕМЕНТ В СЛОВАРЕ"""
def popular(freq, alphabet):
    return alphabet.index(max(freq, key=freq.get))

"""РАБОТА СО СЛОВОМ"""
def word(mes, alphabet, freq):
    mes = format(mes)
    len_key = find_key_len(mes, alphabet)
    arr = split(mes, len_key)
    res = ""
    for str in arr:
        key = break_cipher(str, alphabet, freq)
        res += alphabet[key]
    return res

"""РАСШИФРОВКА ВИЖЕНЕРА"""
def decode(message, key, alphabet):
    message = format(message)
    result = ""
    key_indexes = []
    for x in key:
        key_indexes.append(alphabet.find(x))
    i = 0
    for x in message:
        if i == len(key_indexes):
            i = 0
        index = alphabet.find(x) - key_indexes[i]
        if index < 0:
            index += len(alphabet)
        result += alphabet[index]
        i += 1
    return result

def click_on_buttonDecrypt():
    mes = message.get(1.0, END).lower()
    messageDecrypt.delete(1.0, END)

    if alphabetFind(enFreq, mes):
        key = word(mes, enAlphabet, enFreq)
        labelKey['text'] = f"Ключ: {key}"
        messageDecrypt.insert(1.0, decode(mes, key, enAlphabet))
    elif alphabetFind(ruFreq, mes):
        key = word(mes, ruAlphabet, ruFreq)
        labelKey['text'] = f"Ключ: {key}"
        messageDecrypt.insert(1.0, decode(mes, key, ruAlphabet))
    else:
        messagebox.showwarning("Ошибка", "Сообщение должно быть на одном языке")

def insert_text():
    file_name = fd.askopenfilename()
    f = open(file_name, encoding="utf-8")
    s = f.read()
    message.insert(1.0, s)
    f.close()

def delete():
    message.delete(1.0, END)

if __name__ == '__main__':
    root = Tk()
    root.title("Взлом Виженера")
    root.geometry("360x355")

    message = Text(width=30, height=10)
    message['wrap'] = WORD
    message.place(x=10, y=10)

    label1 = Label()
    label1['text'] = " - сообщение"
    label1.place(x=260, y=50)

    buttonOpenFile = Button(text="Открыть файл")
    buttonOpenFile.config(command=insert_text)
    buttonOpenFile.place(x=260, y=80)

    buttonOpenFile = Button(text="Очистить")
    buttonOpenFile.config(command=delete)
    buttonOpenFile.place(x=260, y=120)

    labelKey = Label()
    labelKey.place(x=260, y=185)

    messageDecrypt = Text(width=30, height=10)
    messageDecrypt['wrap'] = WORD
    messageDecrypt.place(x=10, y=180)

    buttonDecrypt = Button(text="Расшифровать")
    buttonDecrypt.config(command=click_on_buttonDecrypt)
    buttonDecrypt.place(x=260, y=245)

    root.mainloop()
