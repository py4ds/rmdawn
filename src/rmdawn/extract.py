#!/usr/bin/env python
# -*- coding: utf-8 -*-


def extract_after(source: str, start: str) -> str:
    """Extract all of the characters after ``start``.

    :param source: The input string from which to extract a substring.
    :param start: The substring that marks the extraction starting place.
    :param return: A substring that is extracted from ``source``.
    :note: The ``start`` string is not include in the result.
    """
    return source[source.find(start) + len(start):]


def extract_before(source: str, end: str) -> str:
    """Extract all of the characters before start.

    :param source: The input string from which to extract a substring.
    :param end: The substring that marks the place where extraction will end.
    :param return: A substring that is extracted from ``source``.
    :note: The ``end`` string is not include in the result.
    """
    return source[:source.find(end)]


def extract_between(source: str, start: str, end: str) -> str:
    """Extract all of the characters between start and end.

    :param source: The input string from which to extract a substring.
    :param start: The substring that marks the extraction starting place.
    :param end: The substring that marks the place where extraction will end.
    :param return: A substring that is extracted from ``source``.
    :note: The ``start`` and ``end`` strings are not include in the result.
    """
    return source[source.find(start) + len(start):source.find(end)]
