import random
import time
import sys
#made by 6c11!!!! 

player = {
    "name": "",
    "health": 100,
    "max_health": 100,
    "max_mp": 50, 
    "mp": 50, 
    "attack": 10,
    "defense": 5,
    "gold": 0,
    "exp": 0,
    "lv": 1,
    "lue": 100, 
    "stats": 0, 
    "fs": 1, 
    "ss": 0, 
    "ts": 0, 
    "potion": 3,
    "inventory": []
}
#made by 6c11!!!! 

ran  = 0

#怪物資料
enemies = [
    {"name": "slime", "health": 30, "attack": 10, "defense": 0, "gold": 3, "exp": 10, "lv": 1},
    {"name": "spider", "health": 75, "attack": 15, "defense": 5, "gold": 6, "exp": 25, "lv": 3},
    {"name": "Dragon", "health": 100, "attack": 25, "defense": 10, "gold": 20, "exp": 100, "lv": 5}
]
boss = [
    {"name": "lv10.boss-spider_king", "health": 3000, "attack":40, "gold":60,
  "exp": 300} 
] 
#商店物品
shop_items = [
    {"name": "攻擊力永久提升藥水", "attack_bonus": 3, "price": 30},
    {"name": "防玉力永久提升藥水", "defense_bonus": 1, "price": 20},
    {"name": "生命掛牌(可無限配戴)", "max_health_bonus": 50, "price": 10},
    {"name": "刀光劍影(技能) ", "skill2": 1, "price": 50}, 
    {"name": "恢復藥水 ", "hpadd": 40, "mpadd": 20, "price": 3}, 
        {"name": "nope", "attack_bonus": 9999999999999999999,"defense_bonus": 99999999999, "price": -50} 
]

def print_separator():
    print("=" * 30)
#玩家
def print_player_status():
    print_separator()
    print(f"玩家狀態:")
    print(f"名字: {player['name']}")
    print(f"等級: {player['lv']}") 
    print(f"經驗值: {player['exp']}" + "/" + str(player["lue"]))
    print(f"生命值: {player['health']}" + "/" + str(player['max_health'] ) )
    print(f"攻擊力: {player['attack']}")
    print(f"防禦力: {player['defense']}")
    print(f"金幣: {player['gold']}")
    print("背包:")
    if len(player['inventory']) > 0:
        for index, item in enumerate(player['inventory'], start=1):
            print(f"{index}. {item['name']}")
    else:
        print("背包是空的")
    print_separator()
#怪物創建
def create_enemy():
    enemy = random.choice(enemies)
    return enemy.copy()
#物品使用
def use_item(item_index):
    if 0 <= item_index < len(player['inventory']):
        item = player['inventory'][item_index]
        if 'attack_bonus' in item:
            player['attack'] += item['attack_bonus']
            print(f"你使用了{item['name']}，攻擊力增加了{item['attack_bonus']}點！")
        if 'defense_bonus' in item:
            player['defense'] += item['defense_bonus']
            print(f"你使用了{item['name']}，防禦力增加了{item['defense_bonus']}點！")
        if 'max_health_bonus' in item:
            player['max_health'] = player['max_health'] + item['max_health_bonus']
            print(f"你使用了{item['name']}，生命值增加了{item['max_health_bonus']}點！")
        if 'skill2' in item:
            player['ss'] += 1
            print(f"你學習了{item['name']}！")
        if 'hpadd' in item:
            player["potion"] += 1
            print(f"你裝備了{item['name']}！(可在戰鬥中使用)")
        del player['inventory'][item_index]
    else:
        print("請輸入有效的物品編號。")

def start_game():
    print("welcome to到文字RPG遊戲！")
    player["name"] = input("請enter你的名字: ")
    print_player_status()
 #幹什麼列表
  
    while True:
        print("choose一個動作:")
        print("0. 商店") 
        print("1. 冒險")
        print("2. 休息")
        print("3. 顯示背包")
        print("4. alt f4")
        print("5. 你的資訊") 
        print("6. 加點面板") 
        choice = input("你的選擇: ")
        
        
        #商店資料
        if choice == "0":
            print("購買清單:")
            for index, item in enumerate(shop_items, start=1):
                print(f"{index}. {item['name']} (價格: {item['price']}金幣)")

            purchase_choice = input("選擇你要購買的物品編號 (按Enter返回): ")
            if purchase_choice.isdigit():
                item_index = int(purchase_choice) - 1
                if 0 <= item_index < len(shop_items):
                    selected_item = shop_items[item_index]
                    if player['gold'] >= selected_item['price']:
                        player['gold'] -= selected_item['price']
                        player['inventory'].append(selected_item)
                        print(f"你buy了{selected_item['name']}!")
                    else:
                        print("你的金幣不足，無法buy該物品。")
                else:
                    print("請enter有效的物品編號。")
            else:
                print("請enter有效的物品編號。")

        elif choice == "1":
            enemy = create_enemy()
            print(f"你遇到了一個lv{enemy['lv']}.{enemy['name']}！")
            print_separator()
            while enemy["health"] > 0 and player["health"] > 0:
                print(f"lv{enemy['lv']}.{enemy['name']}生命值: {enemy['health']}")
                print("你的生命值:" + str(player['health']) + "/" + str(player['max_health']))
                print("你的mp:" + str(player['mp']) + "/" + str(player['max_mp'])) 
                print_separator()
                player['mp'] = min (player["max_mp"], player['mp'] + 5)
                print("選擇一個動作:")
                print("1. 攻擊")
                print("2. 逃跑(skill issue(jk))")
                print("3. 使用技能1:劍擊") 
                if player["ss"] >= 1:
                    print("4. 使用技能2:刀光劍影") 
                print("5. 使用恢復藥水(現在有" + str(player['potion']) + "瓶) ") 
                print_separator()
                action = input("你的選擇: ")

                if action == "1":
                    ran = random.randint(0,9)
                    if ran == 0:
                        print("爆擊!!!") 
                        player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3)*2) - enemy["defense"]) 
                        enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                        enemy["health"] -= player_damage
                        player["health"] -= enemy_damage
                        print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                        print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                        print_separator()
                    else:
                        player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3)) - enemy["defense"]) 
                        enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                        enemy["health"] -= player_damage
                        player["health"] -= enemy_damage
                        print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                        print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                        print_separator() 
                        
                    if enemy["health"] <= 0:
                        print(f"你擊敗了{enemy['name']}！Ezzzz")
                        player["gold"] += enemy["gold"]
                        player["exp"] += enemy["exp"] 
                        if player["exp"] >=  player["lue"]:
                             player["exp"] = player["exp"] - player["lue"]
                             player["lv"] = player["lv"] + 1
                             player["lue"] += 10
                             player["stats"] = player["stats"] + 3
                             print("lv uppppp uppppp uppppppppp!! ") 
                             for enemy in enemies:
                                 enemy["attack"] = int(round(enemy["attack"] * 1.1))
                                 enemy["lv"] += 1
                                 enemy["defense"] = int(round(enemy["defense"] * 1.05))
                                 enemy["health"] = int(round(enemy["health"] * 1.1))
                                 enemy["exp"] += 5
                                 enemy["gold"] = int(round(enemy["gold"] * 1.1)) 
                                 
                        print("你現在有錢錢" + str(player["gold"]) + "$" ) 
                        print_separator()
                        break

                    if player["health"] <= 0:
                        print("你die了！遊戲alt f4。")
                        sys.exit()

                elif action == "2":
                    print("你逃跑了！ LLL skill issue(jk) ")
                    print_separator()
                    break
                    
                if action == "3":
                    if player["mp"] >= 25:
                        player["mp"] -= 25
                        print("你使用了技能 劍擊(-25mp) ") 
                        ran = random.randint(0,4)
                        if ran == 0:
                            print("爆擊!!! ") 
                            player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3) * 3) - enemy["defense"]) 
                            enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                            enemy["health"] -= player_damage
                            player["health"] -= enemy_damage
                            print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                            print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                        else:
                            player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3) * 1.5) - enemy["defense"]) 
                            enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                            enemy["health"] -= player_damage
                            player["health"] -= enemy_damage
                            print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                            print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                        if enemy["health"] <= 0:
                            print(f"你擊敗了{enemy['name']}！Ezzzz")
                            player["gold"] += enemy["gold"]
                            player["exp"] += enemy["exp"] 
                            if player["exp"] >=  player["lue"]:
                                 player["exp"] = player["exp"] - player["lue"]
                                 player["lv"] = player["lv"] + 1
                                 player["lue"] += 10
                                 player["stats"] = player["stats"] + 3
                                 print("lv uppppp uppppp uppppppppp!! ") 
                                 for enemy in enemies:
                                     enemy["attack"] = int(round(enemy["attack"] * 1.1))
                                     enemy["lv"] += 1
                                     enemy["defense"] = int(round(enemy["defense"] * 1.05))
  #made by 6c11!!!!     
                                     enemy["health"] = int(round(enemy["health"] * 1.1))
                                     enemy["exp"] += 5
                                     enemy["gold"] = int(round(enemy["gold"] * 1.1)) 
                            print("你現在有錢錢" + str(player["gold"]) + "$" ) 
                            print_separator()
                            break

                        if player["health"] <= 0:
                            print("你die了！遊戲alt f4。")
                            sys.exit()
                            print_separator()
                    else:
                        print(" u dont have mp lol") 
                if action == "4":
                    if player["ss"] >= 1:
                        if player["mp"] > 40:
                            player["mp"] -= 40
                            print("你使用了技能 劍影(-40mp) ") 
                            time.sleep(1)
                            print("\ ")
                            time.sleep(0.4)
                            print("/")
                            time.sleep(0.4)
                            print("\ ")
                            time.sleep(0.4)
                            print("/")
                            time.sleep(0.7)
                            print("X")
                            time.sleep(1.5)
                            ran = random.randint(0,2)
                            if ran == 0:
                                print("爆擊!!!") 
                                player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3) * 8) - enemy["defense"]) 
                                enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                                enemy["health"] -= player_damage
                                player["health"] -= enemy_damage
                                print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                                print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                            else:
                                player_damage = max(0, (random.randint(player["attack"] - 3,player["attack"] + 3) * 5) - enemy["defense"]) 
                                enemy_damage = max(0, (random.randint(enemy["attack"] - 5,enemy["attack"] + 6)) - player["defense"]) 
                                enemy["health"] -= player_damage
                                player["health"] -= enemy_damage
                                print(f"你對{enemy['name']}造成了{player_damage}點傷害！")
                                print(f"{enemy['name']}對你造成了{enemy_damage}點傷害！")
                            if enemy["health"] <= 0:
                                print(f"你擊敗了{enemy['name']}！Ezzzz")
                                player["gold"] += enemy["gold"]
                                player["exp"] += enemy["exp"] 
                                if player["exp"] >=  player["lue"]:
                                     player["exp"] = player["exp"] - player["lue"]
                                     player["lv"] = player["lv"] + 1
                                     player["lue"] += 10
                                     player["stats"] = player["stats"] + 3
                                     print("lv uppppp uppppp uppppppppp!! ") 
                                     for enemy in enemies:
                                         enemy["attack"] = int(round(enemy["attack"] * 1.1))
                                         enemy["lv"] += 1
                                         enemy["defense"] = int(round(enemy["defense"] * 1.05))
                                         enemy["health"] = int(round(enemy["health"] * 1.1))
                                         enemy["exp"] += 5
                                         enemy["gold"] = int(round(enemy["gold"] * 1.1)) 
                                print("你現在有錢錢" + str(player["gold"]) + "$" ) 
                                print_separator()
                                break
                                
                            if player["health"] <= 0:
                                print("你die了！遊戲alt f4。")
                                sys.exit()
                        else:
                            print('u dont have mp lol') 
                            print_separator()
                if action == "5":
                    if player["potion"] >= 1:
                        player["potion"] -= 1
                        player['health'] = min (player["max_health"], player['health'] + 40)
                        player['mp'] = min (player["max_mp"], player['mp'] + 20)
                        print("你+了40點hp and 20mp！")
                        print_separator() 
                    else:
                        print("u don't have any potion lol") 
        elif choice == "2":
            player['health'] = min (player["max_health"], player['health'] + 40)
            player['mp'] = min (player["max_mp"], player['mp'] + 20)
            print("你+了40點hp and 20mp！")
        
        elif choice == "5":
            print_player_status()
        
        elif choice == "4":
            print("alt f4。")
            print("made by 6c11 not other!!!") 
            sys.exit()
#made by 6c11!!!! 

        elif choice == "3":
            print("use物品:")
            print_player_status()
            item_choice = input("choose你要使用的物品編號 (按Enter back): ")
            if item_choice.isdigit():
                item_index = int(item_choice) - 1
                use_item(item_index)
            else:
                print("請enter有效的物品編號。")

        else:
            print("請enter有效的選項。")
        if choice == "6":
            print("u have" + str(player["stats"]) + "stats") 
            print("1. 攻擊力+2(now:" + str(player["attack"]) + ")") 
            print("2. 防禦力+0.3(now:" + str(player["defense"]) + ")") 
            print("3. 生命值+10(now:" + str(player["max_health"]) + ")") 
            print("4. mp+5(now:" + str(player["max_mp"]) + ")") 
            print("5. x10") 
            stats_choice  = input("enter number to up stats:") 
            if stats_choice == "1":
                if player["stats"] > 0:
                    player["stats"] = player["stats"] - 1
                    player["attack"] = player["attack"] + 2
                else:
                    print("u have no stats pooorr") 
                    print_separator()
                    
            if stats_choice == "2":
                if player["stats"] > 0:
                    player["stats"] = player["stats"] - 1
                    player["defense"] = player["defense"] + 0.3
                else:
                    print("u have no stats pooorr")           
                    print_separator()
                    
            if stats_choice == "3":
                if player["stats"] > 0:
                    player["stats"] = player["stats"] - 1
                    player["max_health"] = player["max_health"] + 10
                else:
                    print("u have no stats pooorr")
            if stats_choice == "4":
                if player["stats"] > 0:
                    player["stats"] = player["stats"] - 1
                    player["max_mp"] = player["max_mp"] + 5
                else:
                    print("u have no stats pooorr")  
            if stats_choice == "5":
                print("u have" + str(player["stats"]) + "stats") 
                print("1. 攻擊力+20(now:" + str(player["attack"]) + ")") 
                print("2. 防禦力+3(now:" + str(player["defense"]) + ")") 
                print("3. 生命值+100(now:" + str(player["max_health"]) + ")") 
                print("4. mp+50(now:" + str(player["max_mp"]) + ")") 
                x10stats_choice = input("enter number to up 10x stats:") 
                if x10stats_choice == "1":
                    if player["stats"] > 9:
                        player["stats"] = player["stats"] - 10
                        player["attack"] = player["attack"] + 20
                    else:
                         print("u have no stats pooorr") 
                         print_separator()
                    
                if x10stats_choice == "2":
                    if player["stats"] > 9:
                         player["stats"] = player["stats"] - 10
                         player["defense"] = player["defense"] + 3
                    else:
                        print("u have no stats pooorr")           
                        print_separator()
                    
                if x10stats_choice == "3":
                    if player["stats"] > 9:
                         player["stats"] = player["stats"] - 10
                         player["max_health"] = player["max_health"] + 100
                    else:
                         print("u have no stats pooorr")
#made by 6c11!!!! 
                if stats_choice == "4":
                    if player["stats"] > 9:
                        player["stats"] = player["stats"] - 10
                        player["max_mp"] = player["max_mp"] + 50
                    else:
                        print("u have no stats pooorr") 
            
                else:
                     print("pls write right numbers") 
                     print_separator() 
start_game()  



#made by 6c11!!!! 
