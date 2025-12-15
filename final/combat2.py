import curses
import math
import time

def rotate_point(x, y, cx, cy, angle):
    s, c = math.sin(angle), math.cos(angle)
    nx = (x - cx) * c - (y - cy) * s + cx
    ny = (x - cx) * s + (y - cy) * c + cy
    return nx, ny

def draw_rotated_car(stdscr, car_lines, center_x, center_y, angle):
    car_height = len(car_lines)
    car_width = max(len(line) for line in car_lines)
    cx_car = car_width / 2
    cy_car = car_height / 2

    for j, line in enumerate(car_lines):
        for i, ch in enumerate(line):
            if ch.strip() == "":
                continue
            rx, ry = rotate_point(i, j, cx_car, cy_car, angle)
            screen_x = int(center_x + rx - cx_car)
            screen_y = int(center_y + ry - cy_car)
            try:
                stdscr.addch(screen_y, screen_x, ch)
            except curses.error:
                pass

def generate_grid(walls, width, height):
    grid = [[False]*width for _ in range(height)]
    for wall in walls:
        (x1, y1), (x2, y2) = wall
        if x1 == x2:  # vertical wall
            for y_pos in range(min(y1,y2), max(y1,y2)+1):
                if 0 <= y_pos < height and 0 <= x1 < width:
                    grid[y_pos][x1] = True
        elif y1 == y2:  # horizontal wall
            for x_pos in range(min(x1,x2), max(x1,x2)+1):
                if 0 <= y1 < height and 0 <= x_pos < width:
                    grid[y1][x_pos] = True
    return grid

def draw_grid(stdscr, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                try:
                    stdscr.addch(y, x, '#')
                except curses.error:
                    pass

def check_collision_grid(x, y, car_lines, angle, grid):
    car_height = len(car_lines)
    car_width = max(len(line) for line in car_lines)
    cx_car, cy_car = car_width/2, car_height/2
    for j, line in enumerate(car_lines):
        for i, ch in enumerate(line):
            if ch.strip() == "":
                continue
            rx, ry = rotate_point(i, j, cx_car, cy_car, angle)
            gx = int(x + rx - cx_car)
            gy = int(y + ry - cy_car)
            if 0 <= gy < len(grid) and 0 <= gx < len(grid[0]) and grid[gy][gx]:
                return True
    return False

def draw_hud(stdscr, speed, fuel):
    hud_y, hud_x = stdscr.getmaxyx()
    hud_y -= 2
    hud_x = 2
    stdscr.addstr(hud_y, hud_x, f"Speed: {speed:.1f}  ")
    stdscr.addstr(hud_y + 1, hud_x, f"Fuel: {fuel:.1f}  ")

courses = [
    [
        [(10,5), (10,15)],
        [(10,15), (30,15)],
        [(30,15), (30,5)],
        [(30,5), (10,5)]
    ],
    [
        [(5,5),(5,20)],
        [(5,20),(40,20)],
        [(40,20),(40,5)],
        [(40,5),(5,5)]
    ]
]
def car_game(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    height, width = stdscr.getmaxyx()

    car_text = """
---
- -
---
"""
    car_lines = car_text.splitlines()

    car_width = max(len(line) for line in car_lines)
    car_height = len(car_lines)

    x = car_width // 2 + 25
    y = car_height // 2 + 25

    angle = 0
    speed = 0
    ROTATE_DELTA = 0.5
    ACCELERATION = 0.1
    MAX_SPEED = 1
    FUEL_CONSUMPTION = 0.01
    fuel = 100.0

    current_course = 0
    walls = courses[current_course]
    grid = generate_grid(walls, width, height)

    for row in range(height):
        grid[row][0] = True
        grid[row][width-1] = True
    for col in range(width):
        grid[0][col] = True
        grid[height-1][col] = True

    left_pressed = False
    right_pressed = False
    up_pressed = False
    down_pressed = False

    while True:
        key = stdscr.getch()

        if key != -1:
            if key in (ord('q'), 27):
                break
            elif key == curses.KEY_LEFT:
                left_pressed = True
            elif key == curses.KEY_RIGHT:
                right_pressed = True
            elif key == curses.KEY_UP:
                up_pressed = True
            elif key == curses.KEY_DOWN:
                down_pressed = True
            elif key in (ord('1'), ord('2')):
                current_course = int(chr(key)) - 1
                walls = courses[current_course]
                grid = generate_grid(walls, width, height)
        else:
            left_pressed = False
            right_pressed = False
            up_pressed = False
            down_pressed = False

        rotation_speed = 0
        if left_pressed:
            rotation_speed -= ROTATE_DELTA
        if right_pressed:
            rotation_speed += ROTATE_DELTA

        new_angle = angle + rotation_speed
        if not check_collision_grid(x, y, car_lines, new_angle, grid):
            angle = new_angle
        else:
            rotation_speed = 0

        if up_pressed:
            speed = min(speed + ACCELERATION, MAX_SPEED)
        if down_pressed:
            speed = max(speed - ACCELERATION * 10, 0)

        dx = math.sin(angle) * speed
        dy = -math.cos(angle) * speed

        new_x = x + dx
        new_y = y + dy

        if not check_collision_grid(new_x, y, car_lines, angle, grid):
            x = new_x
        else:
            dx = 0

        if not check_collision_grid(x, new_y, car_lines, angle, grid):
            y = new_y
        else:
            dy = 0

        speed = math.hypot(dx, dy)
        if speed > 0:
            angle = math.atan2(dx, -dy)

        fuel = max(fuel - abs(speed) * FUEL_CONSUMPTION, 0)
        if fuel <= 0:
            speed = 0

        stdscr.clear()
        draw_grid(stdscr, grid)
        draw_rotated_car(stdscr, car_lines, x, y, angle)
        draw_hud(stdscr, speed, fuel)
        stdscr.refresh()
        time.sleep(0.01)

curses.wrapper(car_game)