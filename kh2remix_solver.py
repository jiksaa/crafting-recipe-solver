import crafting
import pprint

"""
    Data definition
"""
RECIPE_RAW_DATA = {
    'Elixir': {
        'Pierre de mithril': 3,
        'Pierre de force': 1,
        'Pierre noire': 1
    },
    'Mégalixir': {'Pierre de mithril': 3, 'Pierre de force': 1, 'Pierre noire': 1,
                  'Gemme de sérénité': 1},
    'Mégapotion': {'Eclat de mithril': 3, 'Eclat de force': 1, 'Eclat ardent': 1, 'Eclat hyalin': 1},
    'Mégaéther': {'Eclat de mithril': 3, 'Eclat de force': 1, 'Eclat ardent': 1, 'Eclat hyalin': 1,
                  'Pierre de sérénité': 1},
    'Reflux': {'Eclat de mithril': 3, 'Eclat noir': 3, 'Eclat glacial': 1, 'Eclat grondant': 1},
    'Mégareflux': {'Eclat de mithril': 3, 'Eclat noir': 3, 'Eclat glacial': 1, 'Eclat grondant': 1,
                   'Eclat de sérénité': 1},
    'Bonus PC': {'Gemme de mithril': 1, 'Cristal de force': 3, 'Cristal noir': 3, 'Cristal glacial': 3},
    'Bonus Magie': {'Gemme de mithril': 1, 'Cristal de force': 3, 'Cristal noir': 3, 'Cristal glacial': 3,
                    'Cristal de sérénité': 1},
    'Bonus Défense': {'Cristal de mithril': 1, 'Cristal ardent': 3, 'Cristal grondant': 3,
                      'Cristal hyalin': 3},
    'Bonus Attaque': {'Cristal de mithril': 1, 'Cristal ardent': 3, 'Cristal grondant': 3,
                      'Cristal hyalin': 3, 'Cristal de sérénité': 1},
    'Bracelet Brasier X': {'Eclat de mithril': 5, 'Pierre ardente': 1, 'Eclat ardent': 1},
    'Bracelet Brasier XX': {'Eclat de mithril': 5, 'Pierre ardente': 1, 'Eclat ardent': 1,
                            'Eclat de sérénité': 1},
    'Gourmette Glacier X': {'Eclat de mithril': 5, 'Pierre glaciale': 1, 'Eclat glaciale': 1},
    'Gourmette Glacier XX': {'Eclat de mithril': 5, 'Pierre glaciale': 1, 'Eclat glaciale': 1,
                             'Eclat de sérénité': 1},
    'Jonc Foudre X': {'Eclat de mithril': 5, 'Pierre grondante': 1, 'Eclat grondant': 1},
    'Jonc Foudre XX': {'Eclat de mithril': 5, 'Pierre grondante': 1, 'Eclat grondant': 1,
                       'Eclat de sérénité': 1},
    'Chevillère sinistre': {'Eclat de mithril': 5, 'Pierre hyaline': 1, 'Eclat hyalin': 1},
    'Chevillère du chaos': {'Eclat de mithril': 5, 'Pierre hyaline': 1, 'Eclat hyalin': 1,
                            'Eclat de sérénité': 1},
    'Acrisius': {'Pierre de mithril': 5, 'Pierre ardente': 1, 'Pierre glaciale': 1,
                 'Pierre grondante': 1},
    'Acrisius +': {'Pierre de mithril': 5, 'Pierre ardente': 1, 'Pierre glaciale': 1,
                   'Pierre grondante': 1, 'Pierre de sérénité': 1},
    'Poignet de force': {'Pierre de mithril': 5, 'Pierre de force': 1, 'Pierre noire': 1,
                         'Pierre hyaline': 1},
    'Poignet': {'Pierre de mithril': 5, 'Pierre de force': 1, 'Pierre noire': 1, 'Pierre hyaline': 1,
                'Pierre de sérénité': 1},
    'Escarboucle': {'Pierre de mithril': 3, 'Pierre de force': 1, 'Eclat de force': 1, 'Eclat noir': 1},
    'Diamant': {'Pierre de mithril': 3, 'Pierre de force': 1, 'Eclat de force': 1, 'Eclat noir': 1,
                'Eclat de sérénité': 1},
    'Chevalière mithril': {'Pierre de mithril': 3, 'Pierre de force': 1, 'Pierre noire': 1,
                           'Eclat noir': 1},
    'Chevalière orichalque': {'Pierre de mithril': 3, 'Pierre de force': 1, 'Pierre noire': 1,
                              'Eclat noir': 1, 'Eclat de sérénité': 1},
    'Boucle de soldat': {'Gemme de mithril': 3, 'Gemme noire': 1, 'Gemme glaciale': 1,
                         'Gemme hyaline': 1},
    'Boucle fine lame': {'Gemme de mithril': 3, 'Gemme noire': 1, 'Gemme glaciale': 1, 'Gemme hyaline': 1,
                         'Pierre de sérénité': 1},
    'Boucle de mage': {'Gemme de mithril': 3, 'Gemme de force': 1, 'Gemme ardente': 1,
                       'Gemme grondante': 1},
    'Boucle de pourfendeur': {'Gemme de mithril': 3, 'Gemme de force': 1, 'Gemme ardente': 1,
                              'Gemme grondante': 1, 'Pierre de sérénité': 1},
    'Anneau étoilé': {'Cristal de mithril': 3, 'Cristal noir': 1, 'Gemme noire': 1, 'Pierre noire': 1,
                      'Eclat noir': 1},
    'Anneau royal': {'Cristal de mithril': 3, 'Cristal noir': 1, 'Gemme noire': 1, 'Pierre noire': 1,
                     'Eclat noir': 1, 'Gemme de sérénité': 1},
    'Eclat de mithril': {'Pierre mate': 1, 'Eclat mat': 3, 'Pierre nébuleuse': 1, 'Eclat nébuleux': 3},
    'Pierre de mithril': {'Pierre mate': 1, 'Eclat mat': 3, 'Pierre nébuleuse': 1, 'Eclat nébuleux': 3,
                          'Eclat de sérénité': 1},
    'Gemme de mithril': {'Cristal mat': 1, 'Gemme mate': 3, 'Cristal nébuleux': 1, 'Gemme nébuleuse': 3},
    'Cristal de mithril': {'Cristal mat': 1, 'Gemme mate': 3, 'Cristal nébuleux': 1, 'Gemme nébuleuse': 3,
                           'Pierre de sérénité': 1},
    'Ruban rouge': {'Cristal de mithril': 3, 'Orichalque': 1, 'Pierre mate': 1, 'Eclat mat': 1},
    'Ruban bleu': {'Cristal de mithril': 3, 'Orichalque': 1, 'Pierre mate': 1, 'Eclat mat': 1,
                   'Gemme de sérénité': 1},
    'Amulette lunaire': {'Orichalque': 3, 'Cristal de mithril': 1, 'Pierre nébuleuse': 1,
                         'Eclat nébuleux': 1},
    'Amulette stellaire': {'Orichalque': 3, 'Cristal de mithril': 1, 'Pierre nébuleuse': 1,
                           'Eclat nébuleux': 1, 'Gemme de sérénité': 1},
    'Save the Queen': {'Orichalque': 1, 'Cristal mat': 3, 'Gemme mate': 5, 'Pierre mate': 7,
                       'Eclat mat': 9},
    'Save the Queen +': {'Orichalque': 1, 'Cristal mat': 3, 'Gemme mate': 5, 'Pierre mate': 7,
                         'Eclat mat': 9, 'Cristal de sérénité': 1},
    'Save the King': {'Orichalque': 1, 'Cristal nébuleux': 3, 'Gemme nébuleuse': 5, 'Pierre nébuleuse': 7,
                      'Eclat nébuleux': 9},
    'Save the King +': {'Orichalque': 1, 'Cristal nébuleux': 3, 'Gemme nébuleuse': 5,
                        'Pierre nébuleuse': 7, 'Eclat nébuleux': 9, 'Cristal de sérénité': 1},
    'Ultima': {'Orichalque+': 13, 'Orichalque': 1, 'Cristal de mithril': 1, 'Cristal mat': 1,
               'Cristal nébuleux': 1, 'Cristal de sérénité': 3},
    'Cristal de sérénité': {'Cristal de tranquilité': 1, 'Cristal de souvenir': 1,
                            'Cristal de vitalité': 9},
    'Illusion manifeste': {'Cristal de tranquilité': 1, 'Cristal de souvenir': 1, 'Cristal de vitalité': 9,
                           'Gemme de sérénité': 1},
    'Anneau d\'attraction': {'Illusion manifeste': 1, 'Éclat de souvenir': 3, 'Gemme de vitalité': 3,
                             'Pierre de vitalité': 5, 'Éclat de vitalité': 9},
    'Anneau de fortune': {'Illusion manifeste': 1, 'Éclat de souvenir': 3, 'Gemme de vitalité': 3,
                          'Pierre de vitalité': 5, 'Éclat de vitalité': 9, 'Cristal de sérénité': 1},
    'Grimoire sombre': {'Illusion perdue': 1, 'Illusion manifeste': 1, 'Cristal de souvenir': 1,
                        'Gemme de sérénité': 3},
    'Grimoire sombre +': {'Illusion perdue': 1, 'Illusion manifeste': 1, 'Cristal de souvenir': 1,
                          'Gemme de sérénité': 3, 'Éclat de souvenir': 7, 'Cristal de sérénité': 1},
    'Talisman isolant': {'Illusion perdue': 1, 'Pierre de souvenir': 1, 'Gemme de souvenir': 3,
                         'Pierre de tranquilité': 1, 'Gemme de tranquilité': 3},
    'Talisman isolant +': {'Illusion perdue': 1, 'Pierre de souvenir': 1, 'Gemme de souvenir': 3,
                           'Pierre de tranquilité': 1, 'Gemme de tranquilité': 3,
                           'Cristal de sérénité': 1},
    'Épanouissement': {'Illusion perdue': 1, 'Illusion manifeste': 1, 'Cristal de tranquilité': 1,
                       'Gemme de sérénité': 3},
    'Épanouissement +': {'Illusion perdue': 1, 'Illusion manifeste': 1, 'Cristal de tranquilité': 1,
                         'Gemme de sérénité': 3, 'Cristal de sérénité': 1},
    'Centurion': {'Illusion perdue': 1, 'Cristal de souvenir': 1, 'Gemme de souvenir': 3,
                  'Pierre de souvenir': 5, 'Éclat de souvenir': 7},
    'Centurion +': {'Illusion perdue': 1, 'Cristal de souvenir': 1, 'Gemme de souvenir': 3,
                    'Pierre de souvenir': 5, 'Éclat de souvenir': 7, 'Cristal de sérénité': 1},
    'Fierté gelée': {'Illusion perdue': 1, 'Cristal de tranquilité': 1, 'Gemme de tranquilité': 3,
                     'Pierre de tranquilité': 5, 'Éclat de tranquilité': 7},
    'Fierté gelée +': {'Illusion perdue': 1, 'Cristal de tranquilité': 1, 'Gemme de tranquilité': 3,
                       'Pierre de tranquilité': 5, 'Éclat de tranquilité': 7, 'Cristal de sérénité': 1}
}

EXCLUDE = ['Elixir', 'Mégalixir', 'Mégapotion', 'Save the King +', 'Illusion manifeste', 'Mégaéther', 'Reflux',
           'Mégareflux', 'Bonus PC', 'Bonus Magie', 'Bonus Défense', 'Cristal de sérénité', 'Bonus Attaque',
           'Bracelet Brasier X', 'Bracelet Brasier XX', 'Gourmette Glacier X', 'Gourmette Glacier XX', 'Jonc Foudre X',
           'Chevillère sinistre', 'Acrisius', 'Acrisius +', 'Poignet de force', 'Poignet', 'Escarboucle', 'Diamant',
           'Chevalière mithril', 'Chevalière orichalque', 'Boucle de soldat', 'Boucle fine lame', 'Boucle de mage',
           'Boucle de pourfendeur', 'Anneau étoilé', 'Anneau royal', 'Eclat de mithril', 'Pierre de mithril',
           'Ruban rouge', 'Ruban bleu', 'Amulette lunaire', 'Amulette stellaire', 'Save the Queen', 'Save the Queen +',
           'Save the King', ]

"""
    Init pprinter
"""

pp = pprint.PrettyPrinter(indent=2)

"""
     Create theorical stock
"""
current_stock = crafting.CraftingStock()
for item in EXCLUDE:
    current_stock.push(item)

"""
    Init Crafting solver
"""
solver = crafting.CraftingSolver(RECIPE_RAW_DATA, current_stock)
solved = solver.solve_deep(EXCLUDE)


"""
    Display Result
"""
pp.pprint(solved)
