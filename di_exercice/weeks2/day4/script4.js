//exerci1
/*
function display_age(myage) {
    console.log(`the age of my mum is" ${myage*2} and the age of my dad is ${myage*2*1.2}` )
    
}
display_age(10);
display_age("je");

//exerci 2

function display_mum_age(myage) {
    return myage*2;
    
}
let a = parseInt (prompt("tell me your age"));

alert(" the double of age of my mum is "+" "+display_mum_age(a));

//exercice 1

function checkDriverAge( age){

   
if (Number(age) < 18) {
    alert("Sorry, you are too yound to drive this car. Powering off");
} else if (Number(age) > 18) {
    alert("Powering On. Enjoy the ride!");
} else if (Number(age) === 18) {
    alert("Congratulations on your first year of driving. Enjoy the ride!");
}
    
}
console.log(checkDriverAge(50));

//exercice 2
function fonction_chaine_vide_ou_non(vide_ou_non) {
    if (typeof(vide_ou_non) !="string")
    return false;
    else
    return true;
    
    return maChaine.length === 0;
}
console.log(fonction_chaine_vide_ou_non("14"));


//exercice 2 corrigé
const is_blank= str =>
{ if(str.length==00){return true;} else return false;} 
console.log(is_blank("ff"))


// exercice 3



function abbrev_name(input, to) {
    var states = [
        ['Robin singh', 'Robin S'],];
   
    

        if (to == 'abbr'){
            input = input.replace(/\w\S*//*g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
            for(i = 0; i < states.length; i++){
                if(states[i][0] == input){
                    return(states[i][1]);
                }
            }    
        } else if (to == 'name'){
            input = input.toUpperCase();
            for(i = 0; i < states.length; i++){
                if(states[i][1] == input){
                    return(states[i][0]);
                }
            }    


    
}
console.log(abbrev_name("Robin Singh"));

*/
/*
function abbrev_name(input, to)
 {


        var states = [ ['Robin singh', 'Robin S'],];
        if (input == 'Robin singh') {
            input = input.replace(/\w\S*//*g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
            
        for(i = 0; i < states.length; i++){
                if(states[i][0] == input){
                    return(states[i][1]);
                }
            }    


/*
            else if (to == 'Robin S'){
                input = input.toUpperCase();
                for(i = 0; i < states.length; i++){
                    if(states[i][1] == input){
                        return(states[i][0]);
                    }
                }    
            }
            
        }

}

console.log(abbrev_name("jhgytui"));
*/

let strin =" salut toi hi"
let g= strin.split(" ") // permet de transformer  un string en tableau 
g.join // remet dans le bon ordre

// exercice 4
/*
function reverseCase(input) {
    var output = [];
    for(var char in input) {
        var character = input[char];
        if(character == character.toUpperCase())
            output.push(character.toLowerCase());
        else
            output.push(character.toUpperCase());
    }
    return output.join('');
}
console.log(reverseCase("The Quick Brown fox "))
*//*
function reverseCase(change)

{
    var per= [];
    
for (let i = 0; i < change.length; i++) {
    var character = change[i];
    if (character == character.toUpperCase())
    {
        per.push(character.toLowerCase());
    }
    else
    {
        per.push(character.toUpperCase());
    }   
}
return per.join('');

}
console.log(reverseCase("The Quick Brown fox "))
*/
//exercice 5
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket(elt) {
    let recherche=prompt("entrer ")
    if (amazonBasket[elt] ){
        console.log("l'element se trouve dans le panier");
        
    }
    else
    {
        console.log(" rien a signaler ");
    }
        
      }
      checkBasket("glasses");