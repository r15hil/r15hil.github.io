import asyncio
import math
import os
import random

import aiohttp
import click


async def fetch_count(session, base_url):
    try:
        async with session.get(f"{base_url}?limit=1&offset=0") as response:
            response_data = await response.json()
            return response_data.get("data", {}).get("count", 0)
    except Exception:
        return 0


async def fetch_recipes(session, base_url, limit, offset):
    try:
        async with session.get(f"{base_url}?limit={limit}&offset={offset}") as response:
            response_data = await response.json()
            return response_data.get("data", {}).get("entries", [])
    except Exception:
        return []


async def fetch_recipe_details(session, recipe_slug):
    recipe_url = (
        f"https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/{recipe_slug}"
    )
    try:
        async with session.get(recipe_url) as response:
            recipe_data = await response.json()
            return recipe_data.get("data", {}).get("entry", {})
    except Exception:
        return {}


async def fetch_random_recipes(num_recipes):
    base_url = "https://production-api.gousto.co.uk/cmsreadbroker/v1/recipes"
    limit = 16

    async with aiohttp.ClientSession() as session:
        count = await fetch_count(session, base_url)
        total_pages = math.ceil(count / limit)

        # Randomly select pages to retrieve recipes from
        selected_pages = random.sample(range(total_pages), min(6, total_pages))

        tasks = [
            fetch_recipes(session, base_url, limit, page * limit)
            for page in selected_pages
        ]
        all_recipes_pages = await asyncio.gather(*tasks)
        recipes = [recipe for page in all_recipes_pages for recipe in page]

        # Randomly select the requested number of recipes
        selected_recipes = random.sample(recipes, min(num_recipes, len(recipes)))

        # Fetch details for each selected recipe
        recipe_detail_tasks = [
            fetch_recipe_details(session, recipe.get("url", "").split("/")[-1])
            for recipe in selected_recipes
        ]
        all_recipe_details = await asyncio.gather(*recipe_detail_tasks)

    return all_recipe_details


async def fetch_all_recipes():
    base_url = "https://production-api.gousto.co.uk/cmsreadbroker/v1/recipes"
    limit = 16

    async with aiohttp.ClientSession() as session:
        count = await fetch_count(session, base_url)
        total_pages = math.ceil(count / limit)

        tasks = [
            fetch_recipes(session, base_url, limit, page * limit)
            for page in range(total_pages)
        ]
        all_recipes_pages = await asyncio.gather(*tasks)
        recipes = [recipe for page in all_recipes_pages for recipe in page]

        # Fetch details for each recipe
        recipe_detail_tasks = [
            fetch_recipe_details(session, recipe.get("url", "").split("/")[-1])
            for recipe in recipes
        ]
        all_recipe_details = await asyncio.gather(*recipe_detail_tasks)

    return all_recipe_details


def print_recipe_list(all_recipes):
    print(f"Retrieved {len(all_recipes)} recipes with details.\n")
    for i, recipe in enumerate(all_recipes, start=1):
        print(f"[{i}] Title: {recipe.get('title')}")
        print(f"Description: {recipe.get('description', 'No description available')}\n")
        print(f"URL: https://www.gousto.co.uk/cookbook{recipe.get('url')}\n")


def generate_html_files(selected_recipes):
    for recipe in selected_recipes:
        recipe_title = recipe.get("url", "recipe").split("/")[-1]
        file_name = f"{recipe_title}.html"
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(
                    f"<html><head><title>{recipe.get('title')}</title></head><body>\n"
                )
                file.write(f"<h1>{recipe.get('title')}</h1>\n")
                file.write(
                    "<p>NOTICE: All of these recipes have been retrieved from the Gousto API. I do not claim ownership of any recipes in these files. These recipes are provided for informational purposes only, based on publicly available data from Gousto.</p>\n"
                )
                file.write(
                    f"<p><strong>Description:</strong> {recipe.get('description', 'No description available')}</p>\n"
                )
                file.write(
                    f"<a href='https://www.gousto.co.uk/cookbook/recipes{recipe.get('url')}'>View on Gousto</a><br><br>\n"
                )
                file.write(f"<h3>Ingredients</h3>\n<ul>\n")
                for ingredient in recipe.get("ingredients", []):
                    file.write(f"<li>{ingredient.get('label')}</li>\n")
                file.write("</ul><br><br>\n")
                file.write(f"<h3>Instructions</h3>\n")
                for instruction in recipe.get("cooking_instructions", []):
                    step_number = instruction.get("order")
                    clean_instruction = (
                        instruction.get("instruction", "")
                        .replace("<p>", "\n")
                        .replace("</p>", "\n")
                        .replace("<strong>", "")
                        .replace("</strong>", "")
                        .strip()
                    )
                    image = next(
                        (
                            img["image"]
                            for img in instruction.get("media", {}).get("images", [])
                            if img["width"] == 200
                        ),
                        None,
                    )
                    if image:
                        file.write(
                            f"<img src='{image}' alt='Step {step_number} Image'><br><br>\n"
                        )
                    file.write(
                        f"<h4>Step {step_number}</h4>\n<p>{clean_instruction}</p><br><br>\n"
                    )
                file.write("</body></html>")
            print(f"HTML file '{file_name}' has been generated.")
        except Exception:
            print(f"Failed to generate HTML file for recipe: {recipe.get('title')}")


@click.command()
@click.option("--num_recipes", default=1, help="Number of recipes to retrieve")
@click.option(
    "--generate_all", is_flag=True, help="Generate HTML files for all recipes"
)
def main(num_recipes, generate_all):
    try:
        if generate_all:
            all_recipes = asyncio.run(fetch_all_recipes())
            generate_html_files(all_recipes)
        else:
            all_recipes = asyncio.run(fetch_random_recipes(num_recipes))
            print_recipe_list(all_recipes)

            choice = click.prompt(
                "Enter the number of the recipe(s) you want instructions for (comma-separated)",
                type=str,
            )
            recipe_indices = [int(i) for i in choice.split(",")]
            selected_recipes = [
                all_recipes[i - 1] for i in recipe_indices if 1 <= i <= len(all_recipes)
            ]
            generate_html_files(selected_recipes)
    except Exception as e:
        print(f"An error occurred, {e}")


if __name__ == "__main__":
    main()
