def city_function(city, country, population=''):
    if population:
        city_name = f'{city} - {country}: {population}'
    else:
        city_name = f'{city} - {country}'
    return city_name.title()