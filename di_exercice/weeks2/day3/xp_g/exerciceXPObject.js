// exercice 1 Attendance

let guestList = {
  Randy: "Germany",
  Karla: "France",
  Wendy: "Japan",
  Norman: "England",
  Sam: "Argentina"
};

let name = prompt('Enter your name');
let val = 0;
let nom = "";
let pays= "";

for(let x in guestList){
    if(name == x){
        //val = 1;
        //nom = x;
         console.log('Hi! I\'m  '+ x + ', I \'m from ' + guestList[x]);
         break;
        //pays = guestList[x];
    
    }
    else {
        console.log('Hi ! I\'m a guest');
    }

}
/*
    if(val == 1 ){
        console.log('Hi! I\'m  '+ nom + ', I \'m from ' + pays);
    } else {
        console.log('Hi ! I\'m a guest');
    }*/

    // exercice 2 Family


    let membre = {
        nom: 'Youego', nombre:4, quartier:'fougerolles'
    };
    console.log('the properties of the object membre are :');
    for(let x in membre){
        console.log( x);
        
       }
    console.log('the values of the object membre are :');
    for(let y in membre){
        console.log( membre[y]);
    }

  // exercice 3 Building Management

    let building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
};
console.log('the number of levels in the building is : ' + building.number_levels);
console.log(building.number_of_apt_by_level[1]);
console.log(building.number_of_apt_by_level[3]);
console.log(building.name_of_tenants[1] +'  '+ building.number_of_rooms_and_rent.Dan);
if(building.number_of_rooms_and_rent.Sarah[1] + building.number_of_rooms_and_rent.David[1] > building.number_of_rooms_and_rent.Dan[1]){
    console.log('Increase Dan\'s rent');
    building.number_of_rooms_and_rent.Dan[1] += 490;
    console.log('The new rent of  Dan is ' + building.number_of_rooms_and_rent.Dan[1]);
}

// exercice 4 Checking the BMI

let person1 ={
    fullName : 'Motue',
     mass : 30, 
     height: 1.20,
     bmi : self.mass/(self.height*self.height),
}

let person2 ={
    fullName : 'Elsa',
     mass : 20, 
     height: 1,
     bmi : self.mass/(self.height*self.height),
}

if(person1.bmi < person2.bmi){
    console.log(person2.fullName + ' has the bigguest BMI');
}else{
    console.log(person1.fullName + ' has the biguest BMI');
}