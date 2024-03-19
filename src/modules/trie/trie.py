from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import Any

from src.modules.validate.wordlist import WordList


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
    def get_root(self) -> Any:
        """
        Get the root node of the Trie.

        Returns:
            Any: The root node of the Trie.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def get_key(self, node: Any, letter: str) -> tuple[Any, Any | None]:
        """
        Get the child node and corresponding-edge label for a given letter from a Trie node.

        Parameters:
            node (Any): The Trie node for which to retrieve the child node and edge label.
            letter (str): The letter representing the edge to the child node.

        Returns:
            Tuple[Any, str]: A tuple containing the child node and the edge label.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def get_leaf(self, node: Any) -> Generator[str, None, None]:
        """
        Generate the words in the sub-trie rooted at the given node.

        Parameters:
            node (Any): The Trie node at which to start generating words.

        Yields:
            str: A word in the sub-trie.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        pass
