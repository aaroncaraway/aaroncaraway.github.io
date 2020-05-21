---
layout: single
title: 'PROJECT_RecipeScraper pt1'
tags: PROJECT_RecipeScraper
classes: wide
---

# PROBLEM: Food waste. I want to use ALL the tomatoes I buy at Trader Joes.

# SOLUTION: 

1. Find food blog I like
2. Scrape the site for recipes
3. Collect ingredients
4. Make a database 
5. Optimze for recipes with similar ingredients of small quantities


## STEP 1: Get links to all recipes 

```python
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# We don't need the navigation links
def not_nav(href):
    return href and not re.compile("category").search(href)

# Get the recipes
def get_recipe_links(url):
    all_links = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    recipes = soup.find("div", "recipe-archive")
    recipe_links = recipes.find_all(href=not_nav)
    for link in recipe_links:
        all_links.append(link.get('href'))
    return all_links
#         print(link.get('href'))

all_links_from_site = []
for num in range(0,184):
    links_from_page = get_recipe_links("https://www.halfbakedharvest.com/category/recipes/page/" + str(num))
    all_links_from_site.extend(links_from_page)

df = pd.DataFrame({'links': all_links_from_site})
```


```python
url = "https://www.halfbakedharvest.com/slow-cooker-chipotle-orange-street-tacos/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

ingredients = soup.find_all(itemprop="recipeIngredient")

def ingredients_to_obj(ingredients):
    all_ingredients = []
    for i in ingredients:
        try:
            amount = i.find_all("span","wprm-recipe-ingredient-amount")
            amount = amount[0].text
#             print(amount[0].text)
        except:
            amount = 'no amount'
            print('no amount')

        try:
            unit = i.find_all("span","wprm-recipe-ingredient-unit")
            unit = unit[0].text
#             print(unit[0].text)
        except:
            unit = 'no unit'
            print('no unit')

        try:
            name = i.find_all("span","wprm-recipe-ingredient-name")
            name = name[0].text
#             print(name[0].text)
        except:
            name = 'no name'
            print('no name')

        all_ingredients.append({'amount': amount, 'unit': unit, 'name': name})
    
    return all_ingredients

```

## Some Inspo

[Recipe finder](https://www.reddit.com/r/MealPrepSunday/comments/83pw0y/i_made_an_opensource_chrome_extension_to_make/)