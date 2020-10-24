---
layout: single
title: 'PROJECT_RecipeScraper pt2 -- October 23, 2020'
tags: PROJECT_RecipeScraper
classes: wide
---


```python

import requests
from bs4 import BeautifulSoup


url = "https://www.halfbakedharvest.com/wprm_print/73488"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


recipe_name = soup.find_all('h2', 'wprm-recipe-name')[0].text.strip()
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


        all_ingredients.append({'url': url, 'recipe_name': recipe_name,'amount': amount, 'unit': unit, 'name': name})
    
    
    return all_ingredients

```