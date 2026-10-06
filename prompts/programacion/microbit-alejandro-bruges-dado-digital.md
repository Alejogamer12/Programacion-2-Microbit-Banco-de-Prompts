# Prompt principal - Dado Digital D6

## Datos

**Estudiante:** Alejandro Bruges  
**Grado:** 11  
**Asignatura:** Programación 2  
**Modalidad:** Hardware y Software  
**Institución:** I.E.D.T. INEM Simón Bolívar  
**Año escolar:** 2026

## Prompt

Soy Alejandro Bruges, estudiante de grado 11 de la modalidad Hardware y Software de la I.E.D.T. INEM Simón Bolívar. Estoy cursando Programación 2 durante el año escolar 2026.

Estoy comenzando a aprender programación, así que necesito crear un programa sencillo, corto, ordenado y fácil de entender. No quiero un código complicado. Quiero poder comprender cada parte y después explicarla con mis propias palabras.

### Proyecto

Quiero crear un **Dado Digital D6 para una BBC micro:bit real**.

### Objetivo

Cuando agite físicamente la micro:bit debe aparecer en su matriz LED un número al azar entre 1 y 6, como si estuviera lanzando un dado normal. Cada vez que vuelva a agitar la placa debe poder aparecer un nuevo número.

### Funcionamiento

Al encender la micro:bit, el programa debe quedar esperando. Cuando yo agite la placa, debe detectar ese movimiento con el acelerómetro. Después debe generar un número entero al azar. Los únicos resultados permitidos son 1, 2, 3, 4, 5 y 6.

Después debe mostrar el resultado en la matriz LED. Al terminar, debe volver a esperar para poder realizar otro lanzamiento.

### Entrada

La entrada será agitar físicamente la micro:bit. Utiliza el acelerómetro integrado para reconocer el movimiento.

### Proceso

Cuando se detecte el movimiento, genera un número al azar entre 1 y 6. No debe aparecer 0, 7 ni ningún número fuera de ese rango.

### Salida

Muestra el número obtenido directamente en la matriz LED de la micro:bit.

### Nivel del código

Recuerda que soy principiante. Quiero un código corto, sencillo, ordenado, fácil de leer, fácil de probar y fácil de explicar. No agregues cosas innecesarias solamente para hacer que parezca más avanzado.

### Requisitos

El programa debe estar escrito en MicroPython para BBC micro:bit. Debe utilizar una función sencilla, una variable, una condición, una repetición, el acelerómetro y la matriz LED.

La función puede llamarse `tirar_dado()`. La variable donde se guarda el resultado puede llamarse `numero`. La condición debe comprobar si la micro:bit fue agitada. La repetición debe permitir varios lanzamientos.

No utilices Internet, sensores externos, pantallas externas ni partes que no sean necesarias.

### Explicación solicitada

Después del código explica con palabras sencillas qué hace el programa, cuál es la entrada, el proceso y la salida, dónde están la función, la variable, la condición y la repetición, y cómo se genera el número.

Explica también este recorrido:

Inicio → espera → movimiento → condición → función → número al azar → pantalla → volver a esperar.

### Revisión

Comprueba que solamente genere números del 1 al 6, detecte cuando se agita, tenga una función, una condición y una repetición, muestre el resultado, permita varios lanzamientos y siga siendo corto y entendible.

### Prueba física

Prepara estos pasos:

1. Cargar el programa.
2. Encender la micro:bit.
3. Agitarla una vez.
4. Comprobar que aparece un número.
5. Agitarla varias veces.
6. Comprobar que todos los resultados estén entre 1 y 6.
7. Comprobar que siga funcionando.
8. Reiniciar la placa.
9. Volver a agitarla.
10. Comprobar nuevamente el resultado.

No inventes resultados de pruebas que todavía no se hayan realizado.

### Registro

Preparar un registro con: **Qué probé | Resultado | Cambio realizado**.

Incluir carga, inicio, movimiento, número mostrado, rango del 1 al 6, varios lanzamientos, reinicio y prueba final.

### Posibles problemas

Explica de forma sencilla qué revisar si el programa no carga, aparece un error, no reconoce el movimiento, no aparece el número, aparece un número incorrecto, solamente funciona una vez o deja de responder.

### Evidencia real de la prueba física

**FALTA AQUÍ LA FOTO**

### Reflexión

Después de la prueba responder: ¿qué parte ayudó a crear la IA?, ¿qué partes revisé y entendí yo?, ¿la primera versión funcionó?, ¿tuve que corregir algo?, ¿qué aprendí al probar el programa?, ¿qué diferencia encontré entre tener el código escrito y verlo funcionando realmente? y ¿qué podría mejorar del prompt?

La explicación puede ser completa, pero el código debe mantenerse pequeño, sencillo y entendible.
