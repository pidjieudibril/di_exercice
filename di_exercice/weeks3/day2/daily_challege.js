

let libButton = document.getElementById('lib-button');

let libIt = function() {
    let storyDiv = document.getElementById("story");


let inputs = document.querySelectorAll('input');
let tab = [];
for (let i of inputs) {
    tab.push(i.value)
}
console.log(tab);
storyDiv.innerHTML = `My name is ${tab[0]}, im ${tab[1]}, and I like ${tab[2]}. }`

};
libButton.addEventListener ('click',libIt);