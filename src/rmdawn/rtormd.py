#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional
from rpy2.robjects.packages import importr

def rtormd(filename: str, output: Optional[str] = None) -> None:
    """Convert an R script into an R markdown file.

    :param filename: The name of the input R script.
    :param output: The name of the output R markdown file.
    """

    k = importr("knitr")

    if output:
        print(k.spin(filename, output=output, knit=False, format="Rmd"))
    else:
        print(k.spin(filename, knit=False, format="Rmd"))
