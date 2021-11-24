import pygame
from setting import Settings


class Ship:
    def __init__(self, ai_game):
        # 初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        # 调用设置模块
        self.settings = ai_game.setting
        self.setting = Settings()
        # 处理飞船位置的矩形大小，用处在碰撞体积检测pygame自带方法
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像
        self.image = pygame.image.load('img/ship.bmp')
        # 获取外接矩形
        self.rect = self.image.get_rect()
        # 将飞船放置在屏幕底下和中间
        self.rect.midbottom = self.screen_rect.midbottom
        # 飞船左右移动的属性
        self.move_r = False
        self.move_l = False
        self.move_t = False
        self.move_b = False
        # 储存飞船速度值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # 监控飞船上下左右移动位置信息
    def move_update(self):
        # 飞船向右移动，并且小于整个屏幕的长度范围内移动
        if self.move_r and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        # 飞船向左移动，并且保持在最左边初始位置0处开始范围内
        if self.move_l and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 飞船向上移动，并且保持在顶边初始位置0处开始范围内
        if self.move_t and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        # 飞船向下移动，并且小于整个屏幕的高度范围内移动
        if self.move_b and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # 根据self.x更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # 实现飞船在屏幕的出现
        self.screen.blit(self.image, self.rect)
