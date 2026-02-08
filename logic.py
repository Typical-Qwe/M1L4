from datetime import datetime, timedelta
from random import randint, choice
import requests

from random import randint
import requests

class Pokemon:
    pokemons = {}
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.power = randint(10,20)
        self.hp = randint(100,200)

        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']["front_shiny"])
        else:
            return "https://img.freepik.com/premium-photo/girl-pikachu_551707-69798.jpg?semt=ais_hybrid&w=740"

    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    def info(self):
        return f"Имя твоего покеомона: {self.name}, сила: {self.power} здоровье: {self.hp}"

    def show_img(self):
        return self.img

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time-delta_time}"

class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase=20)

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "
    def feed(self):
        return super().feed(feed_interval=10)

# class Pokemon:
#     pokemons = {}
#     legendary_ids = [144, 145, 146, 150, 151]

#     def __init__(self, pokemon_trainer):
#         self.pokemon_trainer = pokemon_trainer
#         self.pokemon_number = self.roll_pokemon()

#         self.name = self.get_name()
#         self.img = self.get_img()

#         self.level = 1
#         self.xp = 0
#         self.feed_count = 0
#         self.achievements = []

#         if self.pokemon_number in Pokemon.legendary_ids:
#             self.level += 2
#             self.achievements.append("Легендарный покемон")

#         Pokemon.pokemons[pokemon_trainer] = self

#     def roll_pokemon(self):
#         if randint(1, 100) == 1:
#             return choice(Pokemon.legendary_ids)
#         return randint(1, 1000)

#     def feed(self):
#         xp_gain = randint(10, 25)
#         self.xp += xp_gain
#         self.feed_count += 1
#         self.check_level_up()
#         self.check_achievements()
#         return xp_gain

#     def check_level_up(self):
#         while self.xp >= self.level * 50:
#             self.xp -= self.level * 50
#             self.level += 1

#     def check_achievements(self):
#         if self.level >= 10 and "10 уровень" not in self.achievements:
#             self.achievements.append("10 уровень")
#         if self.feed_count >= 20 and "Заботливый тренер" not in self.achievements:
#             self.achievements.append("Заботливый тренер")

#     def get_img(self):
#         url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.json()['sprites']['other']['official-artwork']['front_default']
#         return None

#     def get_name(self):
#         url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.json()['name']
#         return "unknown"
#     def info(self):
#         return {
#             "name": self.name,
#             "level": self.level,
#             "xp": self.xp,
#             "achievements": self.achievements
#         }
#     def show_img(self):
#         return self.img