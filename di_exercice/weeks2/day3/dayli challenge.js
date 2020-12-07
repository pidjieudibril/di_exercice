let list_number = [45,10,2,60,0,25];
console.log("before" +list_number);
let temp;
for (let i= 0; i< list_number.length; i++) {
    for (let j = 0; j < list_number.length; j++) {
      if(list_number[j]<list_number[j+1]) {
          temp=list_number[j+1];
          list_number[j+1]=list_number[j];
          list_number[j]=temp;// si on utilisait seulement la boucle j on devait avoir 10 2 45 0 25 60

      } 
        
    }
    
    
}
console.log(list_number);