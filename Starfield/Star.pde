/**Objeto que representa una 'estrella' dentro del programa*/
class Star {
  // Posición en 3D de la estrella
  float x, y, z;
  
  /**Constructor del objeto. Inicializamos la posición de
   * de la estrella con valores aleatorios*/
  Star() {
    x = random(-width / 2, width / 2);
    y = random(-height / 2, height / 2);
    z = random(width / 2);
  }
  
  /**Actualizamos la estrella*/
  void update() {
    // Movemos la coordenada Z de la estrella en función de la velocidad
    z -= speed;
    
    // Si la estrella ha salido de la pantalla, reseteamos la posición de la
    // estrella a los valores iniciales para reutilizar la estrella
    if (z < 1) {
      x = random(-width / 2, width / 2);
      y = random(-height / 2, height / 2);
      z = width / 2;
    }
  }
  
  /**Función 'render' de la estrella. Dibuja la representación de la estrella
    * en la pantalla*/
  void show() {
    // Mapeamos las coordenadas X e Y en función de la coordenada
    // Z para dar la sensación de que realmente la estrella se
    // está moviendo en un espacio 3D, aunque teóricamente no sea así
    float vx = map(x / z, 0, 1, 0, width / 2);
    float vy = map(y / z, 0, 1, 0, height / 2);
    
    // Mapeamos el tamaño de la estrella en función de la coordenada Z
    // es decir, contra más 'alejada' esté la estrella, más pequeña será,
    // se hará más grande en caso contrario es decir, contra más 'cerca'
    // esté de nosotros, más grande se verá
    float radius = map(z, 0, width / 2, 16, 0);
 
    // Establecemos un color para dibujar en blanco e indicamos que no queremos
    // dibujar el trazo
    fill(255);
    noStroke();
    
    // Dibujamos una elipse con las coordenadas que hemos obtenido del anterior
    // mapeo y establecemos un tamaño para la estrella en base al mapeo del
    // tamaño anterior
    ellipse(vx, vy, radius, radius);
  }
}
