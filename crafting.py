import logging
"""
Crafting Solver Classes
"""


class CraftingStock:
    """
    Stock Data Structure
    """
    def __init__(self):
        """
        Initialize internal stock dictionary
        """
        self._stock = {}

    def push(self, material, qty=1):
        """
        Push material with the given quantity in stock

        :param material: material name
        :param qty:  quantity to push in stock
        :return: None
        """
        try:
            self._stock[material] += qty
        except KeyError:
            self._stock[material] = qty

    def is_available(self, material, qty=1):
        """
        Check if the given material quantity is available in stock instance

        :param material: material name
        :param qty: quantity to check in stock
        :return: True if the material quantity is available in stock False otherwise
        """
        try:
            return self._stock[material] >= qty
        except KeyError:
            return False

    def pop(self, material, qty=1):
        """
        Pop the given material quantity from stock in there enough in stocl

        :param material: material name
        :param qty: quantity tu pop in stock
        :return: True if pop successfully, False otherwise
        """
        if self.is_available(material, qty):
            try:
                self._stock[material] -= qty
                return True
            except KeyError:
                pass
        return False

    def available(self, material):
        """
        Check if the given material is available

        :param material: Material name
        :return: Material quantity available
        """
        try:
            return self._stock[material]
        except KeyError:
            return 0

    def is_empty(self):
        """
        Check if stock is empty

        :return: True if stock is empty, False otherwise
        """
        if len(self._stock) == 0:
            return True
        else:
            empty = False
            for count in self._stock.values():
                if count >= 0:
                    empty = True
            return empty


class CraftingSolver:

    def __init__(self, recipes_data, current_stock=CraftingStock()):
        self._recipes = recipes_data
        self._stock = current_stock
        self._excluded = []
        self._raw_materials = []

    def __filter_recipe(self):
        """
        Filter recipes by non excluded recipes

        :return: Recipes dictionary without excluded recipes
        """
        logging.info('Filtering recipes')
        filtered_data = {}
        # filter excluded element
        for key, value in self._recipes.items():
            if key not in self._excluded:
                filtered_data[key] = value
        return filtered_data

    def __get_full_r(self, component_name, recursion=False):
        """
        Compute ingredients needed to craft the given element.

        :param component_name: Name of the recipe material
        :param recursion: True if the the call is recurcive, False otherwise
        :return: dictionary of Ingredient/Quantity needed to craft the given component_name
        """
        logging.info('Computing ingredient for {}'.format(component_name))
        components = {}
        try:
            ingredient_list = self._recipes[component_name]
        except KeyError:
            self._raw_materials.append(component_name)
            return {}
        for ingredient, count in ingredient_list.items():
            to_merge = {}

            if ingredient not in self._recipes.keys():
                to_merge[ingredient] = count
            else:
                to_merge = self.__get_full_r(ingredient, True)
                # Ponderate qty by number of ingredient needed
                for key in to_merge.keys():
                    to_merge[key] *= count - self._stock.available(ingredient)

            for needed, full_qty in to_merge.items():
                actual_qty = self._stock.available(needed)
                self._stock.pop(needed, actual_qty)
                needed_qty = full_qty - actual_qty
                try:
                    components[needed] += needed_qty
                except KeyError:
                    components[needed] = needed_qty
        if not recursion:
            self._stock.push(component_name)
        return components

    def solve_simple(self, excluded=[]):
        """
        Compute ingredients list simply by adding ingredients quantity without checking
        any ingredient recipes

        :param excluded: Recipes list to exclude from computing
        :return: Dictionnary of ingredient quantity needed
        """
        self._excluded = excluded
        filtered_data = self.__filter_recipe()
        items = {}
        for recipe_items in filtered_data.values():
            for item, count in recipe_items.items():
                try:
                    items[item] += count
                except KeyError:
                    items[item] = count
        return items

    def solve_deep(self, excluded=[]):
        """
        Compute ingredient list recursively. If a recipe ingredient may be crafted by a
        recipe, the ingredient recipe is also computed

        :param excluded: Recipes list to exclude from computing
        :return: Dictionnary of ingredient quantity needed
        """
        self._excluded = excluded
        logging.info('Computing requirements recursively')
        filtered_data = self.__filter_recipe()
        items = {}
        for recipe in filtered_data.keys():
            sub_components = self.__get_full_r(recipe)
            for name, count in sub_components.items():
                try:
                    items[name] += count
                except KeyError:
                    items[name] = count
        return items
