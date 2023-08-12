def describe_city(city, country = "Spain"):
    city = input("Name a City: \n (enter quit to exit)")
    country = input("Now name the country in it located \n ")
    print(f"The beautiful city of {city} is located in the {country}. ")
    if city == "quit":
            break
    

describe_city("\n")
describe_city("Portugal", "Europe")
describe_ciry("Franch", "Europe")

#improve this code like the chatGPT generated
