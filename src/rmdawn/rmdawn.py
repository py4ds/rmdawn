#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from pathlib import Path


def rmdawn(filenames: List[str]) -> str:
    """Create an R markdown file from markdown and code files."""
    return "\n\n".join([
        '```{r}\n'+Path(name).read_text()+'\n```'
        if name.endswith('.R')
        else '---\n'+Path(name).read_text()+'\n---'
        if name.endswith(('.yaml', 'yml'))
        else '```{python}\n'+Path(name).read_text()+'\n```'
        if name.endswith('.py')
        else Path(name).read_text()
        for name in filenames
    ])
