

function wordsInStars(){

    let enter = prompt(' Enter several words (separated by commas).');
    
    let temp = enter.split(', ');
    let long = temp[0].length;
    let long1;

    for(let i =1; i <temp.length; i++){
        if(temp[i].length > long){
            long = temp[i].length;
            
        }
    }

    console.log('*'.repeat(long + 2));
    

    let blank = ' ';
    for(let k = 0; k < temp.length; k++){
        long1 = long - temp[k].length;
        let chaine = '*'+ temp[k];

        if(chaine.length < long + 1){
            chaine += ' '.repeat(long1);
        }
        console.log(chaine  +'*' );
    }
    console.log('*'.repeat(long + 2));
}
