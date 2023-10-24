#!/usr/bin/env python3

import base64
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import os

# setting args
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", type=str, help="target url",
                    default="https://www.selenium.dev/ja/")
parser.add_argument("-d", "--dir", type=str,
                    help="image output dir pass", default="./screenshot")
parser.add_argument("-f", "--file", type=str,
                    help="image output file name", default="./screenshot")
args = parser.parse_args()


def save_screenshot(driver, file_path, is_full_size=False):
    # スクリーンショット設定
    screenshot_config = {
        # Trueの場合スクロールで隠れている箇所も含める、Falseの場合表示されている箇所のみ
        "captureBeyondViewport": is_full_size,
    }
    # スクリーンショット取得
    base64_image = driver.execute_cdp_cmd(
        "Page.captureScreenshot", screenshot_config)

    # make dir
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    # ファイル書き出し
    with open(file_path, "wb") as fh:
        fh.write(base64.urlsafe_b64decode(base64_image["data"]))


# setting webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# ウィンドウ最大化
driver.maximize_window()
# サイト表示
driver.get(args.url)

# ページ上のすべての要素が読み込まれるまで待機（15秒でタイムアウト判定）
WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

# 見えている箇所のみのスクリーンショット取得 取得イメージ①
save_screenshot(driver, f'{args.dir}/not_full_size.png')
# 全画面スクリーンショット取得　取得イメージ②
save_screenshot(driver, f'{args.dir}/full_size.png', is_full_size=True)
