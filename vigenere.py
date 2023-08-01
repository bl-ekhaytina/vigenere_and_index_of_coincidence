from tkinter import *
from tkinter import messagebox

ruAlphabet0 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789"
ruAlphabet1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
enAlphabet0 = "abcdefghijklmnopqrstuvwxyz0123456789"
enAlphabet1 = "abcdefghijklmnopqrstuvwxyz"

def encode(message, key):
    result = ""
    if language.get() == "eng":
        key_indexes = []
        for x in key:
            key_indexes.append(enAlphabet1.find(x))
        i = 0
        for x in message:
            if i == len(key_indexes):
                i = 0
            index = enAlphabet0.find(x) + key_indexes[i]
            if index > len(enAlphabet0) - 1:
                index = index - len(enAlphabet0)
            result += enAlphabet0[index]
            i += 1
    elif language.get() == "ru":
        key_indexes = []
        for x in key:
            key_indexes.append(ruAlphabet1.find(x))
        i = 0
        for x in message:
            if i == len(key_indexes):
                i = 0
            index = ruAlphabet0.find(x) + key_indexes[i]
            if index > len(ruAlphabet0) - 1:
                index -= len(ruAlphabet0)
            result += ruAlphabet0[index]
            i += 1
    return result

def decode(message, key):
    result = ""
    if language.get() == "eng":
        key_indexes = []
        for x in key:
            key_indexes.append(enAlphabet1.find(x))
        i = 0
        for x in message:
            if i == len(key_indexes):
                i = 0
            index = enAlphabet0.find(x) - key_indexes[i]
            if index < 0:
                index += len(enAlphabet0)
            result += enAlphabet0[index]
            i += 1
    elif language.get() == "ru":
        key_indexes = []
        for x in key:
            key_indexes.append(ruAlphabet1.find(x))
        i = 0
        for x in message:
            if i == len(key_indexes):
                i = 0
            index = ruAlphabet0.find(x) - key_indexes[i]
            if index < 0:
                index += len(ruAlphabet0)
            result += ruAlphabet0[index]
            i += 1
    return result

"""ПРИНАДЛЕЖНОСТЬ ВСЕХ БУКВ СТРОКИ АЛФАВИТУ"""
def alphabetFind(alphabet, string):
    for i in string:
        if i not in alphabet:
            return False
    return True

def click_on_buttonEncrypt():
    messageB = message.get(1.0, END)
    keyB = key.get(1.0, END)
    messageB = messageB.replace("\n", "")
    messageB = messageB.replace(" ", "")
    messageB.lower()
    keyB = keyB.replace("\n", "")
    keyB = keyB.replace(" ", "")
    keyB.lower()

    if language.get() == "eng":
        if messageB and keyB:
            if alphabetFind(enAlphabet0, messageB):
                if alphabetFind(enAlphabet1, keyB):
                    messageEncryptB = encode(messageB, keyB)
                    messageEncrypt.delete(1.0, END)
                    messageEncrypt.insert(1.0, messageEncryptB)
                else:
                    messagebox.showwarning("Ошибка", "Ошибка в ключe")
            else:
                messagebox.showwarning("Ошибка", "Ошибка в сообщении")
        else:
            messagebox.showwarning("Ошибка", "Пустое поле")
    elif language.get() == "ru":
        if messageB and keyB:
            if alphabetFind(ruAlphabet0, messageB):
                if alphabetFind(ruAlphabet1, keyB):
                    messageEncryptB = encode(messageB, keyB)
                    messageEncrypt.delete(1.0, END)
                    messageEncrypt.insert(1.0, messageEncryptB)
                else:
                    messagebox.showwarning("Ошибка", "Ошибка в ключe")
            else:
                messagebox.showwarning("Ошибка", "Ошибка в сообщении")
        else:
            messagebox.showwarning("Ошибка", "Пустое поле")

def click_on_buttonDecrypt():
    messageB = messageEncrypt.get(1.0, END)
    keyB = key.get(1.0, END)
    messageB = messageB.replace("\n", "")
    messageB = messageB.replace(" ", "")
    messageB.lower()
    keyB = keyB.replace("\n", "")
    keyB = keyB.replace(" ", "")
    keyB.lower()

    if language.get() == "eng":
        if messageB and keyB:
            if alphabetFind(enAlphabet0, messageB):
                if alphabetFind(enAlphabet1, keyB):
                    messageDecryptB = decode(messageB, keyB)
                    messageDecrypt.delete(1.0, END)
                    messageDecrypt.insert(1.0, messageDecryptB)
                else:
                    messagebox.showwarning("Ошибка", "Ошибка в ключe")
            else:
                messagebox.showwarning("Ошибка", "Ошибка в сообщении")
        else:
            messagebox.showwarning("Ошибка", "Пустое поле")
    elif language.get() == "ru":
        if messageB and keyB:
            if alphabetFind(ruAlphabet0, messageB):
                if alphabetFind(ruAlphabet1, keyB):
                    messageDecryptB = decode(messageB, keyB)
                    messageDecrypt.delete(1.0, END)
                    messageDecrypt.insert(1.0, messageDecryptB)
                else:
                    messagebox.showwarning("Ошибка", "Ошибка в ключe")
            else:
                messagebox.showwarning("Ошибка", "Ошибка в сообщении")
        else:
            messagebox.showwarning("Ошибка", "Пустое поле")

if __name__ == '__main__':
    root = Tk()
    root.title("Шифр Виженера")
    root.geometry("275x315")

    language = StringVar()
    language.set("eng")

    message = Text(width=20, height=5)
    message['wrap'] = WORD  # перенос свова целиком, а не по буквам
    message.place(x=10, y=10)

    key = Text(width=20, height=1)
    key.place(x=10, y=95)

    messageEncrypt = Text(width=20, height=5)
    messageEncrypt['wrap'] = WORD
    messageEncrypt.place(x=10, y=115)

    messageDecrypt = Text(width=20, height=5)
    messageDecrypt['wrap'] = WORD
    messageDecrypt.place(x=10, y=200)

    label1 = Label()
    label1['text'] = " - сообщение"
    label1.place(x=175, y=40)

    label2 = Label()
    label2['text'] = " - ключ"
    label2.place(x=175, y=92)

    buttonEncrypt = Button(text="Зашифровать")
    buttonEncrypt.config(command=click_on_buttonEncrypt)
    buttonEncrypt.place(x=175, y=145)

    buttonDecrypt = Button(text="Расшифровать")
    buttonDecrypt.config(command=click_on_buttonDecrypt)
    buttonDecrypt.place(x=175, y=230)

    button_language_ru = Radiobutton(text="ru", value="ru", variable=language)
    button_language_ru.place(x=45, y=285)
    button_language_eng = Radiobutton(text="eng", value="eng", variable=language)
    button_language_eng.place(x=100, y=285)

    root.mainloop()
