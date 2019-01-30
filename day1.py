# import方法
# 一行目は、pygameパッケージを使用するためのもので、二行目は任意ではあるが、グローバル名前空間に対して定数や関数を追加する。
import pygame
from pygame.locals import *

# init()
# 第一行はpygameのすべてのパッケージを起動しているが、第二行のように個別に起動することも可能である。
pygame.init()
pygame.font.init()

