# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : setting.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
import pygame


class Settings:
    def __init__(self):
        # 程序主题界面大小颜色设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # -------------------------------
        # 飞船速度设置
        self.ship_speed = 0.3
        # -------------------------------
        # 退出按键设置
        self.quit_key = pygame.K_q
        # -------------------------------
        # 添加子弹设置
        self.bullet_speed = 1.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_fire_type = False
        # -------------------------------
        # 外星人移动初始速度
        self.alien_speed = 1.0
        # 外星人碰撞屏幕边缘时，向下移动速度
        self.fleet_drop_speed = 10
        # 外星人移动方向的描述，1为向右，-1为向左
        self.fleet_direction = 1
