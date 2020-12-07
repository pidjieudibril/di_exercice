// verification de l'entrer d'un nombre 
/*
function verification(entree) {
    var seulement_ceci ="0123456789-+*%/.";
    for (var i = 0; i < entree.length; i++)
     if (seulement_ceci.indexOf(entree.charAt(i))<0 ) return false;
    return true;
   }

  function my_f(caractere) {


        window.document.display.value =
    window.document.calculatrice.affiche.value + caracteres;
  }
*/
 /*
  function resultat() {
  let dis=   document.getElementById("display");
  dis.innerHTML=caractere;
  console.log(caractere);
console.log(dis)    ;
}
*/

//fonction pour calculer
function pour_calculer() 
{ 
    let a = document.getElementById("display").value ;
    let b = eval(a) ;
    document.getElementById("display").value = b ;
} 
//fonction qui affiche la valeur
function my_f(val) 
{ 
    document.getElementById("display").value+=val ;
} 
//fonction qui efface l'écran 
function effacer() 
{ 
    document.getElementById("display").value = 0;
} 
/*
function number0() {
    document.getElementById('display').value += 0;
    memory += 0;
    return 0;
}

window.addEventListener("load", my_f(), false);

function toCelsius(f) {
    return (5/9) * (f-32);
  }
  document.getElementById("demo").innerHTML = toCelsius(77);
  */