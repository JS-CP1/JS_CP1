import random

player = {
    "wins": 0,
    "money": 500000,
    "car": "",
    "skill": 7.5,
    "titles": [],
    "tire_age": 0
}
cars = {
    "ae86": {"name": "Toyota AE86 Trueno", "tires": 40000, "grip": 5, "hp": 130, "price": 120000},
    "fd_rx7": {"name": "Mazda RX-7 FD3S", "tires": 100000, "grip": 8, "hp": 200, "price": 350000},
    "nismo": {"name": "nismo", "tires": 500000, "grip": 25, "hp": 600, "price": 1500000},
    "ae85": {"name": "Toyota AE85 Levin", "tires": 60000, "grip": 4, "hp": 85, "price": 90000},
    "supra_rz": {"name": "Toyota Supra RZ", "tires": 150000, "grip": 9, "hp": 320, "price": 420000},
    "mr2_sw20": {"name": "Toyota MR2 SW20", "tires": 90000, "grip": 7, "hp": 200, "price": 220000},
    "celica_st204": {"name": "Toyota Celica ST204", "tires": 95000, "grip": 7, "hp": 170, "price": 180000},
    "fc_rx7": {"name": "Mazda RX-7 FC3S", "tires": 90000, "grip": 7, "hp": 180, "price": 200000},
    "roadster_na6ce": {"name": "Mazda Eunos Roadster NA6CE", "tires": 70000, "grip": 6, "hp": 115, "price": 140000},
    "eg6_civic": {"name": "Honda Civic SiR-II EG6", "tires": 85000, "grip": 7, "hp": 170, "price": 170000},
    "ek9_civic": {"name": "Honda Civic Type R EK9", "tires": 95000, "grip": 8, "hp": 185, "price": 240000},
    "nsx_na1": {"name": "Honda NSX NA1", "tires": 150000, "grip": 10, "hp": 280, "price": 600000},
    "crx_ef8": {"name": "Honda CR-X EF8", "tires": 80000, "grip": 6, "hp": 150, "price": 150000},
    "silvia_s13": {"name": "Nissan Silvia S13", "tires": 80000, "grip": 7, "hp": 160, "price": 160000},
    "silvia_s14": {"name": "Nissan Silvia S14", "tires": 85000, "grip": 7, "hp": 200, "price": 190000},
    "silvia_s15": {"name": "Nissan Silvia S15", "tires": 95000, "grip": 8, "hp": 250, "price": 260000},
    "skyline_r32": {"name": "Nissan Skyline GT-R R32", "tires": 140000, "grip": 10, "hp": 280, "price": 550000},
    "skyline_r34": {"name": "Nissan Skyline GT-R R34", "tires": 160000, "grip": 10, "hp": 320, "price": 750000},
    "180sx": {"name": "Nissan 180SX", "tires": 85000, "grip": 7, "hp": 170, "price": 170000},
    "sil80": {"name": "Nissan SilEighty", "tires": 80000, "grip": 7, "hp": 175, "price": 175000},
    "evo3": {"name": "Mitsubishi Lancer Evolution III", "tires": 130000, "grip": 9, "hp": 270, "price": 300000},
    "evo4": {"name": "Mitsubishi Lancer Evolution IV", "tires": 135000, "grip": 9, "hp": 280, "price": 320000},
    "evo5": {"name": "Mitsubishi Lancer Evolution V", "tires": 140000, "grip": 9, "hp": 280, "price": 340000},
    "evo6": {"name": "Mitsubishi Lancer Evolution VI", "tires": 145000, "grip": 9, "hp": 280, "price": 360000},
    "impreza": {"name": "Subaru Impreza WRX STi GC8", "tires": 120000, "grip": 9, "hp": 280, "price": 300000},
    "cappuccino": {"name": "Suzuki Cappuccino EA11R", "tires": 60000, "grip": 6, "hp": 65, "price": 70000},
    "benz_190e": {"name": "Mercedes-Benz 190E W201", "tires": 110000, "grip": 8, "hp": 170, "price": 230000},
    "porsche_911": {"name": "Porsche 911 Turbo 964", "tires": 160000, "grip": 10, "hp": 320, "price": 900000},
    "alfa_romeo_4c": {"name": "Alfa Romeo 4C", "tires": 140000, "grip": 9, "hp": 240, "price": 380000}
}
enemies = {
    "takahashi": {"name": "Ryosuke Takahashi", "car": "fc_rx7", "track": "Akagi", "skill": 9, "beaten": 0},
    "impact_blue": {"name": "Mako Sato & Sayuki", "car": "sil80", "track": "Usui Pass", "skill": 6, "beaten": 0},
    "bunta": {"name": "Bunta Fujiwara", "car": "impreza", "track": "Akina", "skill": 12, "beaten": 0},
    "takeshi": {"name": "Takeshi Nakazato", "car": "skyline_r32", "track": "Myogi", "skill": 8, "beaten": 0},
    "shingo": {"name": "Shingo Shoji", "car": "eg6_civic", "track": "Myogi", "skill": 6, "beaten": 0},
    "kyoichi": {"name": "Kyoichi Sudo", "car": "evo3", "track": "Akagi", "skill": 8, "beaten": 0},
    "seiji": {"name": "Seiji Iwaki", "car": "evo4", "track": "Akina", "skill": 7, "beaten": 0},
    "hideo": {"name": "Hideo Minagawa", "car": "supra_rz", "track": "Nikko", "skill": 7, "beaten": 0},
    "kai": {"name": "Kai Kogashiwa", "car": "mr2_sw20", "track": "Nikko", "skill": 8, "beaten": 0},
    "tomoyuki": {"name": "Tomoyuki Tachi", "car": "evo5", "track": "Shomaru", "skill": 7, "beaten": 0},
    "daiki": {"name": "Daiki Ninomiya", "car": "ek9_civic", "track": "Shomaru", "skill": 7, "beaten": 0},
    "hiroya": {"name": "Hiroya Okuyama", "car": "silvia_s15", "track": "Nagao", "skill": 7, "beaten": 0},
    "go": {"name": "Go Hojo", "car": "nsx_na1", "track": "Tsuchisaka", "skill": 9, "beaten": 0},
    "kozo": {"name": "Kozo Hoshino", "car": "cappuccino", "track": "Tsuchisaka", "skill": 8, "beaten": 0},
    "wataru": {"name": "Wataru Akiyama", "car": "ae86", "track": "Shomaru", "skill": 7, "beaten": 0},
    "shinji": {"name": "Shinji Inui", "car": "roadster_na6ce", "track": "Nagao", "skill": 9, "beaten": 0},
    "ryo": {"name": "Ryo Shinigami", "car": "evo6", "track": "Tsuchisaka", "skill": 9, "beaten": 0}
}

def akina(player, cars, enemies):
    akinas = []
    for e in enemies:
        if "Akina" == enemies[e]["track"]:
            akinas.append(e)
    enemy = random.choice(akinas)
    turns = 30
    combat(turns, enemy, player, cars, enemies)
def akagi(player, cars, enemies):
    akagis = []
    for e in enemies:
        if "Akagi" in enemies[e]["track"]:
            akagis.append(e)
    enemy = random.choice(akagis)
    turns = 50
    combat(turns, enemy, player, cars, enemies)
def myogi(player, cars, enemies):
    myogis = []
    for e in enemies:
        if "Myogi" in enemies[e]["track"]:
            myogis.append(e)
    enemy = random.choice(myogis)
    turns = 25
    combat(turns, enemy, player, cars, enemies)
def usui(player, cars, enemies):
    usuis = []
    for e in enemies:
        if "Usui" in enemies[e]["track"]:
            usuis.append(e)
    enemy = random.choice(usuis)
    turns = 60
    combat(turns, enemy, player, cars, enemies)
def nikko(player, cars, enemies):
    nikkos = []
    for e in enemies:
        if "Nikko" in enemies[e]["track"]:
            nikkos.append(e)
    enemy = random.choice(nikkos)
    turns = 25
    combat(turns, enemy, player, cars, enemies)
def shomaru(player, cars, enemies):
    shomarus = []
    for e in enemies:
        if "Shomaru" in enemies[e]["track"]:
            shomarus.append(e)
    enemy = random.choice(shomarus)
    turns = 25
    combat(turns, enemy, player, cars, enemies)
def tsuchisaka(player, cars, enemies):
    tsuchisakas = []
    for e in enemies:
        if "Tsuchisaka" in enemies[e]["track"]:
            tsuchisakas.append(e)
    enemy = random.choice(tsuchisakas)
    turns = 25
    combat(turns, enemy, player, cars, enemies)
def nagao(player, cars, enemies):
    nagaos = []
    for e in enemies:
        if "Nagao" in enemies[e]["track"]:
            nagaos.append(e)
    enemy = random.choice(nagaos)
    turns = 25
    combat(turns, enemy, player, cars, enemies)

def combat(turns, enemy, player, cars, enemies):
    if random.choice([0, 1]) == 0:
        order = 0
    else:
        order = 1
    print(f"You have engaged in combat with {enemies[enemy]["name"]}")
    while turns > 0:
        if order == 0:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Defend inside (di)\nDefend outside (do)\nGive position (g)")
            act = input("What would you like to do? ")
            while act != "di" and act != "do" and act != "g":
                act = input("That was not a valid action. What would you like to do? ")
            botpass = (random.random() * 5) + (cars[enemies[enemy]["car"]]["hp"] / 100) + (cars[enemies[enemy]["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5)
            if act == "di":
                if botpass > 8.5:
                    print("Your opponent passes you...")
                    order = 1
                else:
                    print("You successfully fend off your opponent...")
            elif act == "do":
                if botpass > 8:
                    print("Your opponent passes you...")
                    order = 1
                else:
                    print("You successfully fend off your opponent...")
            else:
                print("You give away your position to your opponent...")
        else:
            opt = input("You're approaching the turn... Would you like to review your options? (y/n) ")
            if opt == "yes" or opt == "y":
                print("Take inside (ti)\nTake outside (to)\nStay (s)")
            act = input("What would you like to do? ")
            while act != "ti" and act != "to" and act != "s":
                act = input("That was not a valid action. What would you like to do? ")
            playerpass = (random.random() * 5) + (cars[player["car"]]["hp"] / 100) + (cars[player["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - player["tire_age"]
            if act == "ti":
                if playerpass > 8.5:
                    print("You succesfully pass your opponent...")
                    order = 1
                else:
                    print("You failed to pass your opponent...")
            elif act == "to":
                if playerpass > 8:
                    print("You succesfully pass your opponent...")
                    order = 1
                else:
                    print("You failed to pass your opponent...")
            else:
                print("You give away your position to your opponent...")
        if cars[enemies[enemy]["car"]]["hp"] > cars[player["car"]]["hp"] and order == 1:
            valid = True
        elif cars[enemies[enemy]["car"]]["hp"] < cars[player["car"]]["hp"] and order == 0:
            valid = True
        else:
            valid = False
        if valid == True and order == 1 and input("Would you like to try and overtake in the straightaway (y/n) ") == "y" or valid == True and order == 0 and random.choice(0, 1) == 0:
            if order == 0:
                opt = input("You're approaching the straightaway with your opponent threatening an overtake... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Defend left (l)\nDefend right (r)\nGive position (g)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                botpass = (random.random() * 5) + (cars[enemies[enemy]["car"]]["hp"] / 100) + (cars[enemies[enemy]["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5)
                if act == "l" or act == "r":
                    if botpass > 10:
                        print("Your opponent passes you...")
                        order = 1
                    else:
                        print("You successfully fend off your opponent...")
                else:
                    print("You give away your position to your opponent...")
            else:
                opt = input("You're approaching the straightaway... Would you like to review your options? (y/n) ")
                if opt == "yes" or opt == "y":
                    print("Take left (l)\nTake right (r)")
                act = input("What would you like to do? ")
                while act != "l" and act != "r":
                    act = input("That was not a valid action. What would you like to do? ")
                playerpass = (random.random() * 5) + (cars[player["car"]]["hp"] / 100) + (cars[player["car"]]["grip"] / 15) + (enemies[enemy]["skill"] / 5) - player["tire_age"]
                if act == "ti":
                    if playerpass > 8:
                        print("You succesfully pass your opponent...")
                        order = 1
                    else:
                        print("You failed to pass your opponent...")
                elif act == "to":
                    if playerpass > 8:
                        print("You succesfully pass your opponent...")
                        order = 1
                    else:
                        print("You failed to pass your opponent...")
                else:
                    print("You give away your position to your opponent...")
        turns += 1
    if order == 0:
        print("Congratulations! You won the battle! Your skill increases and you gain 25000 yen.")
        player["money"] += 25000
        player["wins"] += 1
        player["skill"] += .5
        enemies[enemy]["beaten"] += 1
    else:
        print("welp. you lost...")
    main(player, cars, enemies)

def main(player, cars, enemies):
    akina_wins = 0
    akagi_wins = 0
    myogi_wins = 0
    nikko_wins = 0
    shomaru_wins = 0
    tsuchi_wins = 0
    nagao_wins = 0
    for e in enemies:
        if e["track"] == "Usui" and e["beaten"] > 0:
            player["titles"].append("Usui Pass")
        if e["track"] == "Akina" and e["beaten"] > 0:
            akina_wins += 1
        if akina_wins >= 2:
            player["titles"].append("Mt. Akina")
        if e["track"] == "Akagi" and e["beaten"] > 0:
            akagi_wins += 1
        if akagi_wins >= 2:
            player["titles"].append("Mt. Akagi")
        if e["track"] == "Myogi" and e["beaten"] > 0:
            myogi_wins += 1
        if myogi_wins >= 2:
            player["titles"].append("Mt. Myogi")
        if e["track"] == "Nikko" and e["beaten"] > 0:
            nikko_wins += 1
        if nikko_wins >= 2:
            player["titles"].append("Mt. Nikko")
        if e["track"] == "Shomaru" and e["beaten"] > 0:
            shomaru_wins += 1
        if shomaru_wins >= 3:
            player["titles"].append("Mt. Shomaru")
        if e["track"] == "Tsuchisaka" and e["beaten"] > 0:
            tsuchi_wins += 1
        if tsuchi_wins >= 3:
            player["titles"].append("Mt. Tsuchisaka")
        if e["track"] == "Nagao" and e["beaten"] > 0:
            nagao_wins += 1
        if nagao_wins >= 2:
            player["titles"].append("Mt. Nagao")
    if len(player["titles"]) >= 3:
        keep = input("You won! Would you like to keep playing? (yes/no)")
        if keep == "no":
            exit()
    act = input(f"Would you like to buy new tires or a new car? Your money: {player['money']} (tires/car/no)")
    if act == "tires":
        print(f"You spent {cars[player["car"]]["tires"]}")
    elif act == "car":
        print(f"These are your options for cars:")
        for car in cars:
            print(f" {car}; {car["price"]}")
        new_car = input("What car would you like? (make sure it's exactly the same) ").strip().lower()
        while new_car not in cars or player["money"] < cars[new_car]["price"]:
            if new_car not in cars:
                new_car = input("That was not a valid car. Choose again: ").strip().lower()
            else:
                new_car = input("You do not have enough money for that car. Choose again: ")
        print(f"You bought a {new_car}")
        player["car"] = new_car
    goto = input("Where would you like to go to?\n Your options are: akina, akagi, myogi, usui, nikko, shomaru, tsuchisaka, and nagao\n ")
    while goto != "akina" and goto != "akagi" and goto != "myogi" and goto != "usui" and goto != "nikko" and goto != "shomaru" and goto != "tsuchisaka" and goto != "nagao":
        goto = input("That's not a valid location, where would you like to go to?\n Your options are: akina, akagi, myogi, usui, nikko, shomaru, tsuchisaka, and nagao\n ")
    if goto == "akina":
        akina(player, cars, enemies)
    elif goto == "akagi":
        akagi(player, cars, enemies)
    elif goto == "myogi":
        myogi(player, cars, enemies)
    elif goto == "usui":
        usui(player, cars, enemies)
    elif goto == "nikko":
        nikko(player, cars, enemies)
    elif goto == "shomaru":
        shomaru(player, cars, enemies)
    elif goto == "tsuchisaka":
        tsuchisaka(player, cars, enemies)
    elif goto == "nagao":
        nagao(player, cars, enemies)
    else:
        main(player, cars, enemies)

print(f"These are your options for cars:")
for car in cars:
    print(f" {car}")
new_car = input("What car would you like? (make sure it's exactly the same) ").strip().lower()
while new_car not in cars:
    new_car = input("That was not a valid car. Choose again: ").strip().lower()
print(f"You bought a {new_car}")
player["car"] = new_car
main(player, cars, enemies)