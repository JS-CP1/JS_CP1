import random

player = {
    "wins": 0,
    "money": 500000,
    "car": ""
}

cars = {
    "ae86": {"name": "Toyota AE86 Trueno", "tires": 40000, "grip": 5, "hp": 130},
    "fd_rx7": {"name": "Mazda RX-7 FD3S", "tires": 100000, "grip": 8, "hp": 200},
    "civic": {"name": "Toyota AE86 Trueno Hatchback", "tires": 150000, "grip": 7, "hp": 190},
    "nismo": {"name": "Toyota AE86 Trueno Hatchback", "tires": 500000, "grip": 25, "hp": 600},
    "ae85": {"name": "Toyota AE85 Levin", "tires": 60000, "grip": 4, "hp": 85},
    "supra_rz": {"name": "Toyota Supra RZ", "tires": 150000, "grip": 9, "hp": 320},
    "mr2_sw20": {"name": "Toyota MR2 SW20", "tires": 90000, "grip": 7, "hp": 200},
    "celica_st204": {"name": "Toyota Celica ST204", "tires": 95000, "grip": 7, "hp": 170},
    "fc_rx7": {"name": "Mazda RX-7 FC3S", "tires": 90000, "grip": 7, "hp": 180},
    "roadster_na6ce": {"name": "Mazda Eunos Roadster NA6CE", "tires": 70000, "grip": 6, "hp": 115},
    "eg6_civic": {"name": "Honda Civic SiR-II EG6", "tires": 85000, "grip": 7, "hp": 170},
    "ek9_civic": {"name": "Honda Civic Type R EK9", "tires": 95000, "grip": 8, "hp": 185},
    "nsx_na1": {"name": "Honda NSX NA1", "tires": 150000, "grip": 10, "hp": 280},
    "crx_ef8": {"name": "Honda CR-X EF8", "tires": 80000, "grip": 6, "hp": 150},
    "silvia_s13": {"name": "Nissan Silvia S13", "tires": 80000, "grip": 7, "hp": 160},
    "silvia_s14": {"name": "Nissan Silvia S14", "tires": 85000, "grip": 7, "hp": 200},
    "silvia_s15": {"name": "Nissan Silvia S15", "tires": 95000, "grip": 8, "hp": 250},
    "skyline_r32": {"name": "Nissan Skyline GT-R R32", "tires": 140000, "grip": 10, "hp": 280},
    "skyline_r34": {"name": "Nissan Skyline GT-R R34", "tires": 160000, "grip": 10, "hp": 320},
    "180sx": {"name": "Nissan 180SX", "tires": 85000, "grip": 7, "hp": 170},
    "sil80": {"name": "Nissan SilEighty", "tires": 80000, "grip": 7, "hp": 175},
    "evo3": {"name": "Mitsubishi Lancer Evolution III", "tires": 130000, "grip": 9, "hp": 270},
    "evo4": {"name": "Mitsubishi Lancer Evolution IV", "tires": 135000, "grip": 9, "hp": 280},
    "evo5": {"name": "Mitsubishi Lancer Evolution V", "tires": 140000, "grip": 9, "hp": 280},
    "evo6": {"name": "Mitsubishi Lancer Evolution VI", "tires": 145000, "grip": 9, "hp": 280},
    "impreza": {"name": "Subaru Impreza WRX STi GC8", "tires": 120000, "grip": 9, "hp": 280},
    "cappuccino": {"name": "Suzuki Cappuccino EA11R", "tires": 60000, "grip": 6, "hp": 65},
    "benz_190e": {"name": "Mercedes-Benz 190E W201", "tires": 110000, "grip": 8, "hp": 170},
    "porsche_911": {"name": "Porsche 911 Turbo 964", "tires": 160000, "grip": 10, "hp": 320},
    "alfa_romeo_4c": {"name": "Alfa Romeo 4C", "tires": 140000, "grip": 9, "hp": 240}
}

enemies = {
    "takahashi": {"name": "Ryosuke Takahashi", "car": "Mazda RX-7 FC3S", "track": "Akagi", "skill": 9},
    "impact_blue": {"name": "Mako Sato & Sayuki", "car": "Nissan SilEighty", "track": "Usui Pass", "skill": 6},
    "bunta": {"name": "Bunta Fujiwara", "car": "Subaru Impreza WRX STi GC8", "track": "Akina", "skill": 10},
    "takeshi": {"name": "Takeshi Nakazato", "car": "Nissan Skyline GT-R R32", "track": "Myogi", "skill": 8},
    "shingo": {"name": "Shingo Shoji", "car": "Honda Civic EG6", "track": "Myogi", "skill": 6},
    "kyoichi": {"name": "Kyoichi Sudo", "car": "Mitsubishi Lancer Evolution III", "track": "Akagi", "skill": 8},
    "seiji": {"name": "Seiji Iwaki", "car": "Mitsubishi Lancer Evolution IV", "track": "Akina", "skill": 7},
    "hideo": {"name": "Hideo Minagawa", "car": "Toyota Supra RZ", "track": "Irohazaka", "skill": 7},
    "kai": {"name": "Kai Kogashiwa", "car": "Toyota MR2 SW20", "track": "Irohazaka", "skill": 8},
    "tomoyuki": {"name": "Tomoyuki Tachi", "car": "Mitsubishi Lancer Evolution V", "track": "Shomaru", "skill": 7},
    "daiki": {"name": "Daiki Ninomiya", "car": "Honda Civic EK9 Type R", "track": "Shomaru", "skill": 7},
    "hiroya": {"name": "Hiroya Okuyama", "car": "Nissan Silvia S15", "track": "Nagao", "skill": 7},
    "go": {"name": "Go Hojo", "car": "Honda NSX NA1", "track": "Tsuchisaka", "skill": 9},
    "kozo": {"name": "Kozo Hoshino", "car": "Suzuki Cappuccino EA11R", "track": "Tsuchisaka", "skill": 8},
    "wataru": {"name": "Wataru Akiyama", "car": "Toyota AE86 Levin", "track": "Shomaru", "skill": 7},
    "shinji": {"name": "Shinji Inui", "car": "Mazda Eunos Roadster NA6CE", "track": "Nagao", "skill": 9},
    "ryo": {"name": "Ryo Shinigami", "car": "Mitsubishi Lancer Evolution VI", "track": "Tsuchisaka", "skill": 9}
}

def akina():
    pass
def akagi():
    pass
def myogi():
    pass
def usui():
    pass
def nikko():
    pass
def shomaru():
    pass
def tsuchisaka():
    pass
def nagao():
    pass

def combat(turns, enemy, player, cars):
    order = 0 if random.choice(0, 1) == 0 else order = 1
    print(f"You have engaged in combat with {enemy["name"]}")
    while turns > 0:
        if order == 0:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Defend inside (di)\nDefend outside (do)\nGive position (g)\nFeint inside (fi)\nFeint outside (fo)\nFeint give (fg)")
            act = input("What would you like to do? ")
            while act != "di" and act != "do" and act != "g" and act != "fi" and act != "fo" and act != "fg":
                act = input("That was not a valid action. What would you like to do? ")
            # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
        else:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Take inside (ti)\nTake outside (to)\nStay (s)\nFeint inside (fi)\nFeint outside (fo)\nFeint stay (fs)")
            act = input("What would you like to do? ")
            while act != "ti" and act != "to" and act != "s" and act != "fi" and act != "fo" and act != "fs":
                act = input("That was not a valid action. What would you like to do? ")
            # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
        if cars[enemy["car"]]["hp"] > cars[player["car"]]["hp"] and order == 1:
            valid = True
        elif cars[enemy["car"]]["hp"] < cars[player["car"]]["hp"] and order == 0:
            valid = True
        else:
            valid = False
        if valid == True and order == 1 and input("Would you like to try and overtake in the straightaway (y/n) ") == "y" or valid == True and order == 0 and random.choice(0, 1) == 0:
            if order == 0:
                opt = input("You're approaching the straightaway with your opponent threatening an overtake... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Defend left (l)\nDefend right (r)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...
            else:
                opt = input("You're approaching the straightaway... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Take left (l)\nTake right (r)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                # DOOOOO THE OUTCOME PLEAAASE I DONT WANT TO RIGHT NOW...

def main(player, cars, enemies):
    pass

main(player, cars, enemies)