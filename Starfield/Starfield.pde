
// Se crea un array de objetos del tipo estrella
Star[] stars = new Star[800];

// Se declara una variable global para controlar la velocidad de
// las estrellas
float speed;

/**Método que inicializa el programa*/
void setup() {
  
  // Establece el tamaño de la ventana en 600x600 píxeles
  size(600, 600);
  
  // Rellena el array de estrellas que hemos definido anteriormente
  // con objetos del tipo estrella
  for (int i = 0; i < stars.length; i++) {
    stars[i] = new Star();
  }
}

/**Método que se ejecuta indefinidamente durante el programa.
 * Sirve para actualizar todos los componentes del programa
 * y para dibujar los objetos*/
void draw() {
  // Mapeamos la velocidad de las estrellas con la posición
  // horizontal del ratón. Es decir, la velocidad de las estrellas
  // variará dependiendo de la posición horizontal del ratón en la
  // ventana, contra más a la derecha de la pantalla esté el ratón
  // más velocidad tendrá la estrella y contra más a la izquierda
  // de la ventana esté más lento irá
  speed = map(mouseX, 0, width, 0, 20);
  
  // Establecemos un color de fondo negro
  background(0);
  
  // Establecemos el punto de origen, donde queremos empezar a
  // dibujar, en el centro de la ventana
  translate(width / 2, height / 2);
  
  // Recorremos completamente el array de las estrellas,
  // dibujamos y actualizamos cada una de las estrellas
  // que lo componen.
  for (int i = 0; i < stars.length; i++) {
    stars[i].update();
    stars[i].show();
  }
}
