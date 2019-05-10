# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the catrmd() function."""
import click


@click.command()
@click.argument("in_files", nargs=-1, required=True,
                type=click.Path(exists=True))
@click.option("-o", "--out_file", "out")
def catrmd_cli(args=None):
    """Create an R markdown file from markdown and code files."""
