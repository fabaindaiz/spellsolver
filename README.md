# Discord Spellcast Helper

Spellsolver is a software that helps to search for the best possible word in Spellcast discord activity. Spellsolver
uses a trie to store the valid words, and then iteratively tries all the possible combinations of letters on the board,
discarding the ones that don't make valid words and keeping the ones that do.

- Initialization of the trie in single swap mode takes 5 seconds and uses 150 MB of ram memory.
- Once initialized, spellsolver runs almost all single swap queries in less than a second.

A message like this will be printed on the screen while Spellsolver starts

```bash
Spellsolver v1.15
WordValidate is being initialized, this will take several seconds
WordValidate successfully initialized (elapsed time: 4.8 seconds)
```

- #### Inside the docs folder, you will find some documents that detail the operation of spellsolver, as well as notes on how the algorithm is implemented.

### Requirements

- python3 (**3.9 or later**)
- marisa-trie (for store words)
- tk (tkinter for graphicui.py)
- fastapi (for webapi.py)
- uvicorn (for webapi.py)

### TODO

- Add some spellsolver tests to avoid accidentally introducing new bugs
- Document new changes to the spellsolver algorithm, improvements and bug fixes

## instructions for use

- The letters on the board must be written in a single line following the order left -> right and then up -> down with
  no spaces
- To add a multiplier, the coordinates must be written as two numbers together (eg 34 or 01), multiple coordinates must
  be separated by a space (in the case of consoleui.py, you must use dots instead of spaces)

### WebAPI

1. From this folder execute webapi.py
2. Navigate to localhost:8080/docs to test the endpoints

![api image](docs/readme/api1.png?raw=true "API")

```bash
# Example solve request body
{
  "gameboard": "rslesrotvegifovxqmbabaaif",
  "swap": 1,
  "gems": "00 01 02 03 04",
  "x2_mult": "23",
  "dl_mult": "23",
  "tl_mult": ""
}
```

### GraphicUI

1. From this folder execute graphicui.py
2. Write the letters on the board in the interface table
3. Use the right click to select letter modifiers or to delete them
4. Click on one of the buttons to search for words according to the amount of swap you want to use

![gui image](docs/readme/gui1.png?raw=true "GUI")
![gui image](docs/readme/gui2.png?raw=true "GUI")

### ConsoleUI using inputs

1. From this folder execute consoleui.py
2. Write the letters of the board and the rest of the data as indicated above
3. The software will return an ordered list with the score, the word and the coordinate of the initial letter

```bash
Insert a gameboard: rslesrotvegifovxqmbabaaif
Insert 2x coordinates: 23
Insert DL coordinates: 23
Insert TL coordinates: 
Use swap?: 1
The following words have been found (elapsed time: 295.0 milliseconds)
[(66 zoftig (2, 3) | z (2, 3)), (58 vomitory (4, 2) | y (0, 2)), (58 vomitous (4, 2) | u (0, 1)), (58 comfits (3, 3) | c (3, 3)), (58 jabots (2, 3) | j (2, 3)), (58 faqirs (2, 3) | f (2, 3)), (54 fimbria (2, 2) | r (4, 4)), (54 setiform (4, 0) | r (3, 3)), (54 comfit (3, 3) | c (3, 3)), (54 maxing (2, 3) | n (0, 1))]
```

### ConsoleUI using arguments

1. From this folder execute consoleui.py with the following arguments as indicated above
2. The software will return an ordered list with the score, the word and the coordinate of the initial letter

```bash
positional arguments:
  game         gameboard string

options:
  --swap SWAP  enable swap mode
  --gems GEMS  gem coordinates
  --ices ICES  ice coordinates
  --x2 X2      X2 coordinates
  --dl DL      dl coordinates
  --tl TL      tl coordinates

example:
  python consoleui.py rslesrotvegifovxqmbabaaif --swap 1 --x2 23 --dl 23 --gems 00.01.02.03.04
```

### Run tests

Some tests have been included to verify the correct working of spellsolver and all its modules
To run the tests you can use the following command

```bash
python -m unittest discover -s tests -t .
```

## Acknowledgements

- vscala for providing the base [Graphic UI](https://github.com/vscala/Spellcast-Word-Finder)
- SCOWL (And Friends) for providing the [generator](http://app.aspell.net/create) which was used for the initial
  wordlist
- [Jackson Ray Hamilton](https://github.com/jacksonrayhamilton/wordlist-english) for additional words
