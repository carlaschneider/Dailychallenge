#exercice1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
for list in zip (keys, values):
    print(list)

#exercice2
store = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain":  ["red"], "US": ["pink", "green"]},
}
print(store)
store["number_stores"] = 2
print(store)
print("The client of Zara", store["type_of_clothes"])
store["country_creation"] = "Spain"
print(store)
store["international_competitors"].append("Desigual")
print(store)
del store["creation_date"]
print(store)
print(store["international_competitors"][-1])
us_colors = store["major_color"]["US"]
#print(f"The major color in USA: {us_colors [0]} {us_colors [1]}") Sans loop
text = "The major color in USA: "
for color in store["major_color"]["US"]:
    text+= color+" "
print(text)
print(len(store))
for key, value in store.items() :
    print (key)

more_on_store = {
    "creation_date": 1975,
    "number_stores": 10000,
}
print(more_on_store)
store.update(more_on_store)
print(store)

