#!/usr/bin/env python3


import csv
import math
from typing import List, Dict, Any


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end indices for the given page
    in a sequence of items with the specified page size.

    Args:
        page (int): The page number (starting from 1).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        Retrieve a page of data from a data source.

        Parameters:
            self (object): The instance of the class.
            page (int): The page number to retrieve. Default is 1.
            page_size (int): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of lists rep the data on the specified page.
                Each inner list contains items retrieved from the data source.
                The outer list represents the page itself.

        Raises:
            (Specify exp might be raised, or specify None if no exep is raised)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """
        Retrieve hyperlinks for a specified page of data.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page.

        Returns:
            Dict[str, Any]: A dict containing hyperlinks to pecified page.
                The keys represent different categories of hyperlinks.

        Raises:
            (Specify any exceptions that might be raised)
        """
        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page_size > page else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': math.ceil(len(self.__dataset) / page_size)
        }
