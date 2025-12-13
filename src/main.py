"""
This script demonstrates the starting point for using Cursor agents.
It provides a simple structure for running agent-based workflows.
"""

from .utils import get_greeting

def main():
    """
    Entry point for the script.

    Prints a message indicating that Cursor agents are ready.
    """
    print(get_greeting())

if __name__ == "__main__":
    main()