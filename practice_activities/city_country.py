def city_country(city, country):
    formal_city = (f"{city}, {country}")
    return formal_city.title()

while True:
    city = input("Enter City name: ")
    country = input("Enter Country of the city: ")
    formal_city = city_country(city, country)
    print(formal_city)

    continues = input("Enter (y) to continue and (n) to exit")
        
    if continues == "n":
        break