#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:10]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset starting
        from the specified index, resilient to deletions.

        Args:
            index (int): The starting index of the page. Defaults to None.
            page_size (int): The number of items per page. Defaults to 10.

        Returns:
            Dict: A dictionary containing:
                - index (int): The starting index of the current page.
                - next_index (int): The next index to query.
                - page_size (int): The current page size.
                - data (List): The actual page of the dataset.

        Raises:
            AssertionError:
            If the index is not within the valid range of the dataset.
        """
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        data = self.indexed_dataset()
        current_index = index
        fin = []
        collected = 0

        while collected < page_size and current_index < len(data):
            if current_index in data:
                fin.append(data[current_index])
                collected += 1
            current_index += 1

        next_index = current_index if current_index < len(data) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": fin
        }
