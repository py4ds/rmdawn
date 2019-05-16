#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rpy2.robjects.packages import importr

def rmdtor(filename: str, output=None) -> None:
    """Convert an R markdown file into an R script.

    :param filename: The name of the input R markdown file.
    :param output: The name of the output R script.
    """

    k = importr("knitr")

    print(k.purl(filename, output=output) if output else k.purl(filename))
