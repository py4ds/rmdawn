#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from rpy2.robjects.packages import importr


def rtormd(in_file: str, out_file: Optional[str] = None):
    """Convert an R script into an R markdown file.

    :param in_file: The name of the input R script.
    :param out_file: The name of the out_file R markdown file.
    """

    k = importr("knitr")

    if out_file:
        print(k.spin(in_file, output=out_file, knit=False, format="Rmd"))
    else:
        print(k.spin(in_file, knit=False, format="Rmd"))
