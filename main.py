import tkinter as tk

# Функция для шифрования текста
def vernam_encrypt():
    message = input_text.get()
    key = int(key_entry.get())
    encrypted_text = []
    for char in message:
        encrypted_char = chr(ord(char) ^ key)
        encrypted_text.append(encrypted_char)
    encrypted_text = ''.join(encrypted_text)
    encrypted_text_entry.delete(0, tk.END)
    encrypted_text_entry.insert(0, encrypted_text)

# Функция для дешифрования текста
def vernam_decrypt():
    encrypted_text = encrypted_text_entry.get()
    key = int(key_entry.get())
    decrypted_message = []
    for char in encrypted_text:
        decrypted_char = chr(ord(char) ^ key)
        decrypted_message.append(decrypted_char)
    decrypted_message = ''.join(decrypted_message)
    decrypted_text_entry.delete(0, tk.END)
    decrypted_text_entry.insert(0, decrypted_message)

# Создаем главное окно
app = tk.Tk()
app.title("Kalashnikov Lab#5")
app.geometry('1000x400')

label_text = tk.Label(text='Шифр Вернама',font=("Arial", 14),foreground='red')
label_text.pack()
# Создаем и размещаем виджеты на окне
input_label = tk.Label(app, text="Исходный текст:",font=("Arial", 11))
input_label.pack()

input_text = tk.Entry(app, width=40,font=("Arial", 11))
input_text.pack()

key_label = tk.Label(app, text="Ключ (1 байт):",font=("Arial", 11))
key_label.pack()

key_entry = tk.Entry(app,font=("Arial", 11))
key_entry.pack()

encrypt_button = tk.Button(app, text="Зашифровать", command=vernam_encrypt,font=("Arial", 11))
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Расшифровать", command=vernam_decrypt,font=("Arial", 11))
decrypt_button.pack()

encrypted_text_label = tk.Label(app, text="Зашифрованный текст:",font=("Arial", 11))
encrypted_text_label.pack()

encrypted_text_entry = tk.Entry(app, width=40,font=("Arial", 11))
encrypted_text_entry.pack()

decrypted_text_label = tk.Label(app, text="Расшифрованный текст:",font=("Arial", 11))
decrypted_text_label.pack()

decrypted_text_entry = tk.Entry(app, width=40,font=("Arial", 11))
decrypted_text_entry.pack()

# Запускаем главный цикл приложения
if __name__=='__main__':
    app.mainloop()
