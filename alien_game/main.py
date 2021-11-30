# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : main.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
import sys
import pygame
import time
from setting import Settings
from game_stats import GameStates
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        # 设置游戏框显示为"外星人入侵"
        pygame.display.set_caption("外星人入侵")
        # 导入统计信息模块
        self.stats = GameStates(self)
        # 导入飞船类并初始化飞船类，将AlienGame传入Ship()
        self.ship = Ship(self)
        # 在主函数初始化存储子弹编组
        self.bullets = pygame.sprite.Group()
        # 在主函数初始化存储外星人编组
        self.aliens = pygame.sprite.Group()
        # 存储外星人群
        self._create_aiteam()
        # 创建Play按钮
        self.play_button = Button(self, "Play Game")

    def _check_events(self):
        # 监视键盘和鼠标事件
        for even in pygame.event.get():
            # 监测到退出,调用系统关闭进程
            if even.type == pygame.QUIT:
                sys.exit()
            elif even.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            # 监测玩家按键情况
            elif even.type == pygame.KEYDOWN:
                # 检测玩家按下键盘
                self._check_keydown_events(even)
            elif even.type == pygame.KEYUP:
                # 检测玩家松开键盘
                self._check_keyup_events(even)

    # 监测鼠标点击开始
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

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
            self.setting.bullet_fire_type = True

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
        elif even.key == pygame.K_SPACE:
            self.setting.bullet_fire_type = False

    # 创建一颗子弹模板,并加入编组中
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        # time.sleep(0.1)

    # 监听子弹
    def _update_bullet(self):
        # 长按一直开火功能实现
        if self.setting.bullet_fire_type:
            self._fire_bullet()
        # 子弹更新
        self.bullets.update()
        # 删除超出屏幕的子弹，释放内存
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets)) #//测试子弹列表数值
        # 检测子弹射中外星人情况
        self._check_bullet_alien_collisions()

    # 检测子弹射中外星人情况
    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_aiteam()

    # 创建外星人群的大框架方法
    def _create_aiteam(self):
        # 创建单个外星人实例用于计算，不加入游戏编组
        al = Alien(self)
        # 从单个实例中计算外星人矩形的宽值，长值
        al_width, al_height = al.rect.size
        # 屏幕总长-2倍外星人宽值=可用剩余长度
        available_space_x = self.setting.screen_width - (2 * al_width)
        # 可用长度与2倍外星人宽值模运算获得一行可放置外星人的个数
        num_als_x = available_space_x // (2 * al_width)

        # 计算屏幕可以容纳多少外星人,屏幕可使用高度，原理：飞船高度+外星人高度两倍处留白用于击杀
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height - (3 * al_height) - ship_height)
        # 可用长度与2倍外星人高值模运算获得可放置外星人的多个行数
        num_rows = available_space_y // (2 * al_height)
        # 循环放置外星人，第一次循环确定在屏幕中一共多少行外星人，第二次循环确定每一行有几个外星人
        for row_num in range(num_rows):
            for al_num in range(num_als_x):
                # 循环生成外星人,控制个数和行数
                self._create_alien_allscreen(al_num, row_num)

    # 创建全屏外星人群核心代码,从大框架传入需要生成外星人矩阵个数，行数
    def _create_alien_allscreen(self, al_num, row_num):
        # 生成一个外星人，确定所需长宽，传到上方循环处，生成批量满屏幕外星人
        al = Alien(self)
        al_width, al_height = al.rect.size
        al.x = al_width + 2 * al_width * al_num
        al.rect.x = al.x
        al.rect.y = al.rect.height + 2 * al.rect.height * row_num
        self.aliens.add(al)

    # 监听外星人运动到屏幕边缘
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # 外星人运动到屏幕边缘触发向下移动
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        # 向下移动后设置外星人从反方向移动，防止外星人跑出屏幕
        self.setting.fleet_direction *= -1

    # 检测外星人撞到飞船
    def _ship_hit(self):
        # 如果坠毁,继续调用飞船，直到用完
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            # 坠毁同时清空外星人
            self.aliens.empty()
            # 坠毁同时清空屏幕剩余子弹
            self.bullets.empty()
            # 重新生成外星人群
            self._create_aiteam()
            # 飞船重新放回
            self.ship.center_ship()
            # 停顿0.5秒重新开始游戏
            time.sleep(0.5)
        else:
            # 如果飞船次数用完，游戏结束
            self.stats.game_active = False

    # 检测外星人到达屏幕底端
    def _check_aliens_bottem(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    # 检测外星人移动,检测外星人是否运动到屏幕边缘
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        # 检测碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检测外星人到达屏幕底端
        self._check_aliens_bottem()

    # 监听屏幕所有动态更新
    def _update_screen(self):
        # 让绘制的屏幕可见
        self.screen.fill(self.setting.bg_color)
        # 绘制飞船可见
        self.ship.blitme()
        # 每次生成子弹列表，自动调用绘制子弹
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 绘制外星人可见
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 调用pygame显示所有绘制内容
        pygame.display.flip()

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 鼠标键盘按键监测
            self._check_events()
            if self.stats.game_active:
                # 飞船移动更新
                self.ship.move_update()
                # 子弹发射更新
                self._update_bullet()
                # 外星人移动更新
                self._update_aliens()
            # 屏幕绘制更新
            self._update_screen()


# 程序开始
if __name__ == '__main__':
    ai = AlienGame()
    ai.run_game()
