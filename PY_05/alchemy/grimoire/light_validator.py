from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    is_valid = False

    for ingredient in allowed:
        if ingredient in ingredients.lower():
            is_valid = True

    if is_valid:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
