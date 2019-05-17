# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rtormd() function."""
from typing import List, Optional

import click

from rmdawn.catren import catren


@click.command()
@click.argument("in_files", nargs=-1, required=True,
                type=click.Path(exists=True))
@click.option("-r", "--rmd_file")
@click.option("-o", "--out_file")
@click.option("-f", "--format", "out_format")
def catren_cli(in_files: List[str],
               rmd_file: Optional[str] = None,
               out_file: Optional[str] = None,
               out_format: Optional[str] = None) -> None:
    """Convert an R markdown file into an R script.

    :param in_files: A list of YAML, markdown, and code file names.
    :param rmd_file: The name of the intermediate rmd file.
    :param out_file: The name of the final output file.
    :param out_format: The format of the final output file.
    """
    catren(in_files,
           rmd_file=rmd_file,
           out_file=out_file,
           out_format=out_format)
