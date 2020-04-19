let list1 = document.getElementsByClassName('list')[0]
list1
list1.lastElementChild.innerText = "Richard"
list1.firstElementChild.innerText = 'Carla'
let list2 = document.getElementsByClassName('list')[1]
list2.firstElementChild.innerText = 'Carla'
let p = document.createElement('p')
p.innerText = "Hey study"
list1.appendChild(p)
list2.appendChild(p)
