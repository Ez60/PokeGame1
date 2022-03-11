"""
Author: Aaron Mui
Game based on Pokemon games.
"""

import termcolor

class grid:

    def __init__(self, grid_dimensions = [8, 8]):
        self.grid_dimensions = grid_dimensions
        self.grid_use = []
        self.grid_use2 = []

    def __str__(self):
        return "Create and update grid"

    def create_grid(self):
        initial_grid_instance = self.grid_use
        initial_grid_instance2 = self.grid_use2

        for row in range(self.grid_dimensions[0]):
            initial_grid_instance.append([])
            initial_grid_instance2.append([])
            for column in range(self.grid_dimensions[1]):
                initial_grid_instance[-1].append([])
                initial_grid_instance2[-1].append([])

    def set_grid_values(self):
        #1 = grass
        #2 = road
        #3 = tree
        #4 = pokemon
        #5 = pokemon
        #6 = item
        #7 = big rock
        #8 = CPU-trainer
        #9 = player
        for row in range(self.grid_dimensions[0]):
            for column in range(self.grid_dimensions[1]):
                self.grid_use[row][column] = 1
                self.grid_use2[row][column] = 1

        for column in range(self.grid_dimensions[1]):
            self.grid_use[column][0] = 3
            self.grid_use[column][7] = 3
            self.grid_use2[column][0] = 3
            self.grid_use2[column][7] = 3

        for row in range(self.grid_dimensions[0]):
            for column in range(3, 5):
                self.grid_use[row][column] = 2
                self.grid_use2[row][column] = 2

        self.grid_use[7][0] = 2
        self.grid_use[7][1] = 2
        self.grid_use[7][2] = 2
        self.grid_use[6][2] = 2
        self.grid_use[1][2] = 7
        self.grid_use[4][5] = 7
        self.grid_use[6][6] = 7
        self.grid_use[0][1] = 5
        self.grid_use[5][5] = 4
        self.grid_use[2][1] = 6
        self.grid_use[1][6] = 6
        self.grid_use[7][5] = 6
        self.grid_use[4][1] = 8
        self.grid_use2[7][0] = 2
        self.grid_use2[7][1] = 2
        self.grid_use2[7][2] = 2
        self.grid_use2[6][2] = 2
        self.grid_use2[1][2] = 7
        self.grid_use2[4][5] = 7
        self.grid_use2[6][6] = 7
        self.grid_use[7][0] = 9

    def display_grid(self):
        for row in range(self.grid_dimensions[0]):
            print(self.grid_use[row])

    def player_move_update(self, player_move_x, player_move_y, player_pos_x, player_pos_y, player_grid_tile):
        self.grid_use[player_move_x][player_move_y] = player_grid_tile
        self.grid_use[player_pos_x][player_pos_y] = self.grid_use2[player_pos_x][player_pos_y]

class player:

    def __init__(self, money, pokemon_list, player_bag, name, gender, nature):
        self.money = money
        self.pokemon_list = pokemon_list
        self.player_bag = player_bag
        self.name = name
        self.gender = gender
        self.nature = nature
        self.pos_x = 7
        self.pos_y = 0
        self.position = [self.pos_x, self.pos_y]
        self.grid_tile_curr = 9

    def position_update(self, move_pos_x, move_pos_y):
        self.pos_x = move_pos_x
        self.pos_y = move_pos_y
        self.position = [self.pos_x, self.pos_y]

    def add_money(self, money_add):
        self.money = self.money + money_add

    def add_pokemon(self, pokemon_add):
        self.pokemon_list.append(pokemon_add)

    def add_item(self, item_add):
        self.player_bag.append(item_add)

class cpu_trainer(player):

    def __init__(self, money, pokemon_list, cpu_bag, name, gender, nature, fun_fact, money_give, pokemon_give):
        player.__init__(self, money, pokemon_list, cpu_bag, name, gender, nature)
        self.fun_fact = fun_fact
        self.money_give = money_give
        self.pokemon_give = pokemon_give

    def money_lose_give(self):
        print(f"Gives {self.money_give}")
        self.money = self.money - self.money_give

    def pokemon_lose_give(self):
        for poke_give in self.pokemon_give:
            print(f"{poke_give.name} {poke_give.level}")
        for poke_give in self.pokemon_give:
            self.pokemon_give.remove(poke_give)

class pokemon:

    def __init__(self, poke_id, species, name, attack_list, hp, level):
        self.id = poke_id
        self.species = species
        self.name = name
        self.attack_list = attack_list
        self.hp = hp
        self.full_hp = hp
        self.level = level

def player_CPU_battle(player1, CPU_trainer1):

    battle_end = False
    while battle_end == False:
        print(f"{CPU_trainer1.name} wants to battle")
        print(f"{CPU_trainer1.name} chooses {CPU_trainer1.pokemon_list[0].name} {CPU_trainer1.pokemon_list[0].hp} {CPU_trainer1.pokemon_list[0].level}")
        print("Choose a pokemon to fight")
        for poke_in_bag1 in player1.pokemon_list:
            print(f"{poke_in_bag1.name} {poke_in_bag1.hp} {poke_in_bag1.level}")
        poke_to_fight_valid = False
        while poke_to_fight_valid == False:
            poke_to_fight = input("Go: ").lower()
            for i in range(len(player1.pokemon_list)):
                if poke_to_fight == player1.pokemon_list[i].name.lower():
                    pokemon_fight = player1.pokemon_list[i]
                    poke_to_fight_valid = True
        print(f"{pokemon_fight.name} {pokemon_fight.hp} {pokemon_fight.level}")
        while CPU_trainer1.pokemon_list[0].hp > 0:
            print("Choose an attack")
            for atk in pokemon_fight.attack_list:
                print(atk)
            attack_use = input()
            print(f"{pokemon_fight.name} uses {attack_use}!")
            CPU_trainer1.pokemon_list[0].hp = CPU_trainer1.pokemon_list[0].hp - pokemon_fight.level * 5
            if CPU_trainer1.pokemon_list[0].hp <= 0:
                break
            print(f"{CPU_trainer1.pokemon_list[0].name} {CPU_trainer1.pokemon_list[0].hp}hp")
            print(f"{CPU_trainer1.pokemon_list[0].name} uses {CPU_trainer1.pokemon_list[0].attack_list[0]}")
            pokemon_fight.hp = pokemon_fight.hp - CPU_trainer1.pokemon_list[0].level * 5
            print(f"{pokemon_fight.name} {pokemon_fight.hp}hp")
        print(f"{CPU_trainer1.pokemon_list[0].name} can no longer fight")
        print(f"{player1.name} uses potion on {pokemon_fight.name}!")
        pokemon_fight.hp = pokemon_fight.full_hp
        player1.player_bag.remove("potion")
        print(f"{pokemon_fight.name} {pokemon_fight.hp}hp")
        print(f"{CPU_trainer1.name} says go {CPU_trainer1.pokemon_list[1].name}!")
        print(f"{CPU_trainer1.pokemon_list[1].name} {CPU_trainer1.pokemon_list[1].hp} {CPU_trainer1.pokemon_list[1].level}")
        print("Choose a pokemon to fight")
        for poke_in_bag2 in player1.pokemon_list:
            print(f"{poke_in_bag2.name} {poke_in_bag2.hp} {poke_in_bag2.level}")
        poke_to_fight_valid = False
        while poke_to_fight_valid == False:
            poke_to_fight = input("Go: ").lower()
            for i in range(len(player1.pokemon_list)):
                if poke_to_fight == player1.pokemon_list[i].name.lower():
                    pokemon_fight = player1.pokemon_list[i]
                    poke_to_fight_valid = True
        print(f"{pokemon_fight.name} {pokemon_fight.hp} {pokemon_fight.level}")
        while CPU_trainer1.pokemon_list[1].hp > 0:
            print("Choose an attack")
            for atk in pokemon_fight.attack_list:
                print(atk)
            attack_use = input()
            print(f"{pokemon_fight.name} uses {attack_use}!")
            CPU_trainer1.pokemon_list[1].hp = CPU_trainer1.pokemon_list[1].hp - pokemon_fight.level * 5
            if CPU_trainer1.pokemon_list[1].hp <= 0:
                break
            print(f"{CPU_trainer1.pokemon_list[1].name} {CPU_trainer1.pokemon_list[1].hp}hp")
            print(f"{CPU_trainer1.pokemon_list[1].name} uses {CPU_trainer1.pokemon_list[1].attack_list[0]}")
            pokemon_fight.hp = pokemon_fight.hp - CPU_trainer1.pokemon_list[1].level * 5
            print(f"{pokemon_fight.name} {pokemon_fight.hp}hp")
        print(f"{CPU_trainer1.pokemon_list[1].name} can no longer fight")
        print(f"{CPU_trainer1.name} says you are capable. Here take these.")
        CPU_trainer1.money_lose_give()
        CPU_trainer1.pokemon_lose_give()
        battle_end = True

def player_poke_battle(player1, pokemon1):

    battle_end = False
    while battle_end == False:
        print(f"{pokemon1.name} appears")
        print(f"{pokemon1.name} {pokemon1.hp} {pokemon1.level}")
        print("Choose a pokemon to fight")
        for poke_in_bag in player1.pokemon_list:
            print(f"{poke_in_bag.name} {poke_in_bag.hp} {poke_in_bag.level}")
        poke_to_fight_valid = False
        while poke_to_fight_valid == False:
            poke_to_fight = input("Go: ").lower()
            for i in range(len(player1.pokemon_list)):
                if poke_to_fight == player1.pokemon_list[i].name.lower():
                    pokemon_fight = player1.pokemon_list[i]
                    poke_to_fight_valid = True
        print(f"{pokemon_fight.name} {pokemon_fight.hp} {pokemon_fight.level}")
        while pokemon1.hp > 75:
            print("Choose an attack")
            for atk in pokemon_fight.attack_list:
                print(atk)
            attack_use = input()
            print(f"{pokemon_fight.name} uses {attack_use}!")
            pokemon1.hp = pokemon1.hp - pokemon_fight.level * 5
            print(f"{pokemon1.name} {pokemon1.hp}hp")
            print(f"{pokemon1.name} uses {pokemon1.attack_list[0]}")
            pokemon_fight.hp = pokemon_fight.hp - pokemon1.level * 5
            print(f"{pokemon_fight.name} {pokemon_fight.hp}hp")
        print(f"{pokemon1.name} seems to give up")
        print(f"Throw pokeball at {pokemon1.name}. Caught {pokemon1.name}!")
        battle_end = True

def game_start():
    char_name1 = input("Welcome. Enter a char name: ")
    gender1 = input("What is your gender? M, F, or Other: ")
    nature1 = input("What is your nature? Kind, Mean, Funny or DK for Don't Know ")
    pokemon1 = pokemon(1, "water_pokemon", "water_pokemon1", ["water_attack1", "water_attack2"], 250, 5)
    pokemon2 = pokemon(2, "electric_pokemon", "electric_pokemon1", ["electric_attack1", "electric_attack2"], 274, 7)
    pokemon3 = pokemon(3, "earth_pokemon", "earth_pokemon1", ["earth_attack1", "earth_attack2"], 283, 8)
    pokemon_choices = [pokemon1, pokemon2, pokemon3]
    for poke_choice in pokemon_choices:
        print(f"pokemon{poke_choice.id} {poke_choice.name}")
    player1 = player(15000, [], ["potion", "potion", "full_restore"], char_name1, gender1, nature1)
    pokemon_choose_valid = False
    while pokemon_choose_valid == False:
        pokemon_choose = input("Choose a pokemon: pokemon1, pokemon2 or pokemon3 ").lower()
        if pokemon_choose == "pokemon1":
            player1.add_pokemon(pokemon1)
            pokemon_choose_valid = True
        elif pokemon_choose == "pokemon2":
            player1.add_pokemon(pokemon2)
            pokemon_choose_valid = True
        elif pokemon_choose == "pokemon3":
            player1.add_pokemon(pokemon3)
            pokemon_choose_valid = True
    game_end = False
    while game_end == False:
        print("You are at Pokeland, enter A to move left, D to move right, W to move up, S to move down, ")
        print("Bag to see Bag or Quit to quit.")
        termcolor.cprint("Map info: 1 = grass, 2 = road, 3 = tree", "grey")
        termcolor.cprint("4 = pokemon, 5 = pokemon, 6 = item, 7 = big rock, 8 = CPU-trainer 9 = player", "grey")
        grid1.display_grid()
        pokemon4 = pokemon(4, "flying_pokemon", "flying_pokemon1", ["flying_kick1", "flying_punch1"], 237, 5)
        pokemon5 = pokemon(5, "insect_pokemon", "insect_pokemon1", ["sting1", "tackle1"], 379, 17)
        pokemon6 = pokemon(6, "ghost_pokemon", "ghost_pokemon1", ["ghost_choke1", "invisible_kick1"], 248, 4)
        pokemon7 = pokemon(7, "insect_pokemon", "insect_pokemon2", ["claw_slice1", "claw_stab1"], 137, 8)
        cpu_trainer1 = cpu_trainer(4500, [pokemon6, pokemon7], ["potion", "potion"], "CPU1", "M", "Mean",
                                   "CPU1 owns a lot of pokemon and wants to give a few away", 2000, [pokemon6, pokemon7])
        move_input = input().lower()
        if move_input == "a":
            if player1.pos_y - 1 < 0:
                print("Can not move there")
            elif grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 1 or grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 2:
                grid1.player_move_update(player1.pos_x, player1.pos_y - 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y - 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 4:
                player_poke_battle(player1, pokemon4)
                player1.add_pokemon(pokemon4)
                print("Your pokemons seem hurt. Take a rest")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                grid1.player_move_update(player1.pos_x, player1.pos_y - 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y - 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 5:
                print("Pokemon seems to want to join you")
                print("Throw pokeball at pokemon")
                player1.add_pokemon(pokemon5)
                print("Caught pokemon!")
                grid1.player_move_update(player1.pos_x, player1.pos_y - 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y - 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 6:
                termcolor.cprint("Found a potion", "blue")
                player1.add_item("potion")
                grid1.player_move_update(player1.pos_x, player1.pos_y - 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y - 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y - 1] == 8:
                player_CPU_battle(player1, cpu_trainer1)
                player1.add_money(int(2000))
                player1.add_pokemon(pokemon6)
                player1.add_pokemon(pokemon7)
                print(f"{cpu_trainer1.name} walks away")
                termcolor.cprint(cpu_trainer1.fun_fact, "grey")
                print("Your pokemons seem hurt badly. Use full_restore")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                player1.player_bag.remove("full_restore")
                grid1.player_move_update(player1.pos_x, player1.pos_y - 1, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y - 1)
            else:
                print("Can not move there")
        elif move_input == "d":
            if player1.pos_y + 1 > 7:
                print("Can not move there")
            elif grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 1 or grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 2:
                grid1.player_move_update(player1.pos_x, player1.pos_y + 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y + 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 4:
                player_poke_battle(player1, pokemon4)
                player1.add_pokemon(pokemon4)
                print("Your pokemons seem hurt. Take a rest")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                grid1.player_move_update(player1.pos_x, player1.pos_y + 1, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y + 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 5:
                print("Pokemon seems to want to join you")
                print("Throw pokeball at pokemon")
                player1.add_pokemon(pokemon5)
                print("Caught pokemon!")
                grid1.player_move_update(player1.pos_x, player1.pos_y + 1, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y + 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 6:
                termcolor.cprint("Found a potion", "blue")
                player1.add_item("potion")
                grid1.player_move_update(player1.pos_x, player1.pos_y + 1, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y + 1)
            elif grid1.grid_use[player1.pos_x][player1.pos_y + 1] == 8:
                player_CPU_battle(player1, cpu_trainer1)
                player1.add_money(int(2000))
                player1.add_pokemon(pokemon6)
                player1.add_pokemon(pokemon7)
                print(f"{cpu_trainer1.name} walks away")
                termcolor.cprint(cpu_trainer1.fun_fact, "grey")
                print("Your pokemons seem hurt badly. Use full_restore")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                player1.player_bag.remove("full_restore")
                grid1.player_move_update(player1.pos_x, player1.pos_y + 1, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x, player1.pos_y + 1)
            else:
                print("Can not move there")
        elif move_input == "w":
            if player1.pos_x - 1 < 0:
                print("Can not move there")
            elif grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 1 or grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 2:
                grid1.player_move_update(player1.pos_x - 1, player1.pos_y, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x - 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 4:
                player_poke_battle(player1, pokemon4)
                player1.add_pokemon(pokemon4)
                print("Your pokemons seem hurt. Take a rest")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                grid1.player_move_update(player1.pos_x - 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x - 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 5:
                print("Pokemon seems to want to join you")
                print("Throw pokeball at pokemon")
                player1.add_pokemon(pokemon5)
                print("Caught pokemon!")
                grid1.player_move_update(player1.pos_x - 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x - 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 6:
                termcolor.cprint("Found a potion", "blue")
                player1.add_item("potion")
                grid1.player_move_update(player1.pos_x - 1, player1.pos_y, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x - 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x - 1][player1.pos_y] == 8:
                player_CPU_battle(player1, cpu_trainer1)
                player1.add_money(int(2000))
                player1.add_pokemon(pokemon6)
                player1.add_pokemon(pokemon7)
                print(f"{cpu_trainer1.name} walks away")
                termcolor.cprint(cpu_trainer1.fun_fact, "grey")
                print("Your pokemons seem hurt badly. Use full_restore")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                player1.player_bag.remove("full_restore")
                grid1.player_move_update(player1.pos_x - 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x - 1, player1.pos_y)
            else:
                print("Can not move there")
        elif move_input == "s":
            if player1.pos_x + 1 > 7:
                print("Can not move there")
            elif grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 1 or grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 2:
                grid1.player_move_update(player1.pos_x + 1, player1.pos_y, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x + 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 4:
                player_poke_battle(player1, pokemon4)
                player1.add_pokemon(pokemon4)
                print("Your pokemons seem hurt. Take a rest")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                grid1.player_move_update(player1.pos_x + 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x + 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 5:
                print("Pokemon seems to want to join you")
                print("Throw pokeball at pokemon")
                player1.add_pokemon(pokemon5)
                print("Caught pokemon!")
                grid1.player_move_update(player1.pos_x + 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x + 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 6:
                termcolor.cprint("Found a potion", "blue")
                player1.add_item("potion")
                grid1.player_move_update(player1.pos_x + 1, player1.pos_y, player1.pos_x, player1.pos_y, player1.grid_tile_curr)
                player1.position_update(player1.pos_x + 1, player1.pos_y)
            elif grid1.grid_use[player1.pos_x + 1][player1.pos_y] == 8:
                player_CPU_battle(player1, cpu_trainer1)
                player1.add_money(int(2000))
                player1.add_pokemon(pokemon6)
                player1.add_pokemon(pokemon7)
                print(f"{cpu_trainer1.name} walks away")
                termcolor.cprint(cpu_trainer1.fun_fact, "grey")
                print("Your pokemons seem hurt badly. Use full_restore")
                for poke_in_bag in player1.pokemon_list:
                    poke_in_bag.hp = poke_in_bag.full_hp
                    print(f"{poke_in_bag.name} {poke_in_bag.hp}hp")
                player1.player_bag.remove("full_restore")
                grid1.player_move_update(player1.pos_x + 1, player1.pos_y, player1.pos_x, player1.pos_y,
                                         player1.grid_tile_curr)
                player1.position_update(player1.pos_x + 1, player1.pos_y)
            else:
                print("Can not move there")
        elif move_input == "bag":
            for bag_item in player1.player_bag:
                print(bag_item)
            for poke_in_bag in player1.pokemon_list:
                print(f"Pokeball: {poke_in_bag.name}")
        elif move_input == "quit":
            game_end = True
        else:
            print("Can not move there")
        if len(player1.pokemon_list) >= 4:
            print("You win, congrats")
            game_end = True

if __name__ == '__main__':
    grid1 = grid()
    grid1.create_grid()
    grid1.set_grid_values()
    game_start()


