import random
import PySimpleGUI as sg

class Passgen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(15, 1)), sg.Input(key='site', size=(30, 1))],
            [sg.Text('Email/Usuário', size=(15, 1)), sg.Input(key='usuario', size=(30, 1))],
            [sg.Text('Quantidade de caracteres', size=(20, 1)), 
             sg.Combo(values=list(range(1, 31)), key='total_chars', default_value=8, size=(5, 1))],
            [sg.Multiline(size=(50, 10), key='output', disabled=True, autoscroll=True)],  # Aumenta o terminal
            [sg.Button('Gerar Senha', size=(15, 1)), sg.Button('Limpar Terminal', size=(15, 1))]
        ]
        self.window = sg.Window('Gerador de Senhas', layout)

    def Create(self):
        while True:
            evento, values = self.window.read()
            if evento == sg.WIN_CLOSED:
                break
            if evento == 'Gerar Senha':
                new_password = self.create_password(values)
                self.window['output'].print(new_password)
                self.save_password(new_password, values)
            if evento == 'Limpar Terminal':
                self.window['output'].update('')

    def create_password(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
        new_pass = ''.join(random.choices(char_list, k=int(values['total_chars'])))
        return new_pass

    def save_password(self, new_password, values):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"Site: {values['site']}, Usuário: {values['usuario']}, Nova Senha: {new_password}\n")
            self.window['output'].print('Arquivo salvo com sucesso!')

# Executa o gerador de senhas
gen = Passgen()
gen.Create()
