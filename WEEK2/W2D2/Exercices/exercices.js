exercice 1
var number = prompt("Give me a number")
if (number%2 === 0) {
	console.log("x is an even number")
}
else{
	console.log("x is not an even number")
}

exercice 2
let x = 10
let y = 14
if (x < y) {
	console.log("y is biger than x")
}
else{
	console.log("its not y")
}

exercice 3
var user = prompt("Which language do you speak");
switch (user) {
	case "French":
	       alert("Bonjour");
	    break;
	case "English":
	       alert("Hello")
	    break;   
	case "Hebrew": 
	       alert("Shalom");
	    break;   
	default:
	       alert(":)")              
}

exercice 4
var user = prompt("What is your grade?");
if (user > 90){
	console.log("A")
	alert("A")
}
else if (user <= 90){
	console.log("B")
	alert("B")	
}
else if (user <= 80){
	console.log("C")
	alert("C")
}
else if (user < 70){
	console.log("D")
	alert("D")
}	


