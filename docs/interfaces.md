# Interfaces

#### Basic explanation of how the implemented interfaces work.


## BaseUI
In baseui.py, the abstract class BaseUI is implemented. It has all the necessary methods to interact with the spellsolver algorithm and deliver the results in a format that can be easily used by the interface. ThreadSolver is also implemented, which is a thread-safe solver that allows executing multiple queries to the spellsolver queries in parallel, reusing the same initialized WordValidate.

## BaseAPI & ApiRouter
BaseApi implements an interface with a base FastAPI API and router that includes all the necessary basic methods for the WebAPI. ApiRouter implements a router with the methods and endpoints required to perform Spellsolver queries and return a response in JSON format.

## WebAPI
WebAPI utilizes FastAPI to provide a RESTful web interface that allows performing spellsolver queries from a web environment.

## TkinterWidget & TkinterBoard
TkinterWidget implements classes for all the necessary tkinter objects and methods to construct the GraphicUI. TkinterBoard implements all the methods that enable the interaction between the tkinter interface and spellsolver.

## GraphicUI
GraphicUI utilizes Tkinter to provide a simple visual interface that allows performing spellsolver queries from a desktop environment.

## ConsoleUI
ConsoleUI provides a simple console interface that allows performing spellsolver queries from a console environment. It enables interactions using command-line arguments or user inputs.
