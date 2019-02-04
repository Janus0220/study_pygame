import pygame
import random
from pygame.locals import *

"""
ノート
TomPongを実装するためのチュートリアルである。
pygameの基本は6つのセクションに分かれる。
1)  Load modules               必要なモジュールをインポートする事を指す。
2)  Resource handling classes  画像やサウンド、ネットアークやファイルのセーブなどの基本的な要素を扱うためのクラスを作成する。
3)  Game object classes        ゲームの中のオブジェクトを作成する。
4)  Any other game functions   その他のゲームに関する関数を作成する。
5)  Initialize the game        ゲームを始動するためのモジュールの始動など
6)  The main loop              ゲームの画面を生成するループを定義する

Pygameの構成要素としては、Screenオブジェクト、backgrounオブジェクト、textオブジェクトが存在し、これらは最初に呼ばれる
事が多い。
 
"""

def main1():
    SCREEN_SIZE_X = 1000
    SCREEN_SIZE_Y = 800

    # スクリーンの始動
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
    pygame.display.set_caption("Basic Pygame program")
    print("SCREEN_SIZE_X: {}\tSCREEN_SIZE_Y: {}".format(screen.get_size()[0], screen.get_size()[1]))

    # 背景色の決定
    background = pygame.Surface(screen.get_size())  # Surfaceインスタンスは覆う画面の大きさを引数に取る。
    background = background.convert()  # 単一のピクセル形式に変換する。これは複数のSurfaceオブジェクトを使用するようになるときに特に必要となる。
    background.fill((0, 250, 250))  # RGBだから白に近い

    # テキストの表示
    font = pygame.font.Font(None, 100)  # pygame.font.Font(フォント, フォントの大きさ)
    text = font.render("Hello, world", 1, (10, 10, 10))  # fontインスタンス.render(表示する文字列, 省略を許すか(0-no, 1yes), (RGBカラー))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx # テキストを載せるオブジェクトはget_rect()によって決定され、centerxとcenteryによって座標が決定される。
    textpos.centery = background.get_rect().centery - 300
    print("textpos_X: {}, textpos_Y: {}".format(textpos.centerx, textpos.centery))
    # screenやbackgroundなどの画面に表示する系のインスタンスはblitメソッドによって画面に表示される。
    background.blit(text, textpos)

    # 画面に差し込む
    screen.blit(background, (0, 0))
    pygame.display.flip() # flipはアップデートを示す。

    # イベントループの生成
    color_r = 255
    color_g = 255
    color_b = 255
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Event type is {}".format(event.type))
                return
            elif event.type == MOUSEBUTTONDOWN:
                print("Event type is {}".format(event.type))
                color_r -= random.random() * 10 if color_r > 10 else 0
                color_g -= random.random() * 10 if color_g > 10 else 0
                color_b -= random.random() * 10 if color_b > 10 else 0
            elif event.type == MOUSEBUTTONUP:
                print("Event type is {}".format(event.type))
                color_r += random.random() * 10 if color_r < 245 else 0
                color_g += random.random() * 10 if color_g < 245 else 0
                color_b += random.random() * 10 if color_b < 245 else 0

        background.fill((color_r, color_g, color_b))
        background.blit(text, textpos)
        screen.blit(background, (0, 0)) # backgroundの更新
        # pygame.display.flip()　



if __name__ == '__main__':
    main1()


