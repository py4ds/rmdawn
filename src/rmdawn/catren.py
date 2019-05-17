#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile
from pathlib import Path
from typing import List, Optional

from rmdawn.rmdawn import rmdawn
from rmdawn.render import render


def catren(in_files: List[str],
           rmd_file: Optional[str] = None,
           out_file: Optional[str] = None,
           out_format: Optional[str] = None) -> None:
    """Create an R markdown file from source files and then render it.

    :param in_files: A list of YAML, markdown, and code file names.
    :param rmd_file: The name of the intermediate rmd file.
    :param out_file: The name of the final output file.
    :param out_format: The format of the final output file.
    :note: If ``out_format`` is not provided, the output format will be
           inferred from the ``out_file`` argument. To create an html
           notebook, the ``out_format`` must be ``html_notebook``.
           For slides in html or pdf format, the ``out_format`` must be
           - ``slidy_presentation``,
           - ``ioslides_presentation``,
           - ``beamer_presentation``, or
           - ``revealjs::revealjs_presentation``.
    """
    if rmd_file:
        Path(rmd_file).write_text(rmdawn(in_files))
        render(rmd_file, out_file=out_file, out_format=out_format)
    elif out_file:
        rmd_file = Path(out_file).stem + ".Rmd"
        Path(rmd_file).write_text(rmdawn(in_files))
        render(rmd_file, out_file=out_file, out_format=out_format)
    else:
        with tempfile.NamedTemporaryFile(mode="w") as ntf:
            ntf.write(rmdawn(in_files))
            render(ntf.name, out_file=out_file, out_format=out_format)
