import tkinter as tk
import tkinter.ttk as ttk
import random
import menu


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("750x500")
        self.master.title("マクドナルド　チョイスアプリ")
        #アイコン変更
        icon_path = 'hamburger.ico'
        self.master.iconbitmap(default=icon_path)

        #フレーム作成
        #上部フレーム
        self.frame_top = tk.Frame(self.master, pady=5, padx=5, relief=tk.RAISED, borderwidth=1)
        self.frame_top.pack(fill=tk.X)
        #左フレーム
        self.frame_left = tk.Frame(self.master, pady=5, padx=5, width=30, relief=tk.RAISED, borderwidth=1, bg="white")
        self.frame_left.pack(side=tk.LEFT, fill=tk.Y)
        #右フレーム
        self.frame_right_main = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_main.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_right_side = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_side.pack(side=tk.LEFT, fill=tk.Y)
        self.frame_right_drink = tk.Frame(self.master, pady=5, padx=5, relief=tk.RIDGE, borderwidth=1)
        self.frame_right_drink.pack(side=tk.LEFT, fill=tk.Y)

        #ウィジェット作成
        self.create_widgets()

    def create_widgets(self):
        #上部フレーム　ボタン
        #メニュー出力ボタン
        self.button1 = tk.Button(self.frame_top, text='出力',
                                 command=self.input_handler)
        #アプリ終了ボタン
        self.button2 = tk.Button(self.frame_top, text='買いに行く',
                    command=self.master.destroy)
        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.RIGHT)

        # 左フレーム　入力テキストボックス
        self.label__top_left = tk.Label(self.frame_left,text = '数字を入れて出力を押してね', bg="white")
        self.label__main_left = tk.Label(self.frame_left,text = '～メイン～', bg="white")
        self.label__side_left = tk.Label(self.frame_left,text = '～サイド～', bg="white")
        self.label__drink_left = tk.Label(self.frame_left,text = '～ドリンク～', bg="white")

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

        # 右フレーム　出力テキストボックス
        self.label_main = tk.Label(self.frame_right_main, width=25, text='メインはこれです！')
        self.label_main.pack(side=tk.TOP)
        self.label_side = tk.Label(self.frame_right_side, width=25, text='サイドはこれです！')
        self.label_side.pack(side=tk.TOP)
        self.label_drink = tk.Label(self.frame_right_drink, width=25, text='ドリンクはこれです！')
        self.label_drink.pack(side=tk.TOP)

    #実行処理部分
    def input_handler(self):
        main_text = self.textbox_main_left.get()
        for main_num in range(int(main_text)):
            choice = random.choice(menu.main_list)
            main_number = str(main_num + 1)
            main_answer = (f'main{main_number}: {choice}')
            self.main_message = tk.Message(self.frame_right_main)
            self.main_message.pack(side=tk.TOP)
            self.main_message['text'] = main_answer

            #サイド
        side_text = self.textbox_side_left.get()
        for side_num in range(int(side_text)):
            choice = random.choice(menu.side_list)
            side_number = str(side_num + 1)
            side_answer = (f'side{side_number}: {choice}')
            self.side_message = tk.Message(self.frame_right_side)
            self.side_message.pack(side=tk.TOP)
            self.side_message['text'] = side_answer

            #ドリンク
        drink_text = self.textbox_drink_left.get()
        for drink_num in range(int(drink_text)):
            choice = random.choice(menu.drink_list)
            drink_number = str(drink_num + 1)
            drink_answer = (f'drink{drink_number}: {choice}')
            self.drink_message = tk.Message(self.frame_right_drink)
            self.drink_message.pack(side=tk.TOP)
            self.drink_message['text'] = drink_answer

def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()