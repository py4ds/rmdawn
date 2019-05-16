# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rmdtor() function."""
from typing import Optional
import click

from rmdawn.rmdtor import rmdtor


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", "out")
def rmdtor_cli(in_file: str, out: Optional[str] = None) -> None:
    """Convert an R markdown file into an R script.

    :param in_file: The name of the input R markdown file.
    :param out_file: The name of the output R script.
    """
    rmdtor(in_file, output=out) if out else rmdtor(in_file)
