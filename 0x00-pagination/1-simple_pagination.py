#!/usr/bin/env python3
"""
Module containing index_range function
"""
import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a list of rows from the CSV
        file for the specified page and page size.

        Args:
        page (int): The page number (1-based).
        page_size (int): The number of items per page.

        Returns:
        List[List]: A list of rows corresponding to the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        row_list = []

        with open('Popular_Baby_Names.csv', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            data = list(csvreader)
            row_list = data[start_index:end_index]
        return row_list
