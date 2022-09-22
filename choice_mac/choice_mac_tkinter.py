import tkinter
import random
import menu

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=400, height=400,
                         borderwidth=1, relief='groove', cursor="dot")
        self.root = root
        self.pack(side=tkinter.TOP)
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        #ラベル
        label = tkinter.Label(self)
        label['text'] = '～あなたが食べるべきハンバーガーを選択します～'
        label.pack(side=tkinter.TOP)

        label = tkinter.Label(self)
        label['text'] = '↓のボックスに食べたい数を入力して、出力ボタンを押してね'
        label.pack(side=tkinter.TOP)

        #閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '買いに行く'
        quit_btn['command'] = self.root.destroy
        quit_btn.pack(side=tkinter.BOTTOM)

        #テキストボックス
        self.text_box = tkinter.Entry(self)
        self.text_box['width'] = 10
        self.text_box.pack(side=tkinter.TOP)

                #出力ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '出力'
        submit_btn['command'] = self.input_handler
        submit_btn.pack(side=tkinter.TOP)


    #メニュー選択実行処理
    def input_handler(self):
        text = self.text_box.get()

        for main_num in range(int(text)):
            choice = random.choice(menu.main_list)
            main_number = str(main_num + 1)
            main = (f'main{main_number}: {choice}')
            self.message = tkinter.Message(self)
            self.message.pack(side=tkinter.LEFT)
            self.message['text'] = main

root = tkinter.Tk()
root.geometry('600x500')
# root.attributes('-fullscreen', True)
root.title('マクドナルド　チョイスアプリ')
app = Application(root=root)
app.mainloop()