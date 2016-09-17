from math import ceil, floor
from random import randint
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


normal = "normal"
fire = "fire"
water = "water"
grass = "grass"
electric = "electric"
ice = "ice"
fighting = "fighting"
poison = "poison"
ground = "ground"
flying = "flying"
psychic = "psychic"
bug = "bug"
rock = "rock"
ghost = "ghost"
dragon = "dragon"
dark = "dark"
steel = "steel"
fairy = "fairy"
none = "none"

types = [normal, fire, water, grass, electric, ice, fighting, poison, ground,
         flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy, none]

attack = 0
defense = 1
stamina = 2

pokes = {"MissingNo.": [0, 1, 0],
         "Bulbasaur": [126, 126, 90],
         "Ivysaur": [156, 158, 120],
         "Venusaur": [198, 200, 160],
         "Charmander": [128, 108, 78],
         "Charmeleon": [160, 140, 116],
         "Charizard": [212, 182, 156],
         "Squirtle": [112, 142, 88],
         "Wartortle": [144, 176, 118],
         "Blastoise": [186, 222, 158],
         "Caterpie": [62, 66, 90],
         "Metapod": [56, 86, 100],
         "Butterfree": [144, 144, 120],
         "Weedle": [68, 64, 80],
         "Kakuna": [62, 82, 90],
         "Beedrill": [144, 130, 130],
         "Pidgey": [94, 90, 80],
         "Pidgeotto": [126, 122, 126],
         "Pidgeot": [170, 166, 166],
         "Rattata": [92, 86, 60],
         "Raticate": [146, 150, 110],
         "Spearow": [102, 78, 80],
         "Fearow": [168, 146, 130],
         "Ekans": [112, 112, 70],
         "Arbok": [166, 166, 120],
         "Pikachu": [124, 108, 70],
         "Raichu": [200, 154, 120],
         "Sandshrew": [90, 114, 100],
         "Sandslash": [150, 172, 150],
         "Nidoran female": [100, 104, 110],
         "Nidorina": [132, 136, 140],
         "Nidoqueen": [184, 190, 180],
         "Nidoran male": [110, 94, 92],
         "Nidorino": [142, 128, 122],
         "Nidoking": [204, 170, 162],
         "Clefairy": [116, 124, 140],
         "Clefable": [178, 178, 190],
         "Vulpix": [106, 118, 76],
         "Ninetales": [176, 194, 146],
         "Jigglypuff": [98, 54, 230],
         "Wigglytuff": [168, 108, 280],
         "Zubat": [88, 90, 80],
         "Golbat": [164, 164, 150],
         "Oddish": [134, 130, 90],
         "Gloom": [162, 158, 120],
         "Vileplume": [202, 190, 150],
         "Paras": [122, 120, 70],
         "Parasect": [162, 170, 120],
         "Venonat": [108, 118, 120],
         "Venomoth": [172, 154, 140],
         "Diglett": [108, 86, 20],
         "Dugtrio": [148, 140, 70],
         "Meowth": [104, 94, 80],
         "Persian": [156, 146, 130],
         "Psyduck": [132, 112, 100],
         "Golduck": [194, 176, 160],
         "Mankey": [122, 96, 80],
         "Primeape": [178, 150, 130],
         "Growlithe": [156, 110, 110],
         "Arcanine": [230, 180, 180],
         "Poliwag": [108, 98, 80],
         "Poliwhirl": [132, 132, 130],
         "Poliwrath": [180, 202, 180],
         "Abra": [110, 76, 50],
         "Kadabra": [150, 112, 80],
         "Alakazam": [186, 152, 110],
         "Machop": [118, 96, 140],
         "Machoke": [154, 144, 160],
         "Machamp": [198, 180, 180],
         "Bellsprout": [158, 78, 100],
         "Weepinbell": [190, 110, 130],
         "Victreebel": [222, 152, 160],
         "Tentacool": [106, 136, 80],
         "Tentacruel": [170, 196, 160],
         "Geodude": [106, 118, 80],
         "Graveler": [142, 156, 110],
         "Golem": [176, 198, 160],
         "Ponyta": [168, 138, 100],
         "Rapidash": [200, 170, 130],
         "Slowpoke": [110, 110, 180],
         "Slowbro": [184, 198, 190],
         "Magnemite": [128, 138, 50],
         "Magneton": [186, 180, 100],
         "Farfetch'd": [138, 132, 104],
         "Doduo": [126, 96, 70],
         "Dodrio": [182, 150, 120],
         "Seel": [104, 138, 130],
         "Dewgong": [156, 192, 180],
         "Grimer": [124, 110, 160],
         "Muk": [180, 188, 210],
         "Shellder": [120, 112, 60],
         "Cloyster": [196, 196, 100],
         "Gastly": [136, 82, 60],
         "Haunter": [172, 118, 90],
         "Gengar": [204, 156, 120],
         "Onix": [90, 186, 70],
         "Drowzee": [104, 140, 120],
         "Hypno": [162, 196, 170],
         "Krabby": [116, 110, 60],
         "Kingler": [178, 168, 110],
         "Voltorb": [102, 124, 80],
         "Electrode": [150, 174, 120],
         "Exeggcute": [110, 132, 120],
         "Exeggutor": [232, 164, 190],
         "Cubone": [102, 150, 100],
         "Marowak": [140, 202, 120],
         "Hitmonlee": [148, 172, 100],
         "Hitmonchan": [138, 204, 100],
         "Lickitung": [126, 160, 180],
         "Koffing": [136, 142, 80],
         "Weezing": [190, 198, 130],
         "Rhyhorn": [110, 116, 160],
         "Rhydon": [166, 160, 210],
         "Chansey": [40, 60, 500],
         "Tangela": [164, 152, 130],
         "Kangaskhan": [142, 178, 210],
         "Horsea": [122, 100, 60],
         "Seadra": [176, 150, 110],
         "Goldeen": [112, 126, 90],
         "Seaking": [172, 160, 160],
         "Staryu": [130, 128, 60],
         "Starmie": [194, 192, 120],
         "Mr. Mime": [154, 196, 80],
         "Scyther": [176, 180, 140],
         "Jynx": [172, 134, 130],
         "Electabuzz": [198, 160, 130],
         "Magmar": [214, 158, 130],
         "Pinsir": [184, 186, 130],
         "Tauros": [148, 184, 150],
         "Magikarp": [42, 84, 40],
         "Gyarados": [192, 196, 190],
         "Lapras": [186, 190, 260],
         "Ditto": [110, 110, 96],
         "Eevee": [114, 128, 110],
         "Vaporeon": [186, 168, 260],
         "Jolteon": [192, 174, 130],
         "Flareon": [238, 178, 130],
         "Porygon": [156, 158, 130],
         "Omanyte": [132, 160, 70],
         "Omastar": [180, 202, 140],
         "Kabuto": [148, 142, 60],
         "Kabutops": [190, 190, 120],
         "Aerodactyl": [182, 162, 160],
         "Snorlax": [180, 180, 320],
         "Articuno": [198, 242, 180],
         "Zapdos": [232, 194, 180],
         "Moltres": [242, 194, 180],
         "Dratini": [128, 110, 82],
         "Dragonair": [170, 152, 122],
         "Dragonite": [250, 212, 182],
         "Mewtwo": [284, 202, 212],
         "Mew": [220, 220, 200],
         "Chikorita": [],
         "Bayleef": [],
         "Meganium": [],
         "Cyndaquil": [],
         "Quilava": [],
         "Typhlosion": [],
         "Totodile": [],
         "Croconaw": [],
         "Feraligatr": [],
         "Sentret": [],
         "Furret": [],
         "Hoothoot": [],
         "Noctowl": [],
         "Ledyba": [],
         "Ledian": [],
         "Spinarak": [],
         "Ariados": [],
         "Crobat": [],
         "Chinchou": [],
         "Lanturn": [],
         "Pichu": [],
         "Cleffa": [],
         "Igglybuff": [],
         "Togepi": [],
         "Togetic": [],
         "Natu": [],
         "Xatu": [],
         "Mareep": [],
         "Flaaffy": [],
         "Ampharos": [],
         "Bellossom": [],
         "Marill": [],
         "Azumarill": [],
         "Sudowoodo": [],
         "Politoed": [],
         "Hoppip": [],
         "Skiploom": [],
         "Jumpluff": [],
         "Aipom": [],
         "Sunkern": [],
         "Sunflora": [],
         "Yanma": [],
         "Wooper": [],
         "Quagsire": [],
         "Espeon": [],
         "Umbreon": [],
         "Murkrow": [],
         "Slowking": [],
         "Misdreavus": [],
         "Unown": [],
         "Wobbuffet": [],
         "Girafarig": [],
         "Pineco": [],
         "Forretress": [],
         "Dunsparce": [],
         "Gligar": [],
         "Steelix": [],
         "Snubbull": [],
         "Granbull": [],
         "Qwilfish": [],
         "Scizor": [],
         "Shuckle": [],
         "Heracross": [],
         "Sneasel": [],
         "Teddiursa": [],
         "Ursaring": [],
         "Slugma": [],
         "Magcargo": [],
         "Swinub": [],
         "Piloswine": [],
         "Corsola": [],
         "Remoraid": [],
         "Octillery": [],
         "Delibird": [],
         "Mantine": [],
         "Skarmory": [],
         "Houndour": [],
         "Houndoom": [],
         "Kingdra": [],
         "Phanpy": [],
         "Donphan": [],
         "Porygon2": [],
         "Stantler": [],
         "Smeargle": [],
         "Tyrogue": [],
         "Hitmontop": [],
         "Smoochum": [],
         "Elekid": [],
         "Magby": [],
         "Miltank": [],
         "Blissey": [],
         "Raikou": [],
         "Entei": [],
         "Suicune": [],
         "Larvitar": [],
         "Pupitar": [],
         "Tyranitar": [],
         "Lugia": [],
         "Ho-oh": [],
         "Celebi": []}


class Type:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.moves = []
        self.very_strong = []
        self.strong = []
        self.weak = []
        self.very_weak = []
        self.super_eff = []
        self.not_very_eff = []

NORMAL = Type(normal)
FIRE = Type(fire)
WATER = Type(water)
GRASS = Type(grass)
ELECTRIC = Type(electric)
ICE = Type(ice)
FIGHTING = Type(fighting)
POISON = Type(poison)
GROUND = Type(ground)
FLYING = Type(flying)
PSYCHIC = Type(psychic)
BUG = Type(bug)
ROCK = Type(rock)
GHOST = Type(ghost)
DRAGON = Type(dragon)
DARK = Type(dark)
STEEL = Type(steel)
FAIRY = Type(fairy)
NONE = Type(none)

NORMAL.strong = [ghost]
NORMAL.weak = [fighting]
FIRE.strong = [grass, ice, bug, steel, fire, fairy]
FIRE.weak = [ground, water, rock]
WATER.strong = [fire, water, ice, steel]
WATER.weak = [electric, grass]
GRASS.strong = [water, ground, grass, electric]
GRASS.weak = [ice, fire, poison, flying, bug]
ELECTRIC.strong = [flying, electric, steel]
ELECTRIC.weak = [ground]
ICE.strong = [ice]
ICE.weak = [fighting, rock, fire, steel]
FIGHTING.strong = [rock, dark, bug]
FIGHTING.weak = [flying, psychic, fairy]
POISON.strong = [grass, fairy, fighting, poison, bug]
POISON.weak = [psychic, ground]
GROUND.strong = [electric, poison, rock]
GROUND.weak = [water, ice, grass]
FLYING.strong = [grass, fighting, bug, ground]
FLYING.weak = [ice, electric, rock]
PSYCHIC.strong = [fighting, psychic]
PSYCHIC.weak = [bug, ghost, dark]
BUG.strong = [grass, fighting, ground]
BUG.weak = [rock, fire, flying]
ROCK.strong = [fire, flying, normal, poison]
ROCK.weak = [water, grass, fighting, ground, steel]
GHOST.strong = [normal, fighting, poison, bug]
GHOST.weak = [ghost, dark]
DRAGON.strong = [fire, water, grass, electric]
DRAGON.weak = [ice, dragon, fairy]
DARK.strong = [psychic, ghost, dark]
DARK.weak = [bug, fighting, fairy]
STEEL.strong = [ice, rock, fairy, normal, grass, poison, flying, psychic, bug, dragon, steel]
STEEL.weak = [fighting, ground, fire]
FAIRY.strong = [fighting, dragon, dark, bug]
FAIRY.weak = [poison, steel]

# the following code was used to create the super_eff and not_very_eff lists for all types
"""for pokemon_type in TYPES:
    for attack in pokemon_type.strong:
        for pogo_type in TYPES:
            if pogo_type.name == attack:
                pogo_type.not_very_eff.append(pokemon_type.name)

for pokemon_type in TYPES:
    for attack in pokemon_type.weak:
        for pogo_type in TYPES:
            if pogo_type.name == attack:
                pogo_type.super_eff.append(pokemon_type.name)

for pogo_type in TYPES:
    print pogo_type.name.upper(), ".super_eff =", pogo_type.super_eff
    print pogo_type.name.upper(), ".not_very_eff =", pogo_type.not_very_eff"""

NORMAL.super_eff = []
NORMAL.not_very_eff = ['rock', 'ghost', 'steel']
FIRE.super_eff = ['grass', 'ice', 'bug', 'steel']
FIRE.not_very_eff = ['fire', 'water', 'rock', 'dragon']
WATER.super_eff = ['fire', 'ground', 'rock']
WATER.not_very_eff = ['water', 'grass', 'dragon']
GRASS.super_eff = ['water', 'ground', 'rock']
GRASS.not_very_eff = ['fire', 'grass', 'poison', 'flying', 'bug', 'dragon', 'steel']
ELECTRIC.super_eff = ['water', 'flying']
ELECTRIC.not_very_eff = ['grass', 'electric', 'ground', 'dragon']
ICE.super_eff = ['grass', 'ground', 'flying', 'dragon']
ICE.not_very_eff = ['fire', 'water', 'ice', 'steel']
FIGHTING.super_eff = ['normal', 'ice', 'rock', 'dark', 'steel']
FIGHTING.not_very_eff = ['poison', 'flying', 'psychic', 'bug', 'ghost', 'fairy']
POISON.super_eff = ['grass', 'fairy']
POISON.not_very_eff = ['poison', 'ground', 'rock', 'ghost', 'steel']
GROUND.super_eff = ['fire', 'electric', 'poison', 'rock', 'steel']
GROUND.not_very_eff = ['grass', 'flying', 'bug']
FLYING.super_eff = ['grass', 'fighting', 'bug']
FLYING.not_very_eff = ['electric', 'rock', 'steel']
PSYCHIC.super_eff = ['fighting', 'poison']
PSYCHIC.not_very_eff = ['psychic', 'dark', 'steel']
BUG.super_eff = ['grass', 'psychic', 'dark']
BUG.not_very_eff = ['fire', 'fighting', 'poison', 'flying', 'ghost', 'steel', 'fairy']
ROCK.super_eff = ['fire', 'ice', 'flying', 'bug']
ROCK.not_very_eff = ['fighting', 'ground', 'steel']
GHOST.super_eff = ['psychic', 'ghost']
GHOST.not_very_eff = ['normal', 'dark']
DRAGON.super_eff = ['dragon']
DRAGON.not_very_eff = ['steel', 'fairy']
DARK.super_eff = ['psychic', 'ghost']
DARK.not_very_eff = ['fighting', 'dark', 'fairy']
STEEL.super_eff = ['ice', 'rock', 'fairy']
STEEL.not_very_eff = ['fire', 'water', 'electric', 'steel']
FAIRY.super_eff = ['fighting', 'dragon', 'dark']
FAIRY.not_very_eff = ['fire', 'poison', 'steel']

NORMAL.pokemon = ["Snorlax", "Wigglytuff", "Pidgeot", "Kangaskhan", "Tauros", "Dodrio", "Fearow", "Porygon", "Persian",
                  "Lickitung", "Raticate", "Farfetch'd", "Pidgeotto", "Eevee", "Ditto", "Jigglypuff", "Doduo", "Meowth",
                  "Spearow", "Pidgey", "Chansey", "Rattata", "Sentret", "Furret", "Hoothoot", "Noctowl", "Igglybuff",
                  "Aipom", "Girafarig", "Dunsparce", "Teddiursa", "Ursaring", "Porygon2", "Stantler", "Smeargle",
                  "Miltank", "Blissey"]
FIRE.pokemon = ["Moltres", "Arcanine", "Flareon", "Charizard", "Magmar", "Rapidash", "Ninetales", "Charmeleon",
                "Ponyta", "Growlithe", "Charmander", "Vulpix", "Cyndaquil", "Quilava", "Typhlosion", "Slugma",
                "Magcargo", "Houndour", "Houndoom", "Magby", "Entei", "Ho-oh"]
WATER.pokemon = ["Lapras", "Vaporeon", "Gyarados", "Slowbro", "Blastoise", "Poliwrath", "Golduck", "Omastar",
                 "Tentacruel", "Starmie", "Dewgong", "Kabutops", "Cloyster", "Seaking", "Kingler", "Seadra",
                 "Wartortle", "Poliwhirl", "Slowpoke", "Omanyte", "Psyduck", "Seel", "Kabuto", "Squirtle", "Goldeen",
                 "Staryu", "Tentacool", "Shellder", "Poliwag", "Horsea", "Krabby", "Magikarp", "Totodile", "Croconaw",
                 "Feraligatr", "Chinchou", "Lanturn", "Marill", "Azumarill", "Politoed", "Wooper", "Quagsire",
                 "Slowking", "Qwilfish", "Corsola", "Remoraid", "Octillery", "Mantine", "Kingdra", "Suicune"]
GRASS.pokemon = ["Exeggutor", "Venusaur", "Victreebel", "Vileplume", "Parasect", "Tangela", "Weepinbell", "Gloom",
                 "Ivysaur", "Oddish", "Bellsprout", "Exeggcute", "Bulbasaur", "Paras", "Chikorita", "Bayleef",
                 "Meganium", "Bellossom", "Hoppip", "Skiploom", "Jumpluff", "Sunkern", "Sunflora", "Celebi"]
ELECTRIC.pokemon = ["Zapdos", "Jolteon", "Electabuzz", "Raichu", "Magneton", "Electrode", "Magnemite", "Pikachu",
                    "Voltorb", "Chinchou", "Lanturn", "Pichu", "Mareep", "Flaaffy", "Ampharos", "Elekid", "Raikou"]
ICE.pokemon = ["Lapras", "Articuno", "Dewgong", "Cloyster", "Jynx", "Sneasel", "Swinub", "Piloswine", "Delibird",
               "Smoochum"]
FIGHTING.pokemon = ["Machamp", "Poliwrath", "Primeape", "Machoke", "Hitmonchan", "Hitmonlee", "Machop", "Mankey",
                    "Heracross", "Tyrogue", "Hitmontop"]
POISON.pokemon = ["Muk", "Venusaur", "Victreebel", "Vileplume", "Nidoqueen", "Nidoking", "Weezing", "Tentacruel",
                  "Gengar", "Golbat", "Venomoth", "Arbok", "Weepinbell", "Gloom", "Ivysaur", "Beedrill", "Nidorina",
                  "Haunter", "Nidorino", "Grimer", "Koffing", "Oddish", "Bellsprout", "Bulbasaur", "Venonat",
                  "Tentacool", "Nidoran female", "Nidoran male", "Ekans", "Gastly", "Zubat", "Kakuna", "Weedle",
                  "Spinarak", "Ariados", "Crobat", "Qwilfish"]
GROUND.pokemon = ["Nidoqueen", "Nidoking", "Golem", "Rhydon", "Sandslash", "Marowak", "Graveler", "Rhyhorn", "Dugtrio",
                  "Cubone", "Onix", "Geodude", "Sandshrew", "Diglett", "Wooper", "Quagsire", "Gligar", "Steelix",
                  "Swinub", "Piloswine", "Phanpy", "Donphan", "Larvitar", "Pupitar"]
FLYING.pokemon = ["Dragonite", "Moltres", "Zapdos", "Articuno", "Gyarados", "Charizard", "Aerodactyl", "Pidgeot",
                  "Scyther", "Golbat", "Dodrio", "Fearow", "Butterfree", "Farfetch'd", "Pidgeotto", "Doduo", "Spearow",
                  "Pidgey", "Zubat", "Hoothoot", "Noctowl", "Ledyba", "Ledian", "Crobat", "Togetic", "Natu", "Xatu",
                  "Hoppip", "Skiploom", "Jumpluff", "Yanma", "Murkrow", "Gligar", "Delibird", "Mantine", "Skarmory",
                  "Lugia", "Ho-oh"]
PSYCHIC.pokemon = ["Mewtwo", "Mew", "Exeggutor", "Slowbro", "Hypno", "Starmie", "Alakazam", "Jynx", "Mr. Mime",
                   "Slowpoke", "Kadabra", "Exeggcute", "Drowzee", "Abra", "Natu", "Xatu", "Espeon", "Slowking", "Unown",
                   "Wobbuffet", "Girafarig", "Smoochum", "Lugia", "Celebi"]
BUG.pokemon = ["Pinsir", "Scyther", "Venomoth", "Parasect", "Butterfree", "Beedrill", "Venonat", "Paras", "Kakuna",
               "Metapod", "Weedle", "Caterpie", "Ledyba", "Ledian", "Spinarak", "Ariados", "Yanma", "Pineco",
               "Forretress", "Scizor", "Shuckle", "Heracross"]
ROCK.pokemon = ["Golem", "Rhydon", "Omastar", "Aerodactyl", "Kabutops", "Graveler", "Rhyhorn", "Omanyte", "Kabuto",
                "Onix", "Geodude", "Sudowoodo", "Shuckle", "Magcargo", "Corsola", "Larvitar", "Pupitar", "Tyranitar"]
GHOST.pokemon = ["Gengar", "Haunter", "Gastly", "Misdreavus"]
DRAGON.pokemon = ["Dragonite", "Dragonair", "Dratini", "Kingdra"]
DARK.pokemon = ["Umbreon", "Murkrow", "Sneasel", "Houndour", "Houndoom", "Tyranitar"]
STEEL.pokemon = ["Magneton", "Magnemite", "Forretress", "Steelix", "Scizor", "Skarmory"]
FAIRY.pokemon = ["Clefable", "Wigglytuff", "Mr. Mime", "Clefairy", "Jigglypuff", "Cleffa", "Togepi", "Togetic",
                 "Marill", "Azumarill", "Snubbull", "Granbull"]
NONE.pokemon = ["MissingNo."]

NORMAL.moves = ["cut", "pound", "quick attack", "scratch", "tackle", "body slam", "horn attack", "hyper beam",
                "hyper fang", "rest", "stomp", "struggle", "swift", "vice grip", "wrap"]
FIRE.moves = ["ember", "fire fang", "fire blast", "fire punch", "flame burst", "flame charge", "flame wheel",
              "flamethrower", "heat wave"]
WATER.moves = ["bubble", "splash", "water gun", "aqua jet", "aqua tail", "brine", "bubble beam", "hydro pump", "scald",
               "water pulse"]
GRASS.moves = ["razor leaf", "vine whip", "leaf blade", "mega drain", "giga drain", "petal blizzard", "power whip",
               "seed bomb", "solar beam"]
ELECTRIC.moves = ["spark", "thunder shock", "discharge", "parabolic charge", "thunder", "thunder punch", "thunderbolt"]
ICE.moves = ["frost breath", "ice shard", "blizzard", "ice beam", "ice punch", "icy wind"]
FIGHTING.moves = ["karate chop", "low kick", "rock smash", "brick break", "cross chop", "low sweep", "submission"]
POISON.moves = ["acid", "poison jab", "poison sting", "cross poison", "gunk shot", "poison fang", "sludge",
                "sludge bomb", "sludge wave"]
GROUND.moves = ["mud shot", "mud slap", "bone club", "bulldoze", "dig", "drill run", "earthquake", "mud bomb"]
FLYING.moves = ["peck", "wing attack", "aerial ace", "air cutter", "drill peck", "hurricane"]
PSYCHIC.moves = ["confusion", "psycho cut", "zen headbutt", "heart stamp", "psybeam", "psychic", "psyshock",
                 "psystrike"]
BUG.moves = ["bug bite", "fury cutter", "bug buzz", "megahorn", "signal beam", "x-scissor"]
ROCK.moves = ["rock throw", "ancient power", "power gem", "rock slide", "rock tomb", "stone edge"]
GHOST.moves = ["lick", "shadow claw", "ominous wind", "shadow ball", "shadow punch", "shadow sneak"]
DRAGON.moves = ["dragon breath", "dragon claw", "dragon pulse", "twister"]
DARK.moves = ["bite", "feint attack", "sucker punch", "dark pulse", "night slash"]
STEEL.moves = ["bullet punch", "metal claw", "steel wing", "flash cannon", "iron head", "magnet bomb"]
FAIRY.moves = ["dazzling gleam", "disarming voice", "draining kiss", "moonblast", "play rough"]
NONE.moves = ["none"]

dmg = 0
dur = 1
nrg = 2
crit = 3

# to get the damage for acid attack, type quick_moves["acid"][dmg]
# to get the duration for acid attack, type quick_moves["acid"][dur]
# to get the energy gain for acid attack, type quick_moves["acid"][nrg]
quick_moves = {"acid": [10.0, 1.05, 7],
               "bite": [6.0, 0.5, 7, 0.05],
               "bubble": [25.0, 2.3, 15],
               "bug bite": [5.0, 0.45, 7],
               "bullet punch": [10.0, 1.2, 7],
               "confusion": [15.0, 1.51, 7],
               "cut": [12, 1.13, 7],
               "dragon breath": [6.0, 0.5, 7],
               "ember": [10.0, 1.05, 7],
               "feint attack": [12.0, 1.04, 7],
               "fire fang": [10.0, 0.84, 4],
               "frost breath": [9.0, 0.81, 7],
               "fury cutter": [3.0, 0.4, 12],
               "ice shard": [15.0, 1.4, 7],
               "karate chop": [6.0, 0.8, 7],
               "lick": [5.0, 0.5, 7],
               "low kick": [5.0, 0.6, 7],
               "metal claw": [8.0, 0.63, 7],
               "mud shot": [6.0, 0.55, 7],
               "mud slap": [15.0, 1.35, 9],
               "peck": [10.0, 1.15, 10],
               "poison jab": [12.0, 1.05, 7],
               "poison sting": [6.0, 0.58, 4],
               "pound": [7.0, 0.54, 7],
               "psycho cut": [7.0, 0.57, 7],
               "quick attack": [10.0, 1.33, 7],
               "razor leaf": [15.0, 1.45, 7, 0.05],
               "rock smash": [15.0, 1.41, 7],
               "rock throw": [12.0, 1.36, 7],
               "scratch": [6.0, 0.5, 7],
               "shadow claw": [11.0, 0.95, 7],
               "spark": [7.0, 0.7, 4],
               "splash": [0.0, 1.23, 7],
               "steel wing": [15.0, 1.33, 4],
               "sucker punch": [7.0, 0.7, 4],
               "tackle": [12.0, 1.1, 7],
               "thunder shock": [5.0, 0.6, 7],
               "vine whip": [7.0, 0.65, 7],
               "water gun": [6.0, 0.5, 7],
               "wing attack": [9.0, 0.75, 7],
               "zen headbutt": [12.0, 1.05, 4]}

# charge_moves is exactly like quick_moves, except charge_moves["dig"][nrg] returns energy loss, not gain
# to get the chance of a critical hit for blizzard attack, type charge_moves["blizzard"][crit]
charge_moves = {"aerial ace": [30.0, 2.9, 25, 0.05],
                "air cutter": [30.0, 3.3, 25, 0.25],
                "ancient power": [35.0, 3.6, 25, 0.05],
                "aqua jet": [25.0, 2.35, 20, 0.05],
                "aqua tail": [45.0, 2.35, 50, 0.05],
                "blizzard": [100.0, 3.9, 100, 0.05],
                "body slam": [40.0, 1.56, 50, 0.05],
                "bone club": [25.0, 1.6, 25, 0.05],
                "brick break": [30.0, 1.6, 33, 0.25],
                "brine": [25.0, 2.4, 25, 0.05],
                "bubble beam": [30.0, 2.9, 25, 0.05],
                "bug buzz": [75.0, 4.25, 50, 0.05],
                "bulldoze": [35.0, 3.4, 25, 0.05],
                "cross chop": [60.0, 2.0, 100, 0.25],
                "cross poison": [25.0, 1.5, 25, 0.25],
                "dark pulse": [45.0, 3.5, 33, 0.05],
                "dazzling gleam": [55.0, 4.2, 33, 0.05],
                "dig": [70.0, 5.8, 33, 0.05],
                "disarming voice": [25.0, 3.9, 20, 0.05],
                "discharge": [35.0, 2.5, 33, 0.05],
                "dragon claw": [35.0, 1.6, 50, 0.25],
                "dragon pulse": [65.0, 3.6, 50, 0.05],
                "draining kiss": [25.0, 2.8, 20, 0.05],
                "drill peck": [40.0, 2.7, 33, 0.05],
                "drill run": [50.0, 3.4, 33, 0.25],
                "earthquake": [100.0, 4.2, 100, 0.05],
                "fire blast": [100.0, 4.1, 100, 0.05],
                "fire punch": [40.0, 2.8, 33, 0.05],
                "flame burst": [30.0, 2.1, 25, 0.05],
                "flame charge": [25.0, 3.1, 20, 0.05],
                "flame wheel": [40.0, 4.6, 25, 0.05],
                "flamethrower": [55.0, 2.9, 50, 0.05],
                "flash cannon": [60.0, 3.9, 33, 0.05],
                "giga drain": [50.0, 3.6, 33, 0.05],
                "gunk shot": [65.0, 3.0, 100, 0.05],
                "heart stamp": [25.0, 2.55, 25, 0.05],
                "heat wave": [80.0, 3.8, 100, 0.05],
                "horn attack": [25.0, 2.2, 25, 0.05],
                "hurricane": [80.0, 3.2, 100, 0.05],
                "hydro pump": [90.0, 3.8, 100, 0.05],
                "hyper beam": [120.0, 5.0, 100, 0.05],
                "hyper fang": [35.0, 2.1, 33, 0.05],
                "ice beam": [65.0, 3.65, 50, 0.05],
                "ice punch": [45.0, 3.5, 33, 0.05],
                "icy wind": [25.0, 3.8, 20, 0.05],
                "iron head": [30.0, 2.0, 33, 0.05],
                "leaf blade": [55.0, 2.8, 50, 0.25],
                "low sweep": [30.0, 2.25, 25, 0.05],
                "magnet bomb": [30.0, 2.8, 25, 0.05],
                "mega drain": [25.0, 3.2, 20, 0.05],
                "megahorn": [80.0, 3.2, 100, 0.05],
                "moonblast": [85.0, 4.1, 100, 0.05],
                "mud bomb": [30.0, 2.6, 25, 0.05],
                "night slash": [30.0, 2.7, 25, 0.25],
                "ominous wind": [30.0, 3.1, 25, 0.05],
                "parabolic charge": [25.0, 2.1, 20, 0.05],
                "petal blizzard": [65.0, 3.2, 50, 0.05],
                "play rough": [55.0, 2.9, 50, 0.05],
                "poison fang": [25.0, 2.4, 20, 0.05],
                "power gem": [40.0, 2.9, 33, 0.05],
                "power whip": [70.0, 2.8, 100, 0.0],
                "psybeam": [40.0, 3.8, 25, 0.05],
                "psychic": [55.0, 2.8, 50, 0.05],
                "psyshock": [40.0, 2.7, 33, 0.05],
                "psystrike": [100, 5.1, 100, 0.05],
                "rest": [50.0, 3.1, 33, 0.0],
                "rock slide": [50.0, 3.2, 33, 0.05],
                "rock tomb": [30.0, 3.4, 25, 0.25],
                "scald": [55.0, 4.0, 33, 0.05],
                "seed bomb": [40.0, 2.4, 33, 0.05],
                "shadow ball": [45.0, 3.08, 33, 0.05],
                "shadow punch": [25.0, 2.1, 25, 0.05],
                "shadow sneak": [25.0, 3.1, 20, 0.05],
                "signal beam": [45.0, 3.1, 33, 0.05],
                "sludge": [30.0, 2.6, 25, 0.05],
                "sludge bomb": [55.0, 2.6, 50, 0.05],
                "sludge wave": [70.0, 3.4, 100, 0.05],
                "solar beam": [120.0, 4.9, 100, 0.05],
                "stomp": [30.0, 2.1, 25, 0.05],
                "stone edge": [80.0, 3.1, 100, 0.50],
                "struggle": [15.0, 1.7, 20, 0.0],
                "submission": [30.0, 2.1, 33, 0.05],
                "swift": [30.0, 3.0, 25, 0.05],
                "thunder": [100.0, 4.3, 100, 0.05],
                "thunder punch": [40.0, 2.4, 33, 0.05],
                "thunderbolt": [55.0, 2.7, 50, 0.05],
                "twister": [25.0, 2.7, 20, 0.05],
                "vice grip": [25.0, 2.1, 20, 0.05],
                "water pulse": [35.0, 3.3, 25, 0.05],
                "wrap": [25.0, 4.0, 20, 0.05],
                "x-scissor": [35.0, 2.1, 33, 0.05],
                "none": [0.0, 10.0, 0, 0.0]}

TYPES = [NORMAL, FIRE, WATER, GRASS, ELECTRIC, ICE, FIGHTING, POISON, GROUND,
         FLYING, PSYCHIC, BUG, ROCK, GHOST, DRAGON, DARK, STEEL, FAIRY, NONE]


# takes type (string) and returns corresponding Type
def get_type(type_name):
    for POGO_TYPE in TYPES:
        if type_name == POGO_TYPE.name:
            return POGO_TYPE


# takes two Types and returns new dual Type
def dual_type(first, second):
    dual_type_name = " ".join([first.name, "/", second.name])
    new_dual_type = Type(dual_type_name)
    for pokemon in first.pokemon:
        if pokemon in second.pokemon:
            new_dual_type.pokemon.append(pokemon)
    new_dual_type.moves = first.moves + second.moves
    for type_i in types:
        if type_i in first.strong and type_i in second.strong:
            new_dual_type.very_strong.append(type_i)
        elif type_i in first.strong and type_i not in second.weak \
                or type_i in second.strong and type_i not in first.weak:
            new_dual_type.strong.append(type_i)
        elif type_i in first.weak and type_i not in second.strong \
                or type_i in second.weak and type_i not in first.strong:
            new_dual_type.weak.append(type_i)
        elif type_i in first.weak and type_i in second.weak:
            new_dual_type.very_weak.append(type_i)

    return new_dual_type


# takes pokemon name (string) and returns that pokemon's Type
def get_pokemon_type(pokemon):
    temp_type = []
    for POGO_TYPE in TYPES:
        if pokemon in POGO_TYPE.pokemon:
            temp_type.append(POGO_TYPE)
    if len(temp_type) == 1:
        return temp_type[0]
    else:
        return dual_type(temp_type[0], temp_type[1])


# THIS FOR LOOP TESTS THE CORRECTNESS OF EACH POKEMON'S TYPE(S)
"""for pokemon in pokes:
    print(pokemon, "is", get_pokemon_type(pokemon).name)"""


# takes move (string) and returns that move's Type
def get_move_type(move):
    for POGO_TYPE in TYPES:
        if move in POGO_TYPE.moves:
            return POGO_TYPE


crit_multiplier = 1.5
stab = 1.25
se_multiplier = 1.25
nve_multiplier = 0.8


def calculate_dps(pokemon, quick_move, charge_move, opponent):
    tap_dmg = floor(0.5 * quick_moves[quick_move][dmg]) + 1
    tap_dur = quick_moves[quick_move][dur]  # saves typing and keeps original data safe
    tap_nrg = quick_moves[quick_move][nrg]  # this is very convenient, trust me
    hold_dmg = floor(0.5 * charge_moves[charge_move][dmg]) + 1
    hold_dur = charge_moves[charge_move][dur]
    hold_nrg = charge_moves[charge_move][nrg]
    crit_chance = 0  # charge_moves[charge_move][crit]
    hold_dmg += hold_dmg * crit_multiplier * crit_chance
    user_pokemon_type = get_pokemon_type(pokemon)
    opponent_pokemon_type = get_pokemon_type(opponent)
    if quick_move in user_pokemon_type.moves:
        # print("Quick move has STAB")
        tap_dmg *= stab
    if charge_move in user_pokemon_type.moves:
        # print("Charge move has STAB")
        hold_dmg *= stab
    if get_move_type(quick_move).name in opponent_pokemon_type.very_weak:
        # print("Quick move is doubly super effective against opponent")
        tap_dmg *= se_multiplier * se_multiplier
    elif get_move_type(quick_move).name in opponent_pokemon_type.weak:
        # print("Quick move is super effective against opponent")
        tap_dmg *= se_multiplier
    elif get_move_type(quick_move).name in opponent_pokemon_type.strong:
        # print("Quick move is not very effective against opponent")
        tap_dmg *= nve_multiplier
    elif get_move_type(quick_move).name in opponent_pokemon_type.very_strong:
        # print("Quick move is doubly not very effective against opponent")
        tap_dmg *= nve_multiplier * nve_multiplier
    if get_move_type(charge_move).name in opponent_pokemon_type.very_weak:
        hold_dmg *= se_multiplier * se_multiplier
    elif get_move_type(charge_move).name in opponent_pokemon_type.weak:
        hold_dmg *= se_multiplier
    elif get_move_type(charge_move).name in opponent_pokemon_type.strong:
        hold_dmg *= nve_multiplier
    elif get_move_type(charge_move).name in opponent_pokemon_type.very_strong:
        hold_dmg *= nve_multiplier * nve_multiplier
    tap_dps = tap_dmg / tap_dur
    hold_dps = hold_dmg / hold_dur
    if tap_dps >= hold_dps:
        # print("Do not use your Pokemon's charge move.")
        return str(round(tap_dps, 2)) + " DPS\ntap only"
    elif hold_nrg == 100:
        taps = ceil(100 / tap_nrg)
        # print("It takes", taps, "taps to get one charge.")
        total_dmg = tap_dmg * taps + hold_dmg
        total_dur = tap_dur * taps + hold_dur
        total_dps = round((total_dmg / total_dur), 2)
        return str(total_dps) + " DPS"
    else:
        taps = hold_nrg
        holds = tap_nrg
        # print(taps, "taps allows for", holds, "holds.")
        total_dmg = tap_dmg * taps + hold_dmg * holds
        total_dur = tap_dur * taps + hold_dur * holds
        total_dps = round((total_dmg / total_dur), 2)
        return str(total_dps) + " DPS"


def print_type_info(pokemon_go_type):
    print("Name:", pokemon_go_type.name)
    print("Pokemon:", pokemon_go_type.pokemon)
    print("Moves:", pokemon_go_type.moves)
    print("Very strong against:", pokemon_go_type.very_strong)
    print("Strong against:", pokemon_go_type.strong)
    print("Weak against:", pokemon_go_type.weak)
    print("Very weak against:", pokemon_go_type.very_weak)
    print("Super effective against", pokemon_go_type.super_eff)
    print("Not very effective against:", pokemon_go_type.not_very_eff)


class TypeScreen(Screen):
    pass


class DPSScreen(Screen):
    @staticmethod
    def get_dps(pokemon, quick_move, charge_move, opponent):
        if quick_move not in quick_moves.keys():
            return "Enter a valid\nquick move"
        elif charge_move not in charge_moves.keys():
            charge_move = "none"
        if pokemon not in pokes.keys():
            pokemon = "MissingNo."
        if opponent not in pokes.keys():
            opponent = "MissingNo."
        return calculate_dps(pokemon, quick_move, charge_move, opponent)
    pass


class QuizScreen(Screen):
    @staticmethod
    def ask_question():
        topic = types[randint(0, 17)]
        question = ["What attack types are super\neffective against " + topic + " Pokemon?",
                    "What attack types are not very\neffective against " + topic + " Pokemon?",
                    "What Pokemon types are\nstrong against " + topic + " attacks?",
                    "What Pokemon types are\nweak against " + topic + " attacks?"]
        return question[randint(0, 3)]

    @staticmethod
    def check_answer(answer, answers):
        if answer not in answers:
            return
    pass


class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("PoGoHelper.kv")


class PoGoHelper(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    PoGoHelper().run()

"""
user_pokemon = ""
while user_pokemon not in pokes:
    print("What is your Pokemon's name?")
    user_pokemon = get_input()
poke_quick_moves = []
user_quick_move = ""
while user_quick_move not in quick_moves:
    print("What is this Pokemon's quick move?")
    user_quick_move = get_input()
    if user_quick_move in quick_moves:
        poke_quick_moves.append(user_quick_move)
        print("More?")
        if get_input()[0].lower() == "y":
            user_quick_move = ""
poke_charge_moves = []
user_charge_move = ""
while user_charge_move not in charge_moves:
    print("What is this Pokemon's charge move?")
    user_charge_move = get_input()
    if user_charge_move in charge_moves:
        poke_charge_moves.append(user_charge_move)
        print("More?")
        if get_input()[0].lower() == "y":
            user_charge_move = ""
for quick in poke_quick_moves:
    for charge in poke_charge_moves:
        print(calculate_dps(user_pokemon, quick, charge, opponent_pokemon))
"""
