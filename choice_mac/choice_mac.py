import random
import menu
import sys
mains = int(sys.argv[1])
sides = int(sys.argv[2])
drinks = int(sys.argv[3])
partition = "-" * 35

def choice_mac(mains, sides, drinks):
    """今日食べるべきマックを選びます。
       
       いつもは頼まないメニューが食べたくなったら使ってね。
    """
    #メインメニュー選択
    print(partition)
    print("メインはこちら。")
    for main in range(mains):
        choice = random.choice(menu.main_list)
        main_number = str(main + 1)
        print(f'main{main_number}: {choice}')
    print(partition)
    
    #サイドメニュー選択
    print("サイドはこちら。")
    for side in range(sides):
        choice = random.choice(menu.side_list)
        side_number = str(side + 1)
        print(f'side{side_number}: {choice}')
    print(partition)
    
    #ドリンクメニュー選択
    print("ドリンクはこちら。")
    for drink in range(drinks):
        choice = random.choice(menu.drink_list)
        drink_number = str(drink + 1)
        print(f'drink{drink_number}: {choice}')
    print(partition)

if __name__=='__main__':
    choice_mac(mains, sides, drinks)