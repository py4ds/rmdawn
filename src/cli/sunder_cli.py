# -*- coding: utf-8 -*-
"""Command line interface (CLI) for the sunder() function."""
import click


@click.command()
@click.argument("in_file")
@click.option("-o", "--out_file", "out_file")
def sunder_cli(args=None):
    """Extract YAML, markdown, and code files from a R markdown file."""
