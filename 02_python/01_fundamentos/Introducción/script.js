function calcularTotal(arrayOfNumbers) {
   
    var suma = arrayOfNumbers[0];
   
    for(var i=0; i<arrayOfNumbers.length; i++) {
      suma += arrayOfNumbers[i];
      console.log("La suma actual es " + suma, "en el bucle", i);
    }
     
    console.log("La suma total es " + suma);
     
  }
     
  calcularTotal([2, 4, 6]);