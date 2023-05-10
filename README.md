# Discord Spellcast Helper
#### By fabaindaiz

Spellsolver is a software that helps to search for the best possible word in Spellcast discord activity. Spellsolver uses a trie to store the valid words, and then iteratively tries all the possible combinations of letters on the board, discarding the ones that don't make valid words and keeping the ones that do.

- Initialization of the trie structure to store valid words can take anywhere from 10 to 30 seconds and uses approximately 1 GB of ram memory, but allows all spellsolver queries to be executed in less than a second.
- I have planned to implement double swap, but with some algorithm that gives good results in a reasonable time (any ideas?)

### GraphicUI instruction
1. Install tkinter and execute graphicui.py
2. Write the letters on the board in the interface table
3. Use the right click to select letter modifiers or to delete them
4. Click on one of the buttons to search for words according to the amount of swap you want to use

![gui image](img/gui1.png?raw=true "GUI")
![gui image](img/gui2.png?raw=true "GUI")


### ConsoleUI instruction
1. Write the letters on the board in a single line following the order left -> right and then up -> down
2. Write the coordinates of the corresponding multipliers and leave blank if not applicable (eg 34 or 01)
3. To activate the swap mode (consider the use of a swap) you must put a 1, otherwise it will not be activated
4. The software will return an ordered list with the score, the word without swap, the word with swap (if it is not a swapped word both will be the same) and the coordinate of the initial letter

- The coordinates work with two non-separated numerical digits with values from 0 to 4

- Normal mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 
[(48, 'vomits', (3, 1)), (44, 'motels', (2, 3)), (42, 'motors', (2, 3)), (42, 'amigos', (1, 4)), (34, 'vomit', (3, 1)), (34, 'moves', (2, 3)), (34, 'maxi', (2, 3)), (34, 'motif', (2, 3)), (32, 'mix', (2, 3)), (30, 'tomb', (2, 1)), (30, 'motel', (2, 3)), (30, 'move', (2, 3)), (28, 'stoma', (1, 0)), (28, 'grim', (0, 2)), (28, 'omits', (3, 2)), (28, 'motor', (2, 3)), (28, 'motes', (2, 3)), (28, 'mites', (2, 3)), (28, 'ambo', (1, 4)), (28, 'amigo', (1, 4))]
```

- Swap mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 1
[(66, 'zoftig', (3, 2), 'z', (2, 3)), (58, 'vomitory', (3, 1), 'y', (0, 2)), (58, 'vomitous', (3, 1), 'u', (0, 0)), (58, 'comfits', (3, 2), 'c', (4, 2)), (58, 'jabots', (2, 4), 'j', (2, 3)), (58, 'faqirs', (2, 4), 'f', (2, 3)), (54, 'fimbria', (2, 2), 'r', (4, 3)), (54, 'comfit', (3, 2), 'c', (4, 2)), (54, 'setiform', (4, 0), 'r', (3, 3)), (54, 'maxing', (2, 3), 'n', (0, 1)), (54, 'maxima', (1, 4), 'm', (0, 4)), (54, 'fibroma', (4, 4), 'r', (4, 2)), (52, 'soffit', (1, 0), 'f', (2, 3)), (52, 'tombac', (2, 1), 'c', (3, 4)), (52, 'vomited', (3, 1), 'd', (4, 0)), (52, 'tomfool', (2, 1), 'o', (1, 0)), (52, 'motleys', (2, 3), 'y', 
(4, 1)), (52, 'covets', (3, 2), 'c', (2, 3)), (52, 'akimbo', (4, 3), 'k', (4, 4)), (50, 'gimbal', (0, 2), 'l', (1, 4))]
```


## Acknowledgements
- vscala for providing the base [Graphic UI](https://github.com/vscala/Spellcast-Word-Finder)
- SCOWL (And Friends) for providing the [generator](http://app.aspell.net/create) which was used for the initial wordlist
- [Jackson Ray Hamilton](https://github.com/jacksonrayhamilton/wordlist-english) for additional words