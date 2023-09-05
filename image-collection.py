from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from bs4 import BeautifulSoup
import os
import time


def image_collection():
    chrome_service = fs.Service()
    browser = webdriver.Chrome(service=chrome_service)

    # Google画像検索のURLを指定
    url = "https://www.google.co.jp/imghp?hl=ja"
    browser.get(url)

    # 検索キーワードを入力するHTML要素を取得
    selector = "textarea[title='検索']"  # 最新のセレクタに変更

    # WebDriverWaitを使って要素が見つかるまで待機
    try:
        kw_search = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
    except Exception as e:
        print(f"Error: {e}")
        browser.quit()
        exit()

    # 検索キーワードを指定
    actor_name = "カワセミ"

    # ブラウザに検索キーワードを投入
    kw_search.send_keys(str(actor_name))
    kw_search.send_keys(Keys.ENTER)

    # 画像検索したページのURLを取得する
    cur_url = browser.current_url
    res = requests.get(cur_url)
    time.sleep(3)

    # 取得する画像の枚数を設定
    img_limit = 100
    img_count = 0

    # 画面のスクロールを行う。
    try:
        img_urls = []
        # 画面を5回スクロール(スクロールしないと20枚しか取得できない)
        for i in range(5):
            # 画面をスクロール
            browser.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);")
            # BeautifulSoupを読み込み
            soup = BeautifulSoup(browser.page_source, "html.parser")

            # imgタグのHTML要素を全て取得する
            for image in soup.find_all("img"):
                # 画像の取得上限を超えたら終了
                if img_count >= img_limit:
                    break

                try:
                    url = image.get("data-src")

                    if url is None:
                        url = image.get("src")

                    if url is not None:
                        # ファビコンやpng、svgなどの場合はスキップ
                        if ('favicon' in url) or ('.png' in url) or ('.svg' in url) or ('data:image/' in url):
                            continue
                        if url in img_urls:
                            continue
                        img_urls.append(url)
                        img_count += 1
                except Exception as inner_exception:
                    print(f"画像のURL取得に失敗しました: {inner_exception}")
            sleep(2)

    except Exception as e:
        print(f"画面スクロールに失敗しました: {e}")

    # 保存先のディレクトリ
    dl_dir = "download"

    # ダウンロードディレクトリが存在しない場合は作成
    if not os.path.exists(dl_dir):
        os.mkdir(dl_dir)

    # フォルダ数のカウント(連番用)
    dir_count = 0
    files = os.listdir(dl_dir)
    for f in files:
        path = os.path.join(dl_dir, f)
        if os.path.isdir(path):
            dir_count += 1

    # 連番を付与して画像検索キーワードと同名のディレクトリ名を生成
    save_dir = dl_dir + "/" + str(dir_count) + "_" + actor_name

    # サブディレクトリが存在しない場合は作成
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    # 取得した画像のデータを保存する
    file_number = 1
    for elem_url in img_urls:
        try:
            r = requests.get(elem_url)
            with open(save_dir + "/" + str(actor_name) + "_" + str(file_number) + ".jpg", "wb") as fp:
                fp.write(r.content)
            file_number += 1
            sleep(0.1)
        except Exception as e:
            print(f"画像の保存に失敗しました: {e}")

    browser.quit()


if __name__ == '__main__':
    image_collection()
