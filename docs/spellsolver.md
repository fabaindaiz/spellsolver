# Spellsolver
#### Operation of the algorithm to find valid solutions for a spellsolver game using a trie.

## Trie
Is a type of k-ary search tree, a tree data structure used for locating specific keys from within a set. These keys are most often strings, with links between nodes defined not by the entire key, but by individual characters. In order to access a key (to recover its value, change it, or remove it), the trie is traversed depth-first, following the links between nodes, which represent each character in the key. [from wikipedia](https://en.wikipedia.org/wiki/Trie)

In trie.py, a generic TrieNode is defined, where multiple TrieNode children can be stored in a dictionary referenced by a letter as the key. Each node can also store a leaf based on TrieLeaf, where the required data can be stored depending on the case. The trie allows storing the words from the wordlist in an efficient structure to perform the necessary queries for the operation of spellsolver.

## Validate
In validate.py, a ValidateLeaf is implemented, which inherits from TrieLeaf. This class stores a dictionary that allows storing multiple lists of words referenced by a string key. Additionally, it implements the necessary methods to perform insertions and queries in this dictionary. A WordValidate is also implemented, which has the function of storing the complete TrieNode trie and has methods that allow initializing the structure from the wordlist file.

## Gameboard
In gameboard.py, Gametile is implemented, which represents a tile on the spellsolver game board, it can store a letter and the associated multipliers for the tile. GameTile also stores a reference to all its neighbors, which allows for easy iteration when attempting to build valid words. Additionally, a GameBoard is implemented, which stores all the GameTiles in a dictionary, where the key is a tuple representing the coordinates of each tile, this class also implements methods to initialize the spellsolver GameBoard from a string representation.

## Path
In path.py, Path is implemented, which allows for storing a list of GameTiles representing a valid word in formation, along with all the relevant information to continue this process iteratively. The class also implements useful methods to operate with GameTiles and the GameBoard, such as obtaining the score of the formed word considering the multipliers, suggesting valid neighboring nodes to continue forming words, and suggesting possible other paths that allow forming a word by swapping a tile that is not being used.

## Resultlist
In resultlist.py, a structure is implemented to store the valid words found during the execution of spellsolver. It is responsible for removing duplicate solutions and provides methods to construct representations of this list of words as a string and a dictionary, which can be presented later in the interfaces.

## Spellsolver
In spellsolver.py, the spellsolving algorithm is implemented. This algorithm allows finding all possible solutions (with certain constraints) in a spellsolver game using the previously defined GameBoard and WordValidate together. The operation of the algorithm consists of the following steps:

- word_list

Within this step, each tile on the game board is used as a starting point to begin forming valid words. For each tile on the board, the "possible_paths" function is called.

- posible_paths

Within this step, all neighboring nodes of the current tile are iteratively traversed. In each iteration, a query is made to WordValidate to check if the current path allows for the formation of a valid word. If so, the execution of this step continues recursively on these nodes. Additionally, for each valid node reached during this step, the "process_node" function is called to add possible paths that construct valid words to the list of found words.

- process_node

In this step, it is analyzed whether the current formed path, which has already been determined to be valid, constructs a complete word. To do this, the list of valid words for the node is obtained, and it is checked whether the current word is included in these words. If it is a word that does not require a swap, it is directly added to the list of formed words. If it is a word that requires a swap, all possible paths are generated using the available nodes, including the missing letter in the corresponding position.


## Limitations of the algorithm.
The algorithm employs a trick to find words with swaps. It involves iteratively removing one letter from each word and then storing these words with a missing letter within the trie. Finally, in the leaf of the node that completes this word with a missing letter, the complete word is added. This allows for the reconstruction of the word, knowing the information of the missing letter and its position, in order to analyze possible valid swaps later on.

That is why the algorithm cannot find words formed using a swap that connects two non-adjacent tiles, resulting in certain cases where a valid word with a swap, which could be better than the presented options, is not found. This decision was made considering that the algorithmic cost of considering these words would increase significantly without providing a significant benefit in the results it delivers. Additionally, this approach generates significantly better results than other algorithms attempting to solve this problem in a much shorter processing time per query (even when considering the amortization of the trie construction time within the metrics).