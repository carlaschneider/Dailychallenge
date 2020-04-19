function playTheGame(){
    let a = confirm("You want to play a game ?");
    if (a === true){
       let answer = prompt("Put a number beetween 0 and 10");
        if (answer != NaN){
          alert("Sorry it's not a number, Bye");
        } else if (answer < 0 || answer > 10){
	      alert("Sorry it's not a good number, GoodBye");
        }else {
           let computerNumber = random(0, 10)
        }

    } else{
       alert("No problem, GoodBye")
    }   

      function test(myNumber,computerNumber){
	     if (myNumber = computerNumber){
		   alert("You Won!");
	     }else if (myNumber > computerNumber){
		   alert("You are bigger try angain ;)")
	     }else if (myNumber < computerNumber) {
		   alert("You are smaller try again ;)")
	     }else{
		   alert("You don't find the number was" + computerNumber)
	     }
      }

}


 //function playTheGame(){
  //  let a = confirm("You want to play a game ?");
  //  if (a === true){
    //  let answer = prompt("Put a number beetween 0 and 10");
      //  if (answer != NaN){
        //  alert("Sorry it's not a number, Bye");
      //  } else if (answer < 0 || answer > 10){
	  //    alert("Sorry it's not a good number, GoodBye");
       // }
        //else{
       // 	let computerNumber = random(0, 10)
      //  }

   // } else{
    //   alert("No problem, GoodBye")
   // }   

     // function test(myNumber,computerNumber){
	 //    if (myNumber = computerNumber){
	//	   alert("You Won!");
	 //    }else if (myNumber > computerNumber){
		//   alert("You are bigger try angain ;)")
	    // }else if (myNumber < computerNumber) {
		//   alert("You are smaller try again ;)")
	   //  }else{
		//   alert("You don't find the number was" + computerNumber)
	   //  }
     // }

//}