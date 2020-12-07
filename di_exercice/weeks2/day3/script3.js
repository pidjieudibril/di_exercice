// afficher chaque lettre du mot bonjour
/*let str = " bonjour"
for (let i=0; i<str.length;i++){console.log(str.charAt(i))};
// afficher les nombre paire compris entre 0 et 100
for (let i=0; i<=100;i++)
{
    if(i%2==0){console.log(i)}

};

for (let i=220; i<=180;i++){
    if(i%2==0){
        
        console.log(i+" "+"est paire")}

        else
        {
            console.log(i+" "+"est impaire")}
        };


let i=prompt("entrer une valeur compris entre 90 et 180");
for (let i=0; i<=180 & i>=90;i++)
{
    if(i%2==0){
        alert("le nombre est paire");
        console.log(i)}

        else
        {
            alert("le nombre est impaire");
            console.log(i)
        };
    
};

for (let i=0; i<=180 || i>=90;i++)
{
    if(i%2==0){console.log(i)
    alert("le nombre est paire");}
    if else (i%2!=0){
        console.log(i)

    };
    

};
*/
// utiliser typeof pour savoir le type 

/*
let names = ["john", "sarah",  23, "Rudolf", 34];
for (let i = 0; i < names.length; i++)
 {
        if(typeof(names[i]) != "string")

        {  //typeof pour le type
             continue; 
        }

        else if(typeof(names[i])=="string")
        {
            if(names[i].charAt(0)==names[i].charAt(0).toUpperCase()) {
            //charAt pour la position de la lettre
                console.log(names[i]);
            }   
            else{
                console.log(names[i].charAt(0).toUpperCase()+names[i].substring(1,names[i].length)); //
            }
        }   
        
    
}


let names = ["john", "sarah", 23, "Rudolf", 34];
for (let i=0; i<=names.length; i++)
{
    if (typeof(names[i]) !="string")
    {
        break;
    }
    else if(typeof(names[i])=="string")
    {
        console.log(names[i]);
    }

}
*/
// exercice 1 
 let mycolors= ["red", "blue","yellow", "black", "pink"];
 mycolors.forEach(element => console.log("my choise is " +element));

 for (let i=0; i<=mycolors.length-1; i++)
 {
   
         console.log("my " +" "+ i +" "+ "choise is" +mycolors[i]);	
     
 }

/*
 let mycolors= ["red", "blue","yellow", "black", "pink"];
 let suffix= ["st", "nd","rd", "th", "pink"];
 console.log(`my 2 ${suffix[1]} choise is ${color[1]}  `);
*/

//exercice 2 pour moi
/*let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// 
let sortBySensitivity = sensitivity => (a, b) => a.localeCompare( b, undefined, 
    { sensitivity }
  );
  let byAccent  = sortBySensitivity('accent');
  let accentSorted  = [...names].sort(byAccent);
  console.log(accentSorted);
  let society_name=" ";

  for (let i=0; i<=accentSorted.length;i++){
      console.log(accentSorted[i].charAt(0));
      society_name = society_name + accentSorted[i].charAt(0);
  }
  console.log(society_name);
//exercice 2 corrigé
  let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
  let order = names.sort();
  let society_name="";
  for (var i=0; i< names.length; i++){

    console.log(names[i].charAt(0));
    society_name = society_name + names[i].charAt(0);
}
console.log(society_name);

//exercice 3
let nbr = parseInt(prompt("entrer un nombre") ) ;
while (nbr < 10) {
  nbr= parseInt(prompt("entrer a nouveau le nombre")) ;
 
   console.log(nbr)
  // nbr++
  // alert("le nombre est correct");
}
*/
//exercice 3

let people = ["Greg", "Mary", "Devon", "James"]
for (let i = 0; i < people.length; i++) {

  console.log(people)

 
 people.splice(0, 1); 
// n définit le nombre d'éléments à supprimer,
// à partir de la position pos

 people.splice(2, 1, "jason"); 
people.push("dibril");
    

}
