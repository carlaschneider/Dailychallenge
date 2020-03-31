ex1
let family = {
	number_of_parents: 2,
	number_of_children: 2,
	name_of_parents: ["Karen","Gerhard"],
	name_of_children: ["Alex","Carla"] ,
};
for (let x in family) {
  console.log(x)
}
for (let x in family) {
  console.log(family[x])
}


ex2
var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}
building.number_of_apt_by_level[1] 
building.number_of_apt_by_level[3]
building.name_of_tenants[1]
building.number_of_rooms_and_rent["Dan"][0]

i = 2010
if (i >1000) {
	alert("You have to inscrease the rent of Dan. And change the rent of Dan accordingly inside the object")
}
else{
	alert("everything is good")
}


