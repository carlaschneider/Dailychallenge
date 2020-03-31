// Tri des bulles 
let bubbleSort = (arr) => {
  // Longueur du tableau
  let n = arr.length;
  
  for(let i = 0; i < n - 1; i++){
    for(let j = 0; j <= n - i - 1; j++){
       // Permute les nombres
        if(arr[j] < arr[j+1]){
          [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
        }
    }
  }
  
  return arr;
}
console.log(bubbleSort([5,0,9,1,7,4,2,6,3,8]));
bubbleSort.toString([5,0,9,1,7,4,2,6,3,8])
