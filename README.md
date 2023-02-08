# Discord Spellcast Helper
#### By fabaindaiz


### Use
1. Escribe las letras del tablero en una sola linea en el orden izquierda -> derecha y luego arriba -> abajo
2. Escribe las coordenadas de los multiplicadores correspondientes y dejar en blanco si no aplica (ej. 34 o 01)
3. Para activar el modo swap (considerar un swap) se debe poner un 1, en otro caso no se activará
4. El software retornará una lista ordenada con el puntaje, la palabra sin swap, la palabra con swap (si no es palabra swapeada ambas seran iguales) y la coordenada de la letra inicial

- Las coordenadas funcionan con dos digitos numericos no separados con valores de 0 a 4


# Ejemplo de respuesta
```bash
Init solver
Insert a gameboard: iowacijiesraaenredpeiatoe
Insert 2x cord:
Insert DL cord: 00
Insert TL cord:
Use swap?:1
[[32, 'ceapened', 'cheapened', (4, 0)], [32, 'ceapened', 'cheapened', (4, 0)], [31, 'wiened', 'wizened', (2, 0)], [31, 'wiened', 'wizened', (2, 0)], [31, 'wiened', 'wizened', (2, 0)], [30, 'ceapens', 'cheapens', (4, 0)], [30, 'ceapens', 'cheapens', (4, 0)], [29, 'waened', 'wakened', (2, 0)], [29, 'waened', 'wakened', (2, 0)], [29, 'waened', 'wakened', (2, 0)], [29, 'topaes', 'topazes', (2, 4)], [29, 'topaes', 'topazes', (2, 4)], [29, 'topaes', 'topazes', (2, 4)], [29, 'topaes', 'topazes', (2, 4)], [29, 'topaes', 'topazes', (2, 4)], [29, 'topaes', 'topazes', (2, 4)], [28, 'weaens', 'weakens', (2, 0)], [28, 'ascened', 'ascended', (3, 0)], [28, 'weaens', 'weakens', (2, 0)], [28, 'ceapen', 'cheapen', (4, 0)]]
```


### Credits
- [wordlist_english.txt](https://github.com/jacksonrayhamilton/wordlist-english)