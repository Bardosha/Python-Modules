def healing_potion() -> str:
    from .elements import create_air, create_earth
    message = (f"Healing potion brewed with '{create_earth()}'"
               f" and '{create_air()}'")
    return message


def strength_potion() -> str:
    import elements
    message = (f"Strength potion brewed with '{elements.create_fire()}'"
               f" and '{elements.create_water()}'")
    return message
