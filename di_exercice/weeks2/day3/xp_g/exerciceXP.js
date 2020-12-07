// exercice 1 YOur favorite color

let arr = ['red', 'babyblue', 'white', 'nude'];

for(let i = 0; i<arr.length; i++){

    console.log('My first choice is '+ arr[i]);

}


for(let i =0; i < arr.length; i++){

    let j = i+1;

    if(i == 0){
      console.log('My ' + j + 'st'+ ' choice is '+ arr[i]);  
    } else if(i == 1){
      console.log('My ' + j + 'nd'+ ' choice is '+ arr[i]);  
      } else{
          if(i == 2){
      console.log('My ' + j + 'rd'+ ' choice is '+ arr[i]);  
     } else{
        console.log('My ' + j + 'st'+ ' choice is '+ arr[i]);
     }
      }

  /* 
  another solution for the bonus (hint)

  let colors =  ['red', 'babyblue', 'white', 'nude'];
  let suffix = ['st', 'nd', 'rd', 'th'];
  console.log( ` My 2 ${suffix[1]} choice is $ {color[1]}`);


  
  */  

    
}
// exercice 2 Secret group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let name = [names[0].charAt(0)];

for(let i = 1; i< names.length; i++){
    name.push(names[i].charAt(0));
    }
    
    console.log(name.sort().join(''));

// exercice 3 Repeat the question

let number = prompt('enter a number greater than 10');

while(number < 10) {
    number = prompt('enter another one 10');


}



// exercice 4 List of people

let people = ["Greg", "Mary", "Devon", "James"];

for(let i of people){
    console.log(i);
}

people.shift();
console.log(people);
console.log('the command to remove \' Greg \' is people.shift()');
people.splice(2, 1, 'Jason');
console.log(people);
console.log('the command to replace \' James \' by \' Jason \' is people.splice(2,1\'Jason\')');
people.push('Joseline');
console.log('The command to add my name at the end is people.push(\'Joseline\')');

for(let i in people){
    if(people[i] == 'Mary'){
        console.log('Mary');
        console.log('the index of Mary is '+ i);
    }
}

let people1 = people.slice(1,3);
console.log(people1);
console.log(people.indexOf('Foo'));

let last = people[people.length-1];
console.log(last);


// exercice 5 Divisible by Three

let nombre = prompt('enter a number to test if it is divisible by three');
let tab = nombre.split('');
let valeur=0 ;
let val = tab.length;
console.log(tab);
for(let i = 0; i< tab.length; i++){
    valeur = valeur+ parseInt(tab[i]);
}
if(valeur%3 == 0){
    alert(true);
 } else{
     alert(false);
 }

 // exercice 6 Playing with numbers 
 
 let age = [20,5,12,43,98,55];
 let somme = 0;
 for(let i =0; i < age.length;i++){
     somme = somme + age[i];
 }
 console.log('the sum of all the elements in the array is ' + somme);

 let val1 = age[0];
 let i = 1;
 while(i<age.length){
     if(age[i] >= val1){
         val1 = age[i];
     } 
     i++;
 }
 console.log('The largest value in the array is ' + val1);