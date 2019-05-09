Sunder
======

[![image](https://img.shields.io/pypi/v/sunder.svg)](https://pypi.python.org/pypi/sunder)

[![image](https://img.shields.io/travis/marskar/sunder.svg)](https://travis-ci.org/marskar/sunder)

[![Documentation Status](https://readthedocs.org/projects/sunder/badge/?version=latest)](https://sunder.readthedocs.io/en/latest/?badge=latest)

[![Updates](https://pyup.io/repos/github/marskar/sunder/shield.svg)](https://pyup.io/repos/github/marskar/sunder/)

The `sunder` Python package consists of 2 shell commands and functions:
- `sunder`, which extracts 1) a YAML file, 2) R scripts and 3) [Markdown](https://www.markdownguide.org/) (md) files from Rmd files. `sunder` can either output one R script per code chunk or a single R script per Rmd file (similar to `knitr::purl`). Similarly, Markdown content can be combined into a single file or output as separate files.
Python package.
- `catrmd`, which con**cat**enates input files to output an [R Markdown](https://rmarkdown.rstudio.com/authoring_quick_tour.html) (Rmd) file.

Write reports in R markdown format and use sunder to extract code from R markdown code chunks.

-   Free software: MIT license
-   Documentation: <https://sunder.readthedocs.io>.

Features
--------

-   TODO

Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
