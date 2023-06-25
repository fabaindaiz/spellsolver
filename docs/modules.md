# Modules

#### The necessary parts for the functioning of the spellsolver algorithm.


## Trie
Is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key. [from wikipedia](https://en.wikipedia.org/wiki/Trie)

In trie.py, a generic TrieNode is defined, where multiple TrieNode children can be stored in a dictionary referenced by a letter as the key. Each node can also store a leaf based on TrieLeaf, where the required data can be stored depending on the case. The trie allows storing the words from the wordlist in an efficient structure to perform the necessary queries for the operation of spellsolver.

## Validate
In validate.py, a ValidateLeaf is implemented, which inherits from TrieLeaf. This class stores a dictionary that allows storing multiple lists of words referenced by a string key. Additionally, it implements the necessary methods to perform insertions and queries in this dictionary. A WordValidate is also implemented, which has the function of storing the complete TrieNode trie and has methods that allow initializing the structure from the wordlist file.

## Gameboard
In gameboard.py, Gametile is implemented, which represents a tile on the spellsolver game board, it can store a letter and the associated multipliers for the tile. GameTile also stores a reference to all its neighbors, which allows for easy iteration when attempting to build valid words. Additionally, a GameBoard is implemented, which stores all the GameTiles in a dictionary, where the key is a tuple representing the coordinates of each tile, this class also implements methods to initialize the spellsolver GameBoard from a string representation.

## Path
In path.py, Path is implemented, which allows for storing a list of GameTiles representing a valid word in formation, along with all the relevant information to continue this process iteratively. The class also implements useful methods to operate with GameTiles and the GameBoard, such as obtaining the score of the formed word considering the multipliers, suggesting valid neighboring nodes to continue forming words, and and get the indices of the swapped letters from a formed word.

## Resultlist
In resultlist.py, a structure is implemented to store the valid words found during the execution of spellsolver. It is responsible for removing duplicate solutions and provides methods to construct representations of this list of words as a string and a dictionary, which can be presented later in the interfaces.