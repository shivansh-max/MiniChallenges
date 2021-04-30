# IMPORTS
import tkinter as tk
import pickle

# Rootwindow
root = tk.Tk()
root.title('Password saver')
root.geometry('450x700')


# Function

def read_from_pickle(path):
    with open(path, 'rb') as file:
        try:
            while True:
                yield pickle.load(file)
        except EOFError:
            pass


def get_all_the_information(y):
    objects = []
    name = name_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()
    things_list = [name, user_name, password]
    pickle.dump(things_list, open('PasswordUsernamesThings.dat', mode='ab'))
    for item in read_from_pickle('PasswordUsernamesThings.dat'):
        label = tk.Label(root, text=repr(item), font=('comic sans ms', 15))
        label.place(x=70, y=y, height=30)
        y += 35


main_label = tk.Label(root, text='Add A Password', font=('comic sans ms', 15))
format_label = tk.Label(root, text='Format: Name : Username : Password').place(x=120, y=160)

# label
name_label = tk.Label(root, text='Name: ', font=('comic sans ms', 15))
user_name_label = tk.Label(root, text='User_name: ', font=('comic sans ms', 15))
password_label = tk.Label(root, text='Password: ', font=('comic sans ms', 15))

# entry
name_entry = tk.Entry(root, font=('comic sans ms', 15))
user_name_entry = tk.Entry(root, font=('comic sans ms', 15))
password_entry = tk.Entry(root, font=('comic sans ms', 15))

# Saving button
button = tk.Button(root, font=('comic sans ms', 15), text='Save Password',
                   command=lambda: get_all_the_information(y=175))

main_label.pack()

name_label.place(x=0, y=30)
user_name_label.place(x=0, y=60)
password_label.place(x=0, y=90)

name_entry.place(x=130, y=30)
user_name_entry.place(x=130, y=60)
password_entry.place(x=130, y=90)

button.place(x=140, y=135, height=30)

root.mainloop()
