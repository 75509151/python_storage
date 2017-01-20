# coding:utf-8
import math


class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2):
        try:
            return cls(P2[0] - P1[0], P2[1] - P1[1])
        except Exception:
            return cls(P2.x - P1.x, P2.y - P1.y)

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
        return self.x, self.y

    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)


A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print "Vector AB is", AB
print "AB * 2 is", AB * 2
print "AB / 2 is", AB / 2
print "AB + (- 0, 5) is", AB + Vector2(-10, 5)
print "Magnitude of AB is", AB.get_magnitude()
print "AB normalized is", AB.normalize()

# 结果是下面
# Vector AB is (20.0, 15.0)
# AB * 2 is (40.0, 30.0)
# AB / 2 is (10.0, 7.5)
# AB + (- 0, 5) is (10.0, 20.0)
# Magnitude of AB is 25.0
# AB normalized is (0.8, 0.6)


background_image_filename = 'sushiplate.jpg'
sprite_image_filename = 'fugu.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(sprite, (position.x, position.y))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    # 向量规格化
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading = heading + (vector_to_mouse * .1)

    position += heading * time_passed_seconds
    pygame.display.update()
