# Spellsolver

#### Operation of the algorithm to find valid solutions for a spellsolver game using a trie.


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
