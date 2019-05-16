#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from pathlib import Path

from rmdawn.extract import extract_after, extract_between


def rmdusk(in_file: str) -> None:
    """Extract YAML, code, and markdown files from an R markdown file.

    :param in_file: The name of the input R markdown file.
    """

    rmd_path = Path(in_file)
    rmd_text = rmd_path.read_text()

    Path(rmd_path.with_suffix(".yml")).write_text(
        extract_between(rmd_text, start="^---\n", end="\n---\n")
    )

    code_and_text = re.sub(
        r"```{(.*?)}",
        r"```#+ \1",
        extract_after(rmd_text, "\n---\n"),
        flags=re.DOTALL
    ).split("```")

    for n, string in enumerate(code_and_text):
        if string:
            if string.startswith("#+ python"):
                Path(rmd_path.stem + f"_{n}.py").write_text(string.strip())
            if string.startswith("#+ r"):
                Path(rmd_path.stem + f"_{n}.R").write_text(string.strip())
            else:
                Path(rmd_path.stem + f"_{n}.md").write_text(string.strip())
