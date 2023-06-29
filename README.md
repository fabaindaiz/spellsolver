# Discord Spellcast Helper
#### By fabaindaiz

Spellsolver is a software that helps to search for the best possible word in Spellcast discord activity. Spellsolver uses a trie to store the valid words, and then iteratively tries all the possible combinations of letters on the board, discarding the ones that don't make valid words and keeping the ones that do.

- Initialization of the trie structure to store valid words in single swap mode can take anywhere from 20 to 30 seconds and uses approximately 1 GB of ram memory, but allows almost all spellsolver queries to be executed in less than a second.
- Double swap mode can be enabled in config.py, but it is not recommended as it significantly increases load times (100 seconds), ram usage (3.6 GB) and query time (up to 20 seconds)
- In case the wordlist.txt file does not exist, a new file will be automatically generated from the sources folder when starting spellsolver using any interface

A message like this will be printed on the screen while Spellsolver starts
```bash
Spellsolver v1.8 - fabaindaiz
WordValidate is being initialized, this will take several seconds
WordValidate successfully initialized (elapsed time: 25.05 seconds)
```

- #### Inside the docs folder, you will find some documents that detail the operation of spellsolver, as well as notes on how the algorithm is implemented.


### Requirements
- python3
- tk (tkinter for graphicui.py)
- fastapi (for webapi.py)
- uvicorn (for webapi.py)

### TODO
- Look for possible optimizations for the spellsolver algorithm
- Add some heuristics to reduce the load and query time of double swap mode


## instructions for use

- The letters on the board must be written in a single line following the order left -> right and then up -> down with no spaces
- To add a multiplier, the coordinates must be written as two numbers together (eg 34 or 01), otherwise the field must not be included or it must be left empty
- To activate the swap mode you must put the number of swaps that you want to use (eg 1), otherwise you must use a 0 and the option will not be activated

### WebAPI
1. From this folder execute webapi.py
2. Navigate to localhost:8080/docs to test the endpoints

![api image](assets/readme/api1.png?raw=true "API")

```bash
# Example solve request body
{
  "gameboard": "rslesrotvegifovxqmbabaaif",
  "mult": "23",
  "DL": "23",
  "swap": 1
}
```

### GraphicUI
1. From this folder execute graphicui.py
2. Write the letters on the board in the interface table
3. Use the right click to select letter modifiers or to delete them
4. Click on one of the buttons to search for words according to the amount of swap you want to use

![gui image](assets/readme/gui1.png?raw=true "GUI")
![gui image](assets/readme/gui2.png?raw=true "GUI")

### ConsoleUI using inputs
1. From this folder execute consoleui.py
2. Write the letters of the board and the rest of the data as indicated above
3. The software will return an ordered list with the score, the word and the coordinate of the initial letter

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
1. From this folder execute consoleui.py with the following arguments as indicated above
2. The software will return an ordered list with the score, the word and the coordinate of the initial letter

```bash
positional arguments:
  game         gameboard string

options:
  --swap SWAP  enable swap mode
  --x2 X2      word multiplier
  --dl DL      double letter
  --tl TL      triple letter

example:
  python consoleui.py rslesrotvegifovxqmbabaaif --swap 1 --x2 23 --dl 23
```


## Acknowledgements
- vscala for providing the base [Graphic UI](https://github.com/vscala/Spellcast-Word-Finder)
- SCOWL (And Friends) for providing the [generator](http://app.aspell.net/create) which was used for the initial wordlist
- [Jackson Ray Hamilton](https://github.com/jacksonrayhamilton/wordlist-english) for additional words
