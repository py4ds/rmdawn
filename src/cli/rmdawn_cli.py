# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rmdawn() function."""
import sys
from typing import List
from pathlib import Path

import click

from rmdawn.rmdawn import rmdawn


@click.command()
@click.argument("in_files", nargs=-1, required=True,
                type=click.Path(exists=True))
@click.option("-o", "--out_file", "out")
def rmdawn_cli(in_files: List[str], out: str) -> None:
    """Create an R markdown file from markdown and code files.

    :param in_files: The list of the input files.
    :param out_file: The name of the output R markdown file.
    """
    if out:
        Path(out).write_text(rmdawn(in_files))
    else:
        sys.stdout.write(rmdawn(in_files))
