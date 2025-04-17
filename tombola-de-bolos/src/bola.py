import random
import math

class Bola:
    def __init__(self, canvas, centro_x, centro_y, radio_area):
        self.canvas = canvas
        self.radio_area = radio_area
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.x = centro_x
        self.y = centro_y
        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)
        self.id = canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red")

    def mover(self):
        self.x += self.dx
        self.y += self.dy
        dist_x = self.x - self.centro_x
        dist_y = self.y - self.centro_y
        distancia = math.sqrt(dist_x**2 + dist_y**2)
        if distancia + 10 >= self.radio_area:
            angulo = math.atan2(dist_y, dist_x)
            normal_x = math.cos(angulo)
            normal_y = math.sin(angulo)
            dot = self.dx * normal_x + self.dy * normal_y
            self.dx -= 2 * dot * normal_x
            self.dy -= 2 * dot * normal_y
            self.dx += random.uniform(-1, 1)
            self.dy += random.uniform(-1, 1)
        self.canvas.coords(self.id, self.x - 10, self.y - 10, self.x + 10, self.y + 10)