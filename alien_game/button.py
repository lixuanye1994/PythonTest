# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : button.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
import pygame.font


# 按钮类
class Button:
    def __init__(self, ai_game, msg):
        # 设置按钮颜色大小宽度字体
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 创建按钮的rect对象，居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 创建按钮标签
        self._prep_msg(msg)

    # 将msg按钮渲染为图片，并居中显示
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # 将图片绘制到屏幕上
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
