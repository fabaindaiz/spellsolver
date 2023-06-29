# Spellsolver

#### Operation of the algorithm to find valid solutions for a spellsolver game using a trie.


## Spellsolver
In spellsolver.py, the spellsolving algorithm is implemented. This algorithm allows finding all possible solutions (with certain constraints) in a spellsolver game using the previously defined GameBoard and WordValidate together. The operation of the algorithm consists of the following steps:

- process_gameboard

Within this step, each tile on the game board is used as a starting point to begin forming valid words. For each tile on the board, the "possible_paths" function is called.

- process_path

Within this step, all neighboring nodes of the current tile are iteratively traversed. In each iteration, a query is made to WordValidate to check if the current path allows for the formation of a valid word in either swap or normal mode. If so, the execution of this step continues recursively on these nodes. Additionally, for each valid node reached during this step, the "process_path" function is called recursively to add possible paths that construct valid words to the list of found words.

- process_path_aux

Within this step, it is determined if any of the previously formed valid paths build a complete word. All the paths that form whole words are processed in "process_node" and are added to the list of found words. and then the method continues processing the path recursively.

- process_node

Within this step, from a node that ends a valid path, all the possible valid words that can be formed using the amount of swaps requested are obtained and added to the list of found words.


## Operation of the swap in the algorithm.
To find words that can be formed using swap, a kind of inverted index is used. For each word, a version is inserted with one of its letters changed by another symbol (eg "0") that indicates the swap, and in the leaf that corresponds to the word with swap the original word is stored in a list. This allows for the reconstruction of the word, knowing the information of the missing letter and its position, in order to analyze possible valid swaps later on.

This approach generates significantly better results than other algorithms attempting to solve this problem in a much shorter processing time per query (even when considering the amortization of the trie construction time within the metrics).
