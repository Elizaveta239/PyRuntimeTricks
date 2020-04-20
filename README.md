# PyRuntimeTricks

A repository with the source code of examples used in Elizaveta Shashkova's PyCon US 2020 talk "The Hidden Power of the Python Runtime"

All the examples use Python 3.8

`assertvars` - a tool which shows variables values for all variables used inside assertion statement. Can be useful for 
logging and debugging failed assertions 

`asyncfaulthandler` - a tool which prints asynchronous tasks traceback with a given interval. Can be useful for detecting 
and fixing asynchronous deadlocks