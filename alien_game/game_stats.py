# --------------------------------------------------------
# -*- coding: utf-8 -*-
# File  : game_states.py
# Author: LXY
# Date  : 2021/11
# Software  : VS Code
# --------------------------------------------------------
class GameStates:
    def __init__(self, ai_game):
        # 初始化统计信息板
        self.settings = ai_game.setting
        self.reset_stats()
        # 游戏等待开始
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
