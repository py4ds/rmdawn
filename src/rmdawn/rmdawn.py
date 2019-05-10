#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
from pathlib import Path


def rmdawn(filenames: List[str]) -> str:
    """Create an R markdown file from markdown and code files."""
    return "\n\n".join([
        "---\n" + Path(name).read_text() + "\n---"
        if name.endswith((".yaml", "yml"))
        else "```{python}\n" + Path(name).read_text() + "\n```"
        if name.endswith(".py")
        else "```{r}\n" + Path(name).read_text() + "\n```"
        if name.endswith(".R")
        else Path(name).read_text()
        for name in filenames
    ])

    if name.endswith((".yaml", "yml")):
    if name.endswith((".py", ".R", ".r")):
        text = Path(name).read_text()
        if text.startswith("#+"):
