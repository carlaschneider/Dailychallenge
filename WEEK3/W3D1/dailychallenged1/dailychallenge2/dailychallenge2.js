let body = document.getElementsByTagName("body");

let planetlist = ["Mercure", "Mars", "Saturne", "La Terre", "Jupiter"];

for(planets of planetlist){
	let planet = document.createElement("div");
	planet.innerHTML = planets;
	body[0].appendChild(planet);
	planet.setAttribute("class", "planet");
	planet.setAttribute("id", planets);
}

document.getElementById("Mercure").style.backgroundColor = "red"
document.getElementById("Mars").style.backgroundColor = "brown"
document.getElementById("Saturne").style.backgroundColor = "pink"
document.getElementById("La Terre").style.backgroundColor = "blue"
document.getElementById("Jupiter").style.backgroundColor = "purple"

 alert("Click on planet to move it")

 "Mercure".addEventListener("click" , Passing)
 "Mars".addEventListener("click" , Passing)
 "Saturne".addEventListener("click" , Passing)
 "La Terre".addEventListener("click" , Passing)
 "Jupiter".addEventListener("click" , Passing)

function Passing(){
	let start = Date.now();

	let timer = setInterval(function(){
		let timePassed = Date.now() - start;
		console.log(timePassed)
		"Mercure".style.left =  timePassed / 5 + "px";
		if(timePassed > 2000){
			clearInterval(timer)
		}
	}, 20);
}



