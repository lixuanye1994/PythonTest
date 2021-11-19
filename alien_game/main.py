import sys
import pygame
from setting import Settings
from ship import Ship


class AlienGame:

    # 游戏程序主要入口，初始化游戏并创建游戏资源

    def __init__(self):
        pygame.init()
        # 设置游戏窗口大小，1200x800，并设置游戏名字
        # self.screen = pygame.display.set_mode((1200, 800))
        # 设置游戏背景颜色
        # self.bg_color = (230, 230, 230)
        # 将以上设置全部打包成模块Settings()，导入设置模块
        self.setting = Settings()
        # 设置打开屏幕框的预设值
        self.screen = pygame.display.set_mode((self.setting.screnn_width, self.setting.screnn_height))
        # 设置游戏框显示为"外星人入侵"
        pygame.display.set_caption("外星人入侵")
        # 导入飞船类并初始化飞船类，将AlienGame传入Ship()
        self.ship = Ship(self)

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监视键盘和鼠标事件
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()
            # 让绘制的屏幕可见
            self.screen.fill(self.setting.bg_color)
            # 绘制飞船可见
            self.ship.blitme()
            # 调用pygame显示所有绘制内容
            pygame.display.flip()


# 程序开始
if __name__ == '__main__':
    ai = AlienGame()
    ai.run_game()
