import random
import menu
import sys
eats = int(sys.argv[1])

def choice_mac(eats):
    """今日食べるべきマックを選びます。
       
       いつもは頼まないメニューが食べたくなったら使ってね。
    """
    
    for eat in range(1, eats):
        choice = random.choice(menu.menu_list)
        print(str(eat) + ":" + choice + "!!!")

if __name__=='__main__':
    choice_mac(eats)