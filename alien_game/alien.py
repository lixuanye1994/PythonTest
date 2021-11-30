# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : alien.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
import pygame
from pygame.sprite import Sprite


# 单个外星人类
class Alien(Sprite):
    # 外星人船队继承pygame中的Sprite精灵类
    def __init__(self, ai_game):
        super().__init__()
        # 初始化外星人并设置其初始位置
        self.screen = ai_game.screen
        # 调用设置模块
        self.settings = ai_game.setting
        # 加载外星人图像
        self.image = pygame.image.load('img/alien2.bmp')
        # 获取外接矩形
        self.rect = self.image.get_rect()
        # -------------------------------

        """
        初始载入单个外星人会在(0,0)处生成，
        将外星人的宽度长设置为需要出现的X处，
        将外星人的高度长设置为需要出现的y处，
        这样定义可以在屏幕中看到边缘留白，留白大小刚好一个外星人的长和宽
        """
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 储存x坐标的小数
        self.x = float(self.rect.x)

    # 监听外星人移动情况
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # 如果监测到外星人位于屏幕边缘，返回Ture
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    # 外星人向左或者向右自行移动
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
