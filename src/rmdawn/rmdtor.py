#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Optional

from rpy2.robjects.packages import importr


def rmdtor(in_file: str, out_file: Optional[str] = None):
    """Convert an R markdown file into an R script.

    :param in_file: The name of the input R markdown file.
    :param out_file: The name of the out_file R script.
    """

    k = importr("knitr")

    print(k.purl(in_file, output=out_file) if out_file else k.purl(in_file))
