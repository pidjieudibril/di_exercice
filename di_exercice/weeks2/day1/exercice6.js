// ercercice 1

console.log(5 >= 1);
console.log(0 === 1);
console.log(4 <= 1);
console.log(1 != 1);
console.log("A" > "B");
console.log("B" < "C");
console.log("a" > "A");
console.log("b" < "A");
console.log(true ===  false);
console.log(true != true);

// exercice 2 

let c;
let a = 34;
let b = 21;
a = 2;
console.log(a + b);
console.log(c);
console.log(3 + 4 + '5');
let val1 = prompt(' Entrez une serie de dentiers séparés par des virgules ');

let val2 = val1.split(",");

alert(val2.reduce((a,b)=> a*b));


let n = prompt(' Entrez une valeure entière ');
let mot;

let milieu = 'o';

if(n%2 > 2) {
   milieu = milieu.repeat(n);
   mot = 'B' + milieu + 'm';

	if( n % 2 == 0){
		console.log(mot  + ' !');
	}

	if( n % 5 == 0){
		console.log(mot.toUpperCase);
	} 


} else {
		console.log('boom');
	}

console.log(milieu);