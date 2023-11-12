from abc import ABC, abstractmethod

from src.modules.validate.wordlist import WordList
from .trie_query import TrieQuery


class Trie(ABC):
    @abstractmethod
    def insert(self, loader: WordList, swap: int) -> None:
        """
        Insert a wordlist into the trie structure.

        This method is responsible for inserting the words from the provided
        WordList instance into the Trie. Optionally, it allows specifying the
        number of swaps to apply during the insertion process.

        Parameters:
            loader (WordList): The WordList instance containing the words to insert.
            swap (int, optional): The number of swaps to apply during insertion. Defaults to 2.

        Returns:
            None

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def query(self) -> TrieQuery:
        """
        Perform a query on the Trie structure.

        This method is used to perform a query on the Trie structure, returning a
        TrieQuery instance containing the results of the query.

        Returns:
            TrieQuery: A TrieQuery instance containing the results of the query.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass
