import random

def choice_mac(eats = 1):
    """今日食べるべきマックを選びます。
       
       いつもは頼まないメニューが食べたくなったら使ってね。
    """
    menu_list = ["ビックマック",
                 "チーズバーガー",
                 "フィレオフィッシュ",
                 ]
    
    for eat in range(1, eats):
        choice = random.choice(menu_list)
        print(str(eat) + ":" + choice + "!!!")

choice_mac(3)