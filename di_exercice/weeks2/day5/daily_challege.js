

  function beersong () {
      let bouteilles;
      let bouteillesRestantes;
      for (let i =99; i>=1; i--){
          if (i==1){
             bouteilles = 'bottles';
             bouteillesRestantes = 'No bottles of beer on the wall!';
          } 
          else {
             bouteilles = 'bottles';
             bouteillesRestantes = i-1 + 'bottles of beer on the wall!';
          }
          console.log(i + bouteilles + ' of beer on the wall,');
         /* console.log(i+ " " + bouteilles + " of beer,");
          console.log("Take one down, pass it around,");
          console.log(bouteillesRestantes);*/
        }
  }