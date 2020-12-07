// exercice 1 Age difference 

let one = parseInt(prompt('give the birthday year of the first person (YYYY)'));
let two = parseInt(prompt('give the birthday year of the second person(YYYY)'));
let younger ;
let oldest;


if(one >= two){
    younger = one;
    oldest = two;
}else {
    younger = two;
    oldest = one;
}

let difference = one - two;
let val = Math.abs(difference) + younger;

alert(' the date when the younger one is exactly half the age of the other is ' + val );

// exercice 2 : Zip codes

let code = prompt('Entrez un code zip');


if(code.length >= 5){
   if(code.charAt(0) == 'number' && code.charAt(1) == 'number' && code.charAt(2)== 'number' && code.charAt(3 ) == 'number'){


    alert('good!');
   } 
 } 

console.log('Good!');



