# Discord Spellcast Helper
#### By fabaindaiz

Spellsolver is a software that helps to search for the best possible word in Spellcast discord activity. Spellsolver uses a trie to store the valid words, and then iteratively tries all the possible combinations of letters on the board, discarding the ones that don't make valid words and keeping the ones that do.

- Initialization of the trie structure to store valid words can take anywhere from 10 to 30 seconds and uses approximately 1 GB of ram memory, but allows all spellsolver queries to be executed in less than a second.
- I have planned to implement double swap, but with some algorithm that gives good results in a reasonable time (any ideas?)

The following messages will be printed while spellsolver is starting
```bash
Spellsolver v1.3 - fabaindaiz
WordValidate is being initialized, this will take several seconds
WordValidate successfully initialized (elapsed time: 25.05 seconds)
```

### TODO
- Add general documentation about how spellsolver works
- Improve results print format in console mode

### Requirements
- python3
- tk (tkinter for graphicui.py)
- fastapi (for webapi.py)
- uvicorn (for webapi.py)


## instructions for use

### WebAPI
1. From this folder execute webapi.py
2. Navigate to localhost:8080/docs to test the endpoints

![api image](img/api1.png?raw=true "API")


### GraphicUI
1. From this folder execute graphicui.py
2. Write the letters on the board in the interface table
3. Use the right click to select letter modifiers or to delete them
4. Click on one of the buttons to search for words according to the amount of swap you want to use

![gui image](img/gui1.png?raw=true "GUI")
![gui image](img/gui2.png?raw=true "GUI")


### ConsoleUI
1. From this folder execute consoleui.py
2. Write the letters on the board in a single line following the order left -> right and then up -> down
3. Write the coordinates of the corresponding multipliers and leave blank if not applicable (eg 34 or 01)
4. To activate the swap mode (consider the use of a swap) you must put a 1, otherwise it will not be activated
5. The software will return an ordered list with the score, the word without swap, the word with swap (if it is not a swapped word both will be the same) and the coordinate of the initial letter

- The coordinates work with two non-separated numerical digits with values from 0 to 4

- Normal mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 
The following words have been found (elapsed time: 95.0 milliseconds)
['(48 vomits (4, 2))', '(44 motels (2, 3))', '(42 motors (2, 3))', '(42 amigos (2, 4))', '(34 vomit (4, 2))', '(34 moves (2, 3))', '(34 maxi (2, 3))', '(34 motif (2, 3))', '(32 mix (2, 3))', '(30 tomb (2, 1))']
```

- Swap mode
```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 1
The following words have been found (elapsed time: 437.0 milliseconds)
['(66 zoftig (2, 3) | z (2, 3))', '(58 vomitory (4, 2) | y (0, 0))', '(58 vomitous (4, 2) | u (2, 0))', '(58 comfits (3, 3) | c (3, 3))', '(58 jabots (2, 3) | j (2, 3))', '(58 faqirs (2, 3) | f (2, 3))', '(54 fimbria (2, 2) | r (4, 3))', '(54 setiform (4, 0) | r (3, 3))', '(54 comfit (3, 3) | c (3, 3))', '(54 maxing (2, 3) | n (1, 3))']
```

### Generate wordlist
It is not necessary to carry out this step since wordlist is already generated

1. Move to path "src/wordlist/" and execute generate_wordlist.py


## Acknowledgements
- vscala for providing the base [Graphic UI](https://github.com/vscala/Spellcast-Word-Finder)
- SCOWL (And Friends) for providing the [generator](http://app.aspell.net/create) which was used for the initial wordlist
- [Jackson Ray Hamilton](https://github.com/jacksonrayhamilton/wordlist-english) for additional words
