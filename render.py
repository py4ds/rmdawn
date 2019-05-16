#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
from typing import Optional

from rpy2.robjects.packages import importr


def render(in_file: str,
           out_file: Optional[str] = None,
           out_format: Optional[str] = None) -> None:
    """Render an R script or R markdown file into another format.

    :param in_file: The name of the input R script or R markdown file.
    :param out_file: The name of the output file.
    :param out_format: The format of the output file.
    :note: If ``out_format`` is not provided, the output format will be
           inferred from the ``out_file`` argument. To create an html
           notebook, the ``out_format`` must be ``html_notebook``.
           For slides in html or pdf format, the ``out_format`` must be
           - ``slidy_presentation``,
           - ``ioslides_presentation``,
           - ``beamer_presentation``, or
           - ``revealjs::revealjs_presentation``.
    """

    if out_file and not out_format:
        ext = Path(out_file).suffix
        if ext in (".html", ".pdf", ".rtf", ".odt", ".md"):
            out_format = ext.replace(".", "") + "_document"
        elif ext in ("doc", "docx"):
            out_format = "word_document"
        elif ext in ("ppt", "pptx"):
            out_format = "powerpoint_presentation"

    rmd = importr("rmarkdown")

    if out_file:
        print(rmd.render(in_file,
                         output_file=out_file,
                         output_format=out_format))
    else:
        print(rmd.render(in_file))
