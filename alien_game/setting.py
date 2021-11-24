import pygame


class Settings:
    def __init__(self):
        # 程序主题界面大小颜色设置
        self.screnn_width = 400
        self.screnn_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船速度设置
        self.ship_speed = 0.3
        # 退出按键设置
        self.quit_key = pygame.K_q
        # 添加子弹设置
        self.bullet_speed = 1.6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_fire_type = False
