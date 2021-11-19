import pygame


class Ship:
    def __init__(self, ai_game):
        # 初始化飞船并设置其初始位置
        self.screen = ai_game.screen
        # 处理飞船位置的矩形大小，用处在碰撞体积检测pygame自带方法
        self.screen_rect = ai_game.screen.get_rect()
        # 加载飞船图像
        self.image = pygame.image.load('img/ship.bmp')
        # 获取外接矩形
        self.rect = self.image.get_rect()
        # 将飞船放置在屏幕底下和中间
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # 实现飞船在屏幕的出现
        self.screen.blit(self.image, self.rect)
