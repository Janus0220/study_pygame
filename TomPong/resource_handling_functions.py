#!/usr/bin/env python
#
# Tom's Pong
# A simple pong game with realistic physics and AI
# http://www.tomchance.uklinux.net/projects/pong.shtml
#
# Released under the GNU General Public License

VERSION = "0.4"

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print("couldn't load module. {}".format(err))
    sys.exit(2)


def load_png(name):
    """ 画像をロードし、画像と画像の矩形オブジェクトを返す"""
    fullname = os.path.join(os.path.dirname(__file__), 'data', name)
    try:
        image = pygame.image.load(fullname) # 画像をロードし、Surfaceインスタンスを返す
        # Surfaceインスタンス.get_alpha()は透過性(Transparency alpha)を取得する。
        if image.get_alpha() is None:
            image = image.convert()  # ピクセル方式の画像に変換する.
        else:
            image = image.convert_alpha() # ピクセルの透過性を含んだ形でピクセル形式に変換する。
    except pygame.error as message:
        print('Cannot load image:', fullname)
        print(message)
        raise SystemExit
    return image, image.get_rect()
