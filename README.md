# Discord Spellcast Helper
#### By fabaindaiz

Spellsolver is a software that helps to search for the best possible word in Spellcast discord activity. Spellsolver uses a trie to store the valid words, and then iteratively tries all the possible combinations of letters on the board, discarding the ones that don't make valid words and keeping the ones that do.

- Initialization of the trie structure to store valid words can take anywhere from 10 to 30 seconds and uses approximately 1 GB of ram memory, but allows all spellsolver queries to be executed in less than a second.
- I have planned to implement double swap, but with some algorithm that gives good results in a reasonable time (any ideas?)

The following messages will be printed while spellsolver is starting
```bash
Spellsolver v1.4 - fabaindaiz
WordValidate is being initialized, this will take several seconds
WordValidate successfully initialized (elapsed time: 25.05 seconds)
```

- #### Inside the docs folder, you will find some documents that detail the operation of spellsolver, as well as notes on how the algorithm is implemented and its limitations.


### Requirements
- python3
- tk (tkinter for graphicui.py)
- fastapi (for webapi.py)
- uvicorn (for webapi.py)

### TODO
- Improve results print format in console mode


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

### ConsoleUI using inputs
1. From this folder execute consoleui.py
2. Write the letters on the board in a single line following the order left -> right and then up -> down
3. Write the coordinates of the corresponding multipliers and leave blank if not applicable (eg 34 or 01)
4. To activate the swap mode (consider the use of a swap) you must put a 1, otherwise it will not be activated
5. The software will return an ordered list with the score, the word and the coordinate of the initial letter

```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x cord: 23
Insert DL cord: 23
Insert TL cord: 
Use swap?: 1
The following words have been found (elapsed time: 295.0 milliseconds)
['(66 zoftig (2, 3) | z (2, 3)), (58 vomitory (4, 2) | y (0, 2)), (58 vomitous (4, 2) | u (0, 1)), (58 comfits (3, 3) | c (3, 3)), (58 jabots (2, 3) | j (2, 3)), (58 faqirs (2, 3) | f (2, 3)), (54 fimbria (2, 2) | r (4, 4)), (54 setiform (4, 0) | r (3, 3)), (54 comfit (3, 3) | c (3, 3)), (54 maxing (2, 3) | n (0, 1))']
```

### ConsoleUI using arguments
1. From this folder execute consoleui.py with the following arguments
2. The software will return an ordered list with the score, the word and the coordinate of the initial letter

```bash
positional arguments:
  game        gameboard string

options:
  --swap      enable swap mode
  --x2 X2     word multiplier
  --dl DL     double letter
  --tl TL     triple letter

example:
    python consoleui.py rslesrotvegifovxqmbabaaif --swap --x2 23 --dl 23
```

### Generate wordlist
It is not necessary to carry out this step since wordlist is already generated

1. Move to path "src/wordlist/" and execute generate_wordlist.py
2. wordlist_english.txt file will be generated in the same folder


## Acknowledgements
- vscala for providing the base [Graphic UI](https://github.com/vscala/Spellcast-Word-Finder)
- SCOWL (And Friends) for providing the [generator](http://app.aspell.net/create) which was used for the initial wordlist
- [Jackson Ray Hamilton](https://github.com/jacksonrayhamilton/wordlist-english) for additional words
