# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the rmdusk() function."""
import click

from rmdawn import rmdusk


@click.command()
@click.argument("in_file")
def rmdusk_cli(in_file: str):
    """Extract YAML, markdown, and code files from a R markdown file."""
    rmdusk(in_file)
