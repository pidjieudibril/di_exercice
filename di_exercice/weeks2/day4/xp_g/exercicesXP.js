// exercices 1 Keyless car

//1 - 
/*
let age = prompt('Enter your age');

function checkDriverAge(val){
    if(val < 18){
        alert("Sorry, you are too yound to drive this car. Powering off");
    }else if (val > 18){
        alert("Powering On. Enjoy the ride!");
    }else if (val == 18){
        alert("Congratulations on your first year of driving. Enjoy the ride!");
    }

}
alert(checkDriverAge(Number(age)));


// 2 -

function checkDriverAge1(age1){
    if(age1 < 18){
        console.log("Sorry, you are too yound to drive this car. Powering off");
    }else if (age1 > 18){
        console.log("Powering On. Enjoy the ride!");
    }else{
        console.log("Congratulations on your first year of driving. Enjoy the ride!");
    }

}*/

// exercice 2 Is_blank


function is_Blank(chaine){
    if(chaine == ''){
        console.log(true);
    }else {
        console.log(false);
    }
}
console.log(is_Blank('')); 
console.log(is_Blank('abc')); 

// exercice 3 Abbrev_name

function abbrev_name(chaine){
    let temp = chaine.split(' ');
    let val = temp[0];
    console.log(temp.length);
    for(i = 1; i <temp.length; i++){
        val = val + ' ' + temp[i].charAt(0) + '.';
    }
  return val ; 
}
console.log(abbrev_name("Robin Singh"));


// exercice 4 : SwapCase

function swapCase(chaine){

    let temp = chaine.split('');

    for(let i = 0 ; i < temp.length; i++){

        if(temp[i] == temp[i].toUpperCase()){
            temp[i] = temp[i].toLowerCase();
        }else{
            temp[i] = temp[i].toUpperCase();
        }
    }
    return temp.join('');
}

console.log(swapCase('The Quick Brown Fox' ));

// exercice 5 : Amazon shopping

let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
};

function checkBasket(){
    let entre = prompt('What item do you want?');
    for(let x in amazonBasket){
        if(entre == x){
            alert('The item is in the basket');
        }else{
            alert('The item is not in the basket');
        }
    }
}


// exercice 6 : What’s In My Wallet ?

let monnaie= [];

function changeEnough(monnaie, total){
    let val=0;
    for(i=0; i<4; i++){
        val = val + (monnaie[i] * 0.01);
    }
    val += (monnaie[0]*0.25);
    val += (monnaie[1]*0.1);
    val += (monnaie[2]*0.5);
    val += (monnaie[3]*0.1); 

    return(val >= total);
}

// exercice 7 : Shopping List

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList= ['banana', 'orange', 'apple'];

function myBill(){
    let price = 0;
    for(let i = 0; i <3; i++){
        for(let x in prices){
            if(shoppingList[i] == x){
                price += prices[x];
            }
        }

    }
    return price;
}
console.log(myBill());

// bonus 

function myBills(){
    let price = 0;
    for(let i = 0; i<3; i++){
        for(let x in stock){
            if(shoppingList[i]== x){
                for(let y in prices){
                    if(shoppingList[i] == y){
                        price += prices[y];
                    }
                }
            }
        }
    }
}


// exercice 8 : Find The Multiples Of 23


function vingtTrois(){
    let mul = 0;
    for(let i = 0; i< 500; i++){
        if(i % 23 == 0){
            console.log(i);
            mul += i;
        }
    }
    return mul;
}

function vingtTrois1(){
    let mul = 0;
    let tab= [];
    for(let i = 0; i< 500; i++){
        if(i % 23 == 0){
            tab.push(i);
           
            mul += i;
        }
    }
    console.log('Elements : ' + tab.join(' , ') );
    console.log('Sum : ' + mul);
    
}

// exercice 9 : Omnipresent Value

function isOmnipresent(arrArr, val){
    let tab = [];
    let test = 1;
    for(let i = 0 ; i < arrArr.length; i++){
        tab = arrArr[i];
        for(let j=0; j<tab.length; j++){
            if()
        }


    }
}