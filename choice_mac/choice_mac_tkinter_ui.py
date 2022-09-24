# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import random
import menu

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("600x500")
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
        self.label = tk.Label(self.frame_right_main, text='メインはこれです！')
        self.label.pack()
        self.label = tk.Label(self.frame_right_side, text='サイドはこれです！')
        self.label.pack()
        self.label = tk.Label(self.frame_right_drink, text='ドリンクはこれです！')
        self.label.pack()

    #出力ボタン押下後の実行処理
    def input_handler(self):
    #メイン
        text = self.textbox_main_left.get()
        for main_num in range(int(text)):
            choice = random.choice(menu.main_list)
            main_number = str(main_num + 1)
            main_text = (f'main{main_number}: {choice}')
            message = tk.Message()
            message.pack(self.frame_right_main, side=tk.TOP)
            message['text'] = main_text


def main():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()