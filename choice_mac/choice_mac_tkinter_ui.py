# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
import random
import menu

# rootメインウィンドウの設定
root = tk.Tk()
root.title("マクドナルド　チョイスアプリ")
root.geometry("600x400")

#上部カラム(ラベル)
frame_top = tk.Frame(root, pady=5, padx=5, relief=tk.RAISED, bd=2)
frame_top.pack(fill=tk.X)

button1 = tk.Button(frame_top, text='出力')
                    # command=input_handler())

button2 = tk.Button(frame_top, text='買いに行く',
                    command=root.destroy)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)



# 左カラム(入力テキストボックス)
frame_left = tk.Frame(root, pady=5, padx=5, relief=tk.RAISED, bd=1, bg="white")
label__top_left = tk.Label(frame_left,text = '<<↓に数字を入れて出力を押してね>>', bg="white")
label__main_left = tk.Label(frame_left,text = '～メイン～', bg="white")
label__side_left = tk.Label(frame_left,text = '～サイド～', bg="white")
label__drink_left = tk.Label(frame_left,text = '～ドリンク～', bg="white")

textbox_main_left = tk.Entry(frame_left, width=30, relief=tk.RAISED, bd=2)
textbox_side_left = tk.Entry(frame_left, width=30, relief=tk.RAISED, bd=2)
textbox_drink_left = tk.Entry(frame_left, width=30, relief=tk.RAISED, bd=2)

frame_left.pack(side=tk.LEFT, fill=tk.Y)
label__top_left.pack(pady=5, padx=5)

label__main_left.pack(padx=5)
textbox_main_left.pack()

label__side_left.pack(padx=5)
textbox_side_left.pack()

label__drink_left.pack(padx=5)
textbox_drink_left.pack()

# 右カラム(出力テキストボックス)
frame_right1 = tk.Frame(root, pady=5, padx=5, relief=tk.RIDGE, bd=1)
label = tk.Label(frame_right1, text='メインはこれです！')
frame_right1.pack(side=tk.LEFT, fill=tk.Y)
label.pack()

frame_right2 = tk.Frame(root, pady=5, padx=5, relief=tk.RIDGE, bd=1)
label = tk.Label(frame_right2, text='サイドはこれです！')
frame_right2.pack(side=tk.LEFT, fill=tk.Y)
label.pack()

frame_right3 = tk.Frame(root, pady=5, padx=5, relief=tk.RIDGE, bd=1)
label = tk.Label(frame_right3, text='ドリンクはこれです！')
frame_right3.pack(side=tk.LEFT, fill=tk.Y)
label.pack()

#出力ボタン押下後の実行処理
def input_handler():
    #メイン
    text = textbox_main_left.get()
    for main_num in range(int(text)):
        choice = random.choice(menu.main_list)
        main_number = str(main_num + 1)
        main_text = (f'main{main_number}: {choice}')
        message = tk.Message()
        message.pack(frame_right1, side=tk.TOP)
        message['text'] = main_text


root.mainloop()