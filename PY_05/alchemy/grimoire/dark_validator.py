from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = False

    for ingredient in allowed:
        if ingredient in ingredients.lower():
            is_valid = True

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
