let str = prompt('Create a string that has the word not and bad inside');

let one = str.indexOf('not');
let two = str.indexOf('bad');
let long = str.length;

if(one >0 || two >0 ) {

	alert("the first appearance of the substring not is at " + one + "position");

alert("the first appearance of the substring bad is at " + two + "position");


alert(str.substr(0, one) + ' good ' + str.substr(two + 3, long - 1) );

} else {
	console.log(str);
}


