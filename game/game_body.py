# 导入pygame库
import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# 设置窗口标题
pygame.display.set_caption("Demo")

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充屏幕背景色
    screen.fill((255, 255, 255))  # 白色背景

    # 更新屏幕显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
