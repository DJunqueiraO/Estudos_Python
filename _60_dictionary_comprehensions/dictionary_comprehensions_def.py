
cities_in_F = {'New York': 32, 
               'Boston': 75, 
               'Los Angeles': 100, 
               'Chicago': 50}

def check(temp: int):
    if temp >= 70:
        return 'HOT'
    elif temp >= 40:
        return 'WARM'
    else:
        return 'COLD'

desc_cities = {key: check(temp=value) for (key, value) in cities_in_F.items()}

print(desc_cities)
