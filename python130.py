from typing import TypedDict


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation:
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs = NutritionInformation


def get_nutrition_from_spoonacular(recipe_name: str) -> RecipeNutritionInformation:
    return {
        "calories": 1313,
        "fat": 13131,
        "protein": 30,
        "carbs": 50
    }

