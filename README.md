# Discord Spellcast Helper
#### By fabaindaiz


### Use
1. Write the letters on the board in a single line following the order left -> right and then up -> down
2. Write the coordinates of the corresponding multipliers and leave blank if not applicable (eg 34 or 01)
3. To activate the swap mode (consider the use of a swap) you must put a 1, otherwise it will not be activated
4. The software will return an ordered list with the score, the word without swap, the word with swap (if it is not a swapped word both will be the same) and the coordinate of the initial letter

- The coordinates work with two non-separated numerical digits with values from 0 to 4


# Sample answer
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