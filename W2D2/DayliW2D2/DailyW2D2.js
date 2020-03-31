let string = "This dinner is not that bad!"

let not = (string.search("not"))
let bad = (string.search("bad"))
let sub = (string.substring("not"))
console.log(sub)
console.log(bad)
console.log(not)

if (not < bad){
	string = string.slice(0, "not")
	string = (string + "This dinner is good")
	console.log(string)
}