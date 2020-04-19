let new_navbar = document.getElementById("navBar");
new_navbar.setAttribute("socialNetworkNavigation", "color:blue;");
let another_li = document.createElement("li")
another_li.innerText = "Logout"
let ul = document.querySelector("ul")
ul.append(another_li)