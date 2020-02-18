import math


# Input is the recipe && the available ingredients you have
def recipe_batches(recipe, ingredients, test):
    # Key is the ingredient name
    # Values are the amount
    # Recipe dictionary represents amount needed
    # Ingredients dictionary represents amount available
    # Function should output the maximum number of whole batches that can be made with available ingredients

    # Need to iterate over the recipe, get the key and check if available
    # Then need to check if the value is enough
    # If it is not then we need to return 0

    total = test
    for key, value in recipe.items():
        # Check if the ingredients contain the ingredients that the recipe calls for
        if ingredients.get(key) is not None:
            # pass
            if ingredients.get(key) >= value:
                ingredients[key] -= value
                print('new ing', ingredients[key])
            else:
                print("Not enough {ingredient} available".format(ingredient=key))
                return total
        # If the ingredient is not available return 0 and output what ingredient is not available
        else:
            print("No {ingredient} available".format(ingredient=key))
            return 0
            # Check if the amount is the correct amount using the current key and value
        # if ingredients.get(key) >= value:
        #     ingredients[key] -= value
        #     print('new ing', ingredients[key])
        # else:
        #     print("Not enough {ingredient} available".format(ingredient=key))
        #     return 0
    total += 1
    recipe_batches(recipe, ingredients, total)
    print(total)
    return total


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 2}
    ingredients = {'milk': 200}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients, 0), ingredients=ingredients))
