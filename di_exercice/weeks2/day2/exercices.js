
//exercice 1
let x = 25;
let y = 11;
if(x>y){
    console.log(x + ' is the bigguest number ' );
} else if( x == y){
    console.log(x + ' is egual to' + y);
}else{
    console.log(y + ' is the bigguest number ');
}

//exercice 2 : Chihuahua

let newDog = 'Chihuahua';

console.log(newDog.length);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if(newDog == 'Chihuahuah'){
    console.log(' I love Chihuahua, it\'s my favorite dog breed');

} else {
    console.log('I dont care, I prefer cats');

}


// exercice 3 : Even or not even

let number = prompt('Enter a number');

if(number % 2 == 0){
    alert(number + ' is an even number!!');
}else{
    alert(number + ' is not an even number!');
}


// exercice 4 : Group chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

switch(users.length){
    case 0:
    console.log('no one is online ');
    break;
    case 1:
    console.log(users[0] + ' is online');
    break;
    case 2:
    console.log(users[0] + ' and ' + users[1] + ' are online');
    break;
    default:
        let val = users.length -2;
    console.log(users[0] + ',  ' + users[1] + ' and ' + val  + ' more are online');
}

