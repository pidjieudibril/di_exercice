

// exercice 1 : The world translator

let language = prompt('Which language do you speaks? French, English or Hebrew?');

switch(language){
    case 'French':
        alert('Bonjour!');
    break;
    case 'English':
        alert('Hello');
    break;
    case 'Hebrew':
        alert('Shalom');
    break;
    default:
        alert('01110011 01101111 01110010 01110010 01111001');
}


// exercice 2 : The grade assigner

let grade = prompt('What is your grade?');


if( grade>90 ){

    console.log('A');

} else if (grade > 80 && grade <= 90 ){

    console.log('B');
} else {
    if(grade >= 70 && grade <= 80){
        console.log('C');
    } else{
        console.log('D');
    }
}




// exercice 3 : verbing

let verb = prompt('enter a verb!');
let longueur = verb.length ;

if(longueur >= 3){

    if(verb[longueur-1] == 'm' || verb[longueur-1] == 'n'){
        console.log(verb + verb[longueur-1] + 'ing');

    }

    if(verb[longueur-3] == 'i' && verb[longueur-2] == 'n' && verb[longueur-1] == 'g'){
        console.log(verb.substr(2, verb.length-1)+'ly');
    }

    if(verb[longueur-1] == 'e' || verb[longueur-1] == 'a' || verb[longueur-1] == 'o'){
        console.log(verb.substr(0,verb.length-1)+ 'ing');
    }
    
}else{
    console.log(verb);
}

