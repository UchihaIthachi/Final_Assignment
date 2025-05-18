# tools/__init__.py
# Automatically gather all @tool-decorated tools for registration

from .math_tools import add, multiply
from .search_tools import wiki_search

ALL_TOOLS = [add, multiply, wiki_search]
