import pygame
import math
import random

# --- Initialize Pygame FIRST ---
pygame.init() # This MUST run before any display functions

# --- Configuration (using display info now that pygame is initialized) ---
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

PLAYER_BASE_SPEED = 200
BOOST_SPEED_MULTIPLIER = 1.6 
BOOST_COST_RATE = 100 
INITIAL_FOOD_COUNT = 150
MIN_FOOD_SIZE = 5
MAX_FOOD_SIZE = 15
INITIAL_PLAYER_RADIUS = 10 
BG_COLOR = (20, 20, 20)
PLAYER_COLOR = (0, 200, 0)
MAP_SIZE = 3000

# --- Setup Display and other Pygame modules ---
# Set mode to fullscreen using monitor resolution
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Slither.io Clone (Fullscreen)")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Classes (same as before) ---
class Player:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.radius = INITIAL_PLAYER_RADIUS
        self.score = 0
        self.color = PLAYER_COLOR
        self.length = 150 
        self.base_speed = PLAYER_BASE_SPEED
        self.speed = self.base_speed
        self.positions = [self.pos.copy()] * int(self.length)
        self.boosting = False
    def update(self, dt):
        speed_multiplier = BOOST_SPEED_MULTIPLIER if self.boosting else 1.0
        size_multiplier = (INITIAL_PLAYER_RADIUS / self.radius)
        self.speed = max(100, self.base_speed * size_multiplier * speed_multiplier)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        target = pygame.math.Vector2(mouse_x - SCREEN_WIDTH // 2, mouse_y - SCREEN_HEIGHT // 2)
        direction = pygame.math.Vector2(0, 0)
        if target.length_squared() > 0:
            direction = target.normalize()
            self.pos += direction * self.speed * dt
        self.pos.x = max(self.radius, min(MAP_SIZE - self.radius, self.pos.x))
        self.pos.y = max(self.radius, min(MAP_SIZE - self.radius, self.pos.y))
        shed_food_item = None
        if self.boosting and self.length > 50:
            mass_lost = BOOST_COST_RATE * dt
            self.length -= mass_lost
            self.score -= mass_lost * 0.1 
            if len(self.positions) > 10: 
                shed_pos = self.positions[-10]
                shed_food_item = Food(shed_pos.x, shed_pos.y, is_shed=True)
        self.positions.insert(0, self.pos.copy()) 
        self.positions = self.positions[:int(self.length)]
        self.update_radius()
        return shed_food_item
    def update_radius(self):
         self.radius = INITIAL_PLAYER_RADIUS + math.sqrt(self.length / 10.0)
    def grow(self, mass_gained):
        self.length += mass_gained
        self.score += mass_gained
        self.update_radius()
    def draw(self, surface, camera_x, camera_y):
        offset_x = -camera_x + SCREEN_WIDTH // 2
        offset_y = -camera_y + SCREEN_HEIGHT // 2
        for i, pos in enumerate(self.positions):
            taper_factor = 1 - (i / len(self.positions)) * 0.7 
            segment_radius = max(1, self.radius * taper_factor)
            screen_x = pos.x + offset_x
            screen_y = pos.y + offset_y
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), int(segment_radius))

class Food:
    def __init__(self, x, y, is_shed=False):
        self.pos = pygame.math.Vector2(x, y)
        if is_shed:
            self.radius = 4
            self.value = 5
            self.color = (150, 150, 150)
        else:
            self.radius = random.randint(MIN_FOOD_SIZE, MAX_FOOD_SIZE)
            self.value = self.radius * 2
            self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    def draw(self, surface, camera_x, camera_y):
        screen_x = self.pos.x - camera_x + SCREEN_WIDTH // 2
        screen_y = self.pos.y - camera_y + SCREEN_HEIGHT // 2
        if -self.radius < screen_x < SCREEN_WIDTH + self.radius and -self.radius < screen_y < SCREEN_HEIGHT + self.radius:
            pygame.draw.circle(surface, self.color, (int(screen_x), int(screen_y)), self.radius)

# --- Game Setup ---
player = Player(MAP_SIZE // 2, MAP_SIZE // 2)
foods = []
def generate_food(count):
    for _ in range(count):
        x = random.randint(MAX_FOOD_SIZE, MAP_SIZE - MAX_FOOD_SIZE)
        y = random.randint(MAX_FOOD_SIZE, MAP_SIZE - MAX_FOOD_SIZE)
        foods.append(Food(x, y))
generate_food(INITIAL_FOOD_COUNT)

# --- Main Game Loop ---
running = True
while running:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.boosting = True
            if event.key == pygame.K_ESCAPE: 
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.boosting = False

    # Update Game State
    shed_food = player.update(dt) 
    if shed_food:
        foods.append(shed_food)

    # Handle Food Collisions and Drawing (omitted for brevity, code is same as above)
    foods_to_remove = []
    for food in foods:
        distance = player.pos.distance_to(food.pos)
        if distance < player.radius + food.radius:
            foods_to_remove.append(food)
            player.grow(food.value) 
    for food in foods_to_remove:
        foods.remove(food)
    if len(foods) < INITIAL_FOOD_COUNT + 50:
        generate_food(1)
    camera_x = player.pos.x
    camera_y = player.pos.y

    # Drawing
    screen.fill(BG_COLOR)
    map_left = -camera_x + SCREEN_WIDTH // 2
    map_top = -camera_y + SCREEN_HEIGHT // 2
    pygame.draw.rect(screen, (100, 100, 100), (map_left, map_top, MAP_SIZE, MAP_SIZE), 5)
    for food in foods:
        food.draw(screen, camera_x, camera_y)
    player.draw(screen, camera_x, camera_y)
    pygame.display.flip()

# This call de-initializes the video system cleanly upon exiting the loop
pygame.quit()