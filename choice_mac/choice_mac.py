import random
import menu
import sys
mains = int(sys.argv[1])
sides = int(sys.argv[2])
drinks = int(sys.argv[3])

def choice_mac(mains, sides, drinks):
    """今日食べるべきマックを選びます。
       
       いつもは頼まないメニューが食べたくなったら使ってね。
    """
    #メインメニュー選択
    print("----------------------------------")
    print("メインはこちら。")
    for main in range(mains):
        choice = random.choice(menu.main_list)
        main_number = main + 1
        print("main" + str(main_number) + ":  " + choice)
    print("----------------------------------")
    
    #サイドメニュー選択
    print("サイドはこちら。")
    for side in range(sides):
        choice = random.choice(menu.side_list)
        side_number = side + 1
        print("side" + str(side_number) + ":  " + choice)
    print("----------------------------------")
    
    #ドリンクメニュー選択
    print("ドリンクはこちら。")
    for drink in range(drinks):
        choice = random.choice(menu.drink_list)
        drink_number = drink + 1
        print("drink" + str(drink_number) + ":  " + choice)
    print("----------------------------------")

if __name__=='__main__':
    choice_mac(mains, sides, drinks)