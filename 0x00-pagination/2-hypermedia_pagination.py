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
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
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

        with open("Popular_Baby_Names.csv", newline="") as csvfile:
            csvreader = csv.reader(csvfile)
            data = list(csvreader)
            row_list = data[start_index:end_index]
        return row_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a dict of containing the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an intege

        Args:
        page (int): The page number (1-based).
        page_size (int): The number of items per page.

        Returns:
        dict{}: A dict corresponding to the specified key-value pair.
        """
        data = self.get_page(page, page_size)
        pg_size = len(data)
        data_set = self.dataset()
        return {
            "page_size": pg_size,
            "page": page,
            "data": data,
            "next_page": (
                page + 1 if self.get_page(page + 1, page_size) else None
            ),
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": int(
                math.ceil((len(data_set) / page_size if page_size != 0 else 1))
            ),
        }
