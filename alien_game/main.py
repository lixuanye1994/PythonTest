import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet


# 游戏程序主要入口，初始化游戏并创建游戏资源
class AlienGame:
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
        # 在主函数初始化存储子弹编组
        self.bullets = pygame.sprite.Group()

    def _check_events(self):
        # 监视键盘和鼠标事件
        for even in pygame.event.get():
            # 监测到退出,调用系统关闭进程
            if even.type == pygame.QUIT:
                sys.exit()
            # 监测玩家按键情况
            elif even.type == pygame.KEYDOWN:
                # 检测玩家按下键盘
                self._check_keydown_events(even)
            elif even.type == pygame.KEYUP:
                # 检测玩家松开键盘
                self._check_keyup_events(even)

    # 重构检测玩家按下键盘
    def _check_keydown_events(self, even):
        if even.key == pygame.K_RIGHT:
            self.ship.move_r = True
        if even.key == pygame.K_LEFT:
            self.ship.move_l = True
        if even.key == pygame.K_UP:
            self.ship.move_t = True
        if even.key == pygame.K_DOWN:
            self.ship.move_b = True
        # 根据设置类实现按键退出
        elif even.key == self.setting.quit_key:
            sys.exit()
        # 按空格开火
        elif even.key == pygame.K_SPACE:
            self._fire_bullet()

    # 重构检测玩家松开键盘
    def _check_keyup_events(self, even):
        if even.key == pygame.K_RIGHT:
            self.ship.move_r = False
        if even.key == pygame.K_LEFT:
            self.ship.move_l = False
        if even.key == pygame.K_UP:
            self.ship.move_t = False
        if even.key == pygame.K_DOWN:
            self.ship.move_b = False

    def _update_screen(self):
        # 让绘制的屏幕可见
        self.screen.fill(self.setting.bg_color)
        # 绘制飞船可见
        self.ship.blitme()
        # 每次生成子弹列表，自动调用屏幕绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 调用pygame显示所有绘制内容
        pygame.display.flip()

    # 创建一颗子弹模板,并加入编组中
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    # 监听子弹
    def _update_bullet(self):
        # 子弹更新  
        self.bullets.update()
        # 删除超出屏幕的子弹，释放内存
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) #//测试子弹列表数值

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 鼠标键盘按键监测
            self._check_events()
            # 飞船移动更新
            self.ship.move_update()
            # 子弹发射更新
            self._update_bullet()
            # 屏幕绘制更新
            self._update_screen()


# 程序开始
if __name__ == '__main__':
    ai = AlienGame()
    ai.run_game()
