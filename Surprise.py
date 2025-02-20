import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Melancholic Fireworks")

clock = pygame.time.Clock()

melancholic_colors = [
    (150, 0, 0),
    (100, 0, 50),
    (120, 0, 70),
    (80, 0, 80)
]

def draw_heart(surface, pos, size, color, alpha):

    heart_surface = pygame.Surface((size, size), pygame.SRCALPHA)
    
    points = [
         (size * 0.5, size * 0.25),
         (size * 0.85, size * 0.1),
         (size, size * 0.45),
         (size * 0.5, size),
         (0, size * 0.45),
         (size * 0.15, size * 0.1)
    ]
    pygame.draw.polygon(heart_surface, color + (alpha,), points)
    surface.blit(heart_surface, (int(pos[0] - size/2), int(pos[1] - size/2)))

class Particle:
    def __init__(self, x, y, color, angle, speed, is_heart=False):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = 255  
        self.size = random.randint(2, 4)
        self.is_heart = is_heart
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.05  
        self.life -= 3  
    
    def draw(self, surface):
        if self.life > 0:
            alpha = max(self.life, 0)
            if self.is_heart:

                draw_heart(surface, (self.x, self.y), self.size * 8, self.color, alpha)
            else:

                s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
                pygame.draw.circle(s, self.color + (alpha,), (self.size, self.size), self.size)
                surface.blit(s, (int(self.x - self.size), int(self.y - self.size)))

class Firework:
    def __init__(self, is_heart=False):

        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.is_heart = is_heart

        if is_heart:
            self.color = random.choice(melancholic_colors)
        else:
            self.color = (
                random.randint(128, 255),
                random.randint(128, 255),
                random.randint(128, 255)
            )
        self.speed = random.uniform(7, 10)
        self.angle = random.uniform(-math.pi/12, math.pi/12)
        self.vx = math.sin(self.angle) * self.speed
        self.vy = -math.cos(self.angle) * self.speed
        self.exploded = False
        self.particles = []
        self.trail = []  
    
    def update(self):
        if not self.exploded:
            self.trail.append((self.x, self.y))
            if len(self.trail) > 10:
                self.trail.pop(0)
            self.x += self.vx
            self.y += self.vy
            self.vy += 0.15  
            if self.vy >= 0:
                self.explode()
        else:
            for p in self.particles:
                p.update()
            self.particles = [p for p in self.particles if p.life > 0]
    
    def explode(self):
        self.exploded = True
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 5)
            self.particles.append(Particle(self.x, self.y, self.color, angle, speed, is_heart=self.is_heart))
    
    def draw(self, surface):
        if not self.exploded:
            for pos in self.trail:
                pygame.draw.circle(surface, self.color, (int(pos[0]), int(pos[1])), 2)
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 4)
        else:
            for p in self.particles:
                p.draw(surface)

fireworks = []

def main():
    running = True
    while running:

        screen.fill((10, 0, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if random.random() < 0.02:
            if random.random() < 0.3:
                fireworks.append(Firework(is_heart=True))
            else:
                fireworks.append(Firework())

        for fw in fireworks[:]:
            fw.update()
            fw.draw(screen)
            if fw.exploded and not fw.particles:
                fireworks.remove(fw)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
