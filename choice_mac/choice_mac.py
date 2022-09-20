import random
import menu

while True:
    try:
        mains = int(input("1,メイン数を入れてください： "))
        sides = int(input("2,サイドの数を入れてください： "))
        drinks = int(input("3,ドリンクの数を入れてください： "))
        print("\n")
        partition = "-" * 35
        break
    except ValueError:
        print("残念ながら、これは有効な数字ではありません....。どうぞ最初からもう一度。")

def choice_mac(mains, sides, drinks):
    """今日食べるべきマックを選びます。
       
       いつもは頼まないメニューが食べたくなったら使ってね。
    """
    #メインメニュー選択
    print(partition)
    print("メインメニューはこちら。")
    for main in range(mains):
        choice = random.choice(menu.main_list)
        main_number = str(main + 1)
        print(f'main{main_number}: {choice}')
    print(partition)
    
    #サイドメニュー選択
    print("サイドメニューはこちら。")
    for side in range(sides):
        choice = random.choice(menu.side_list)
        side_number = str(side + 1)
        print(f'side{side_number}: {choice}')
    print(partition)
    
    #ドリンクメニュー選択
    print("ドリンクメニューはこちら。")
    for drink in range(drinks):
        choice = random.choice(menu.drink_list)
        drink_number = str(drink + 1)
        print(f'drink{drink_number}: {choice}')
    print(partition)
        
if __name__=='__main__':
    choice_mac(mains, sides, drinks)