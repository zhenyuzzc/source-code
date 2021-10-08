def city_functions(city,country,population=''):
    if population:
        cf = f"{city}-{country}-population {population}"
    else:
        cf = f"{city} {country}"
    return cf
    