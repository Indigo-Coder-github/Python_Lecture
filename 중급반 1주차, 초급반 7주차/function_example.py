def making_bread(ingredient):
    if ingredient == "egg": return "egg bread"
    elif ingredient == "apple": return "apple pie"

def bread_recipe():
    print("Put an ingredient you want!")

def making_all_bread():
    return "egg bread", "apple pie"

bread_recipe()
print(making_bread("egg"))
print(making_all_bread())

kims_bread, kangs_bread = making_all_bread()
print(kims_bread, kangs_bread)

def show_food_list(ingredients, food="sushi"):
    for ingredient in ingredients: print("{}_{}".format(ingredient, food))
show_food_list(["salmon", "tuna", "shrimp"], "sashimi")

def show_food_list(food, *args):
    for ingredient in args: print("{}_{}".format(ingredient, food))
show_food_list("sushi", "salmon", "tuna", "shrimp")

ingredient_list = ["salmon", "tuna", "shrimp"]
show_food_list("sushi", *ingredient_list)

def show_food_list(**kwargs):
    if "food" in kwargs and "ingredient" in kwargs:
        print("{}_{}".format(kwargs["ingredient"], kwargs["food"]))
show_food_list(**{"food":"pizza", "ingredient":"pineapple"})