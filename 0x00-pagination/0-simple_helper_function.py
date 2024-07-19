#!/usr/bin/env python3
"""
Module containing index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function named index_range that takes
    two integer arguments page and page_size
    and returns a tuple of size two containing the start and end index.

    Args:
    page (int): The page number.
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
