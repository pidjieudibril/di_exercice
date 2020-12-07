let str1 = 'bonjour';
let str2 = 'Jose';

let str3 = str1.substring(6);

str1.substr(6);
let str4 = str2.substring(3);
 str2.substr(3);


console.log(str1.replace('r', str4) + ' ' + str2.replace('e', str3));
console.log(str1.replace(str1.charAt(6), str4) + ' ' + str2.replace(str2.charAt(3), str3));

let newWord = str2.substring(0,2) + str1.substring(2) + ' ' +str1.substring(0,2)+str2.substring(2);
console.log(newWord);