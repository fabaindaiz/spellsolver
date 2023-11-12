from abc import ABC, abstractmethod
from collections.abc import Generator
from typing import Any


class TrieQuery(ABC):
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
    def get_key(self, node: Any, letter: str) -> tuple[Any, str]:
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
