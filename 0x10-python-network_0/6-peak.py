#!/usr/bin/python3
"""Module for finding a peak in a list of integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers."""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
