from turtle import *

# --- Setup ---
screen = Screen()
screen.tracer(0)
screen.setup()
screen.title("Turtle Platformer")

# --- Player setup ---
player = Turtle()
player.shape("triangle")
player.left(90)
player.color("black")
player.shapesize(1, 1)
player.penup()
player.goto(0, -230)

# --- Physics ---
gravity = -1
yvel = 0
xvel = 0
keys_pressed = set()
on_ground = False

# --- Platforms ---
platforms = []
boosters = []

def make_platform(x, y, width, height):
    p = Turtle()
    p.shape("square")
    p.color("black")
    p.shapesize(height / 20, width / 20)
    p.penup()
    p.goto(x, y)
    platforms.append((x, y, width, height))
    return p

def make_booster(x, y, width, height):
    b = Turtle()
    b.shape("square")
    b.color("light green")
    b.shapesize(height / 20, width / 20)
    b.penup()
    b.goto(x, y)
    boosters.append((x, y, width, height))
    return b

# Ground + Floating Platforms
platform_assigner = {
    "1-1": [[0, -400, 1510, 10, "w"], # Ground
            [750, 100, 10, 1000, "w"], # Right wall
            [-750, 100, 10, 1000, "w"], # Left wall
            [-200, -250, 200, 10, "w"],
            [200, -150, 200, 10, "w"],
            [-200, -50, 200, 10, "w"], 
            [200, 50, 200, 10, "w"], 
            [0, 200, 150, 10, "w"], 
            [0, 400, 150, 100, "b"],
            [450, -100, 150, 100, "b"],
            [-450, -100, 150, 100, "b"]
            ]
}
for platform in platform_assigner["1-1"]:
    if platform[4] == "w":
        make_platform(platform[0], platform[1], platform[2], platform[3])
    elif platform[4] == "b":
        make_booster(platform[0], platform[1], platform[2], platform[3])


# --- Input handling ---
def key_down(key):
    keys_pressed.add(key)

def key_up(key):
    keys_pressed.discard(key)

def quit_game():
    screen.bye()

# Bind keys
screen.listen()
for key in ["a", "d", "w"]:
    screen.onkeypress(lambda k=key: key_down(k), key)
    screen.onkeyrelease(lambda k=key: key_up(k), key)
screen.onkeypress(quit_game, "q")

# --- Collision detection ---
def check_platform_collision(old_y, new_y, px, vy):
    player_half_height = 10
    for (x, y, width, height) in platforms:
        half_width = width / 2
        if abs(px - x) < half_width:
            plat_top = y + height / 2
            plat_bottom = y - height / 2

            bottom_old = old_y - player_half_height
            bottom_new = new_y - player_half_height
            top_old = old_y + player_half_height
            top_new = new_y + player_half_height

            # Landing on top
            if vy < 0 and bottom_old >= plat_top and bottom_new <= plat_top:
                return ("land", plat_top)

            # Hitting head (ceiling)
            if vy > 0 and top_old <= plat_bottom and top_new >= plat_bottom:
                return ("head", plat_bottom)

    return (None, None)


def check_horizontal_collision(old_x, new_x, py, vx):
    player_half_width = 10
    player_half_height = 10
    for (x, y, width, height) in platforms:
        half_width = width / 2
        plat_left = x - half_width
        plat_right = x + half_width
        plat_top = y + height / 2
        plat_bottom = y - height / 2

        # Check vertical overlap between player (at py) and platform
        player_top = py + player_half_height
        player_bottom = py - player_half_height
        if player_bottom < plat_top and player_top > plat_bottom:
            # moving right -> check collision with platform left side
            if vx > 0:
                if old_x + player_half_width <= plat_left and new_x + player_half_width >= plat_left:
                    return (plat_left - player_half_width, 0)
            # moving left -> check collision with platform right side
            elif vx < 0:
                if old_x - player_half_width >= plat_right and new_x - player_half_width <= plat_right:
                    return (plat_right + player_half_width, 0)

    return (new_x, vx)


def check_booster_collision(old_y, new_y, old_x, new_x, px, vy, vx):
    player_half = 10
    for (x, y, width, height) in boosters:
        half_width = width / 2
        # Check horizontal overlap (player center within platform half-width)
        if abs(px - x) <= half_width:
            plat_top = y + height / 2
            plat_bottom = y - height / 2
            plat_left = x + height / 2
            plat_right = y + height / 2

            bottom_old = old_y - player_half
            bottom_new = new_y - player_half
            top_old = old_y + player_half
            top_new = new_y + player_half
            left_old = old_x - player_half
            left_new = new_x - player_half
            right_old = old_x + player_half
            right_new = new_x + player_half

            if vy < 0 and bottom_old >= plat_top and bottom_new <= plat_top:
                return ("land", plat_top)

            if vy > 0 and top_old <= plat_bottom and top_new >= plat_bottom:
                return ("head", plat_bottom)
            
            if vx < 0 and left_old >= plat_right and left_new <= plat_right:
                return ("side", plat_right)
            
            if vx > 0 and right_old <= plat_left and right_new >= plat_left:
                return ("side", plat_left)

    return (None, None)

# --- Game loop ---
def game_loop():
    global xvel, yvel, on_ground

    old_y = player.ycor()
    old_x = player.xcor()

    # Handle input
    if "a" in keys_pressed:
        xvel = -10
    elif "d" in keys_pressed:
        xvel = 10
    else:
        xvel = 0

    # Jump only if the player is on ground (prevents jumping at apex)
    if "w" in keys_pressed and on_ground:
        yvel = 20
        on_ground = False

    # Apply gravity
    yvel += gravity
    new_y = player.ycor() + yvel
    new_x = player.xcor() + xvel

    # Check for new level
    if new_y > 500:
        new_y = -230
        new_x = 0
        yvel = 0
        xvel = 0
        on_ground = False
    
    # Check horizontal collisions first and adjust x position/velocity
    new_x, xvel = check_horizontal_collision(old_x, new_x, new_y, xvel)

    # Check platform collisions (top and bottom)
    collision_type, platform_y = check_platform_collision(old_y, new_y, old_x, yvel)
    if collision_type == "land":
        new_y = platform_y + 10
        yvel = 0
        on_ground = True
    elif collision_type == "head":
        new_y = platform_y - 10
        yvel = -2
        on_ground = False

    # Check booster collisions (boosters propel the player upward instead of stopping)
    boost_collision_type, boost_y = check_booster_collision(old_y, new_y, old_x, new_x, new_x, yvel, xvel)
    if boost_collision_type != None:
        yvel = 0
        yvel += 30
    player.goto(new_x, new_y)
    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()
