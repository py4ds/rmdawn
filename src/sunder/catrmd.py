#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from pathlib import Path


def catrmd(filenames: List[str]) -> str:
    """Create an R markdown file from markdown and code files."""
    return ['```{r}\n'+Path(name).read_text()+'\n```'
            if name.endswith('.R')
            else '```{python}\n'+Path(name).read_text()+'\n```'
            if name.endswith('.py')
            else Path(name).read_text()
            for name in filenames]
