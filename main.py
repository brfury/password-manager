from tkinter import *
import generate
from tkinter import messagebox
import random
import json



root = Tk()


class Root:

    def __init__(self):
        # atributos ui interface
        self.password_entry = Entry(width=21)
        self.email_user_entry = Entry(width=35)
        self.website_entry = Entry(width=21)

        # janela de imagem
        self.canvas = Canvas(width=200, height=195, highlightthickness=0)

        # proporções e características da tela
        self.root = root
        self.root.title('jdhf')
        self.root.geometry('500x400')
        self.root.config(pady=50, padx=50)
        self.root.resizable(False, False)

        # arquivo da imagem principal
        self.image = PhotoImage(file='logo.png')

        # chamada dos metodos
        self.canvas_image()
        self.create_web_entry()
        self.create_email_entry()
        self.create_pass_entry()
        self.create_labels()
        self.butons()
        self.root.mainloop()

    def canvas_image(self):
        '''
        metodo canvas gera um espaço para nossa img que deve ser centralizado,
        como nossa imagem tem 200x200, peamos 1/2 de x e 1/2
        '''
        self.canvas.create_image(100, 100, image=self.image)
        self.canvas.grid(column=1, row=0)

    def create_web_entry(self):
        self.website_entry.place(x=97, y=198)
        self.website_entry.focus()

    def create_email_entry(self):
        self.email_user_entry.grid(row=2, column=1, columnspan=2)

    def create_pass_entry(self):
        self.password_entry.place(x=97, y=240)

    def create_labels(self):
        self.website_text = Label(text='website', font=('gotham', 10))
        self.email_user_label = Label(text='email/user: ', font=('gotham', 10), background='#36454f')
        self.email_user_label.grid(column=0, row=2)
        self.password_label = Label(text='password ', font=('gotham', 10), background='#36454f')
        self.password_label.grid(column=0, row=3)
        self.website_text.grid(column=0, row=1)

    def generate_pass(self):
        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
            'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z'
        ]

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        letters_random = [random.choice(letters) for _ in range(random.randint(4, 10))]
        symbols_random = [random.choice(symbols) for _ in range(random.randint(2, 6))]
        numbers_random = [random.choice(numbers) for _ in range(random.randint(1, 4))]

        random_password = letters_random + symbols_random + numbers_random
        random.shuffle(random_password)
        password = ''.join(random_password)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def save(self):
        website = self.website_entry.get()
        email = self.email_user_entry.get()
        password = self.password_entry.get()

        new_dirc = {
            website: {
                'email': email,
                'password': password
            }
        }
        if len(email) == 0 or len(password) == 0:
            messagebox.showerror(title='Oops', message='os campos email/user e password podem estar vazios 😬')
        else:
            is_ok = messagebox.askyesno(
                message=f'website: {website}\n email:{email}\n senha:{password}\n '
                        f'estão corretos ?'

            )

            if is_ok:
                try:
                    with open('data.json', 'r') as txt:
                        data = json.load(txt)

                except FileNotFoundError:
                    with open('data.json', 'w') as txt:
                        json.dump(new_dirc, txt, indent=4)

                else:
                    data.update(new_dirc)

                    with open('data.json', 'w') as txt:
                        json.dump(data, txt, indent=4)

                finally:
                    self.website_entry.delete(0, END)
                    self.email_user_entry.delete(0, END)
                    self.password_entry.delete(0, END)
                    self.website_entry.focus()

    def seach(self):
        with open('data.json', 'r') as data_file:
            data_entry = self.website_entry.get()

            data = json.load(data_file)

            self.website_entry.delete(0, END)

            try:
                self.website_entry.insert(0, data[data_entry]['password'])
            except KeyError:
                messagebox.showerror(title='não consta', message='verifique se esta escrito corretamente')

    def butons(self):

        search_button = Button(text='search', width=12, borderwidth=1, font=('gotham', 8), command=self.seach)
        search_button.place(x=232, y=197)

        generate_buton = Button(text='generete pass', borderwidth=1, command=self.generate_pass)
        generate_buton.place(x=230, y=240)

        add_buton = Button(text='add', width=36, borderwidth=1, command=self.save)
        add_buton.grid(row=4, column=1, columnspan=2)

    # ---------------------------- UI SETUP ------------------------------- #


rootw = Root()
