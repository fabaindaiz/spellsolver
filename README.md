# Discord Spellcast Helper
#### By fabaindaiz


### Use
1. Write the letters on the board in a single line following the order left -> right and then up -> down
2. Write the coordinates of the corresponding multipliers and leave blank if not applicable (eg 34 or 01)
3. To activate the swap mode (consider the use of a swap) you must put a 1, otherwise it will not be activated
4. The software will return an ordered list with the score, the word without swap, the word with swap (if it is not a swapped word both will be the same) and the coordinate of the initial letter

- The coordinates work with two non-separated numerical digits with values from 0 to 4


# Sample answer
- Normal mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 
[(48, 'vomits', (3, 1)), (48, 'vomits', (3, 1)), (48, 'vomits', (3, 1)), (48, 'vomits', (4, 2)), (48, 'vomits', (3, 1)), (48, 'vomits', (4, 2)), (48, 'vomits', (3, 1)), (48, 'vomits', (3, 1)), (48, 'vomits', (4, 2)), (48, 'vomits', (4, 2)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (44, 'motels', (2, 3)), (42, 'motors', (2, 3)), (42, 'motors', (2, 3)), (42, 'amigos', (1, 4))]
```

- Swap mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 1
[(66, 'zoftig', (3, 2), 'z'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (3, 1), 'y'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (3, 1), 'y'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (3, 1), 'y'), (58, 'vomitory', (4, 2), 'y'), (58, 'comfits', (3, 2), 'c'), (58, 'vomitous', (4, 2), 'u'), (58, 'comfits', (3, 2), 'c'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (4, 2), 'y'), (58, 'vomitory', (3, 1), 'y'), (58, 'vomitous', (4, 2), 'u'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (3, 1), 'y'), (58, 'comfits', (3, 2), 'c'), (58, 'vomitous', (3, 1), 'u'), (58, 'vomitory', (3, 1), 'y')]
```


### Credits
- [wordlist_english.txt](https://github.com/jacksonrayhamilton/wordlist-english)