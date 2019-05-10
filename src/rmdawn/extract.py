#!/usr/bin/env python
# -*- coding: utf-8 -*-


def extract_after(string, start):
    """Extract all of the characters after start."""
    return string[string.find(start) + len(start):]


def extract_before(string, end):
    """Extract all of the characters after start."""
    return string[:string.find(end)]


def extract_between(string, start, end):
    """Extract all of the characters between start and end."""
    return string[string.find(start) + len(start):string.find(end)]
