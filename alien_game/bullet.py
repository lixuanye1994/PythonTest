# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : bullet.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
import pygame
from pygame.sprite import Sprite


# 子弹类继承Sprite精灵类，编组实现子弹放射
class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # 在飞船的当前位置生成子弹，显示在屏幕上
        self.screen = ai_game.screen
        # 导入设置类，导入设置
        self.setting = ai_game.setting
        # 设置子弹颜色
        self.color = self.setting.bullet_color
        # 从坐标(0,0)处生成子弹矩形，由于子弹是代码生成没有具体位置，必须从(0,0)处生成
        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)
        # 将生成的子弹再挪动到合适的位置，放置在飞船头部
        self.rect.midtop = ai_game.ship.rect.midtop
        # 强制保存y坐标小数值
        self.y = float(self.rect.y)

    # 子弹轨迹，向上移动，此处是一个坑点，update() 实际上是重写了Sprite.update()，不能自定义方法名字
    def update(self):
        # 更新表示子弹位置的小数值
        self.y -= self.setting.bullet_speed
        # 更新子弹的矩形位置
        self.rect.y = self.y

    # 在屏幕上绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
