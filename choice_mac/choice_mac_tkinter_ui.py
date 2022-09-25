# tkinter�̃C���|�[�g
import tkinter as tk
import tkinter.ttk as ttk
import random
import menu


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("750x500")
        self.master.title("�}�N�h�i���h�@�`���C�X�A�v��")
        #�A�C�R���ύX
        icon_path = 'hamburger.ico'
        self.master.iconbitmap(default=icon_path)

        #�t���[���쐬
        #�㕔�t���[��
        self.frame_top = tk.Frame(self.master, pady=5, padx=5, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(fill=tk.X)
        #���t���[��
        self.frame_left = tk.Frame(self.master, pady=5, padx=5, width=30, relief=tk.RAISED, borderwidth=1, bg="white")
        self.frame_left.pack(side=tk.LEFT, fill=tk.Y)
        #�E�t���[��
        self.frame_right_main = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_main.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_right_side = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_side.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_right_drink = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_drink.pack(side=tk.LEFT, fill=tk.Y)

        #�E�B�W�F�b�g�쐬
        self.create_widgets()

    def create_widgets(self):
        #�㕔�t���[���@�{�^��
        #���j���[�o�̓{�^��
        self.button1 = tk.Button(self.frame_top, text='�o��',
                                 command=self.input_handler)
        #�A�v���I���{�^��
        self.button2 = tk.Button(self.frame_top, text='�����ɍs��',
                    command=self.master.destroy)
        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.RIGHT)

        # ���t���[���@���̓e�L�X�g�{�b�N�X
        self.label__top_left = tk.Label(self.frame_left,text = '���������ďo�͂������Ă�', bg="white")
        self.label__main_left = tk.Label(self.frame_left,text = '�`���C���`', bg="white")
        self.label__side_left = tk.Label(self.frame_left,text = '�`�T�C�h�`', bg="white")
        self.label__drink_left = tk.Label(self.frame_left,text = '�`�h�����N�`', bg="white")

        self.textbox_main_left = tk.Entry(self.frame_left, width=20, relief=tk.RAISED, bd=2)
        self.textbox_side_left = tk.Entry(self.frame_left, width=20, relief=tk.RAISED, bd=2)
        self.textbox_drink_left = tk.Entry(self.frame_left, width=20, relief=tk.RAISED, bd=2)


        self.label__top_left.pack(pady=5, padx=5)
        self.label__main_left.pack(padx=5)
        self.textbox_main_left.pack()

        self.label__side_left.pack(padx=5)
        self.textbox_side_left.pack()

        self.label__drink_left.pack(padx=5)
        self.textbox_drink_left.pack()

        # �E�t���[���@�o�̓e�L�X�g�{�b�N�X
        self.label_main = tk.Label(self.frame_right_main, width=25, text='���C���͂���ł��I')
        self.label_main.pack(side=tk.TOP)
        self.label_side = tk.Label(self.frame_right_side, width=25, text='�T�C�h�͂���ł��I')
        self.label_side.pack(side=tk.TOP)
        self.label_drink = tk.Label(self.frame_right_drink, width=25, text='�h�����N�͂���ł��I')
        self.label_drink.pack(side=tk.TOP)

    # def choice_exec(self, menu_type):
    #         #���͒l�擾
    #     full_menu_lsit = {"main":int(self.textbox_main_left.get()),
    #                       "side":int(self.textbox_side_left.get()),
    #                       "drink":int(self.textbox_drink_left.get())}
    #     for menu_num in range(full_menu_lsit[f'{menu_type}']):
    #         choice = random.choice(f'menu.{menu_type}_list')
    #         menu_number = str(menu_num + 1)
    #         menu_answer = (f'{menu_type}{menu_number}: {choice}')
    #         if menu_type == 'main':
    #             self.menu_message = tk.Message(self.frame_right_main)
    #         elif menu_type == 'side':
    #             self.menu_message = tk.Message(self.frame_right_side)
    #         elif menu_type == 'drink':
    #             self.menu_message = tk.Message(self.frame_right_drink)
    #         self.menu_message.pack(side=tk.TOP)
    #         self.menu_message['text'] = menu_answer


    #�o�̓{�^��������̎��s����
    def input_handler(self):
    #���͒l�擾
        self.full_menu_lsit = {"main":int(self.textbox_main_left.get()),
                          "side":int(self.textbox_side_left.get()),
                          "drink":int(self.textbox_drink_left.get())}
        def choice_exec(self, menu_type):
            #���͒l�擾
            self.full_menu_lsit = {"main":int(self.textbox_main_left.get()),
                          "side":int(self.textbox_side_left.get()),
                          "drink":int(self.textbox_drink_left.get())}

            for menu_num in range(self.full_menu_lsit[f'{menu_type}']):
                choice = random.choice(f'menu.{menu_type}_list')
                menu_number = str(menu_num + 1)
                menu_answer = (f'{menu_type}{menu_number}: {choice}')
            if menu_type == 'main':
                self.menu_message = tk.Message(self.frame_right_main)
            elif menu_type == 'side':
                self.menu_message = tk.Message(self.frame_right_side)
            elif menu_type == 'drink':
                self.menu_message = tk.Message(self.frame_right_drink)
            self.menu_message.pack(side=tk.TOP)
            self.menu_message['text'] = menu_answer

        #�o�͓��e�쐬
            for num in self.full_menu_lsit:
                if num == "main":
                    choice_exec(self.full_menu_lsit['main'])
                elif num == "side":
                    choice_exec(self.full_menu_lsit['side'])
                elif num == "drink":
                    choice_exec(self.full_menu_lsit['drink'])

            # elif num == int_list[1]:
            #     for menu_num in range(num):
            #         choice = random.choice(menu.side_list)
            #         menu_number = str(menu_num + 1)
            #         menu_answer = (f'side{menu_number}: {choice}')
            #         self.menu_message = tk.Message(self.frame_right_side)
            #         self.menu_message.pack(side=tk.TOP)
            #         self.menu_message['text'] = menu_answer
            # elif num == int_list[2]:
            #     for menu_num in range(num):
            #         choice = random.choice(menu.drink_list)
            #         menu_number = str(menu_num + 1)
            #         menu_answer = (f'drink{menu_number}: {choice}')
            #         self.menu_message = tk.Message(self.frame_right_drink)
            #         self.menu_message.pack(side=tk.TOP)
            #         self.menu_message['text'] = menu_answer



        # main_text = self.textbox_main_left.get()
        # for main_num in range(int(main_text)):
        #     choice = random.choice(menu.main_list)
        #     main_number = str(main_num + 1)
        #     main_answer = (f'main{main_number}: {choice}')
        #     self.main_message = tk.Message(self.frame_right_main)
        #     self.main_message.pack(side=tk.TOP)
        #     self.main_message['text'] = main_answer

        #     #�T�C�h
        # side_text = self.textbox_side_left.get()
        # for side_num in range(int(side_text)):
        #     choice = random.choice(menu.side_list)
        #     side_number = str(side_num + 1)
        #     side_answer = (f'side{side_number}: {choice}')
        #     self.side_message = tk.Message(self.frame_right_side)
        #     self.side_message.pack(side=tk.TOP)
        #     self.side_message['text'] = side_answer

        #     #�h�����N
        # drink_text = self.textbox_drink_left.get()
        # for drink_num in range(int(drink_text)):
        #     choice = random.choice(menu.drink_list)
        #     drink_number = str(drink_num + 1)
        #     drink_answer = (f'drink{drink_number}: {choice}')
        #     self.drink_message = tk.Message(self.frame_right_drink)
        #     self.drink_message.pack(side=tk.TOP)
        #     self.drink_message['text'] = drink_answer

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
