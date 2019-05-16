# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rtormd() function."""
from typing import Optional

import click

from rmdawn.render import render


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file")
@click.option("-f", "--format", "out_format")
def render_cli(in_file: str,
               out_file: Optional[str] = None,
               out_format: Optional[str] = None) -> None:
    """Convert an R markdown file into an R script.

    :param in_file: The name of the input R markdown file.
    :param out_file: The name of the output R script.
    :param out_format: The format of the output file.
    """
    render(in_file, out_file=out_file, out_format=out_format)
