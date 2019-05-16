# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rtormd() function."""
from typing import Optional

import click

from rmdawn.rtormd import rtormd


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", "out")
def rtormd_cli(in_file: str, out: Optional[str] = None) -> None:
    """Convert an R markdown file into an R script.

    :param in_file: The name of the input R markdown file.
    :param out_file: The name of the output R script.
    """
    rtormd(in_file, output=out) if out else rtormd(in_file)
