#!/usr/bin/env python3
""" module contains simple helper function """


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
