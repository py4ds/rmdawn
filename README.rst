Sunder
======

Extract YAML, code, and markdown files from an R markdown (Rmd) file.

|PyPI| |Travis| |Documentation Status| |Updates|

The ``sunder`` Python package consists of 2 shell commands and
functions: - ``sunder``, which extracts 1) a YAML file, 2) Python or R
scripts and 3) `Markdown <https://www.markdownguide.org/>`__ (md) files
from Rmd files. ``sunder`` can either output one R script per code chunk
or a single R script per Rmd file (similar to ``knitr::purl``).
Similarly, Markdown content can be combined into a single file or output
as separate files. Python package. - ``catrmd``, which
con\ **cat**\ enates input files to output an `R
Markdown <https://rmarkdown.rstudio.com/authoring_quick_tour.html>`__
(Rmd) file.

Write reports in R markdown format and use sunder to extract code from R
markdown code chunks.

.. |PyPI| image:: https://img.shields.io/pypi/v/sunder.svg
   :target: https://pypi.python.org/pypi/sunder
.. |Travis| image:: https://img.shields.io/travis/marskar/sunder.svg
   :target: https://travis-ci.org/marskar/sunder
.. |Documentation Status| image:: https://readthedocs.org/projects/sunder/badge/?version=latest
   :target: https://sunder.readthedocs.io/en/latest/?badge=latest
.. |Updates| image:: https://pyup.io/repos/github/marskar/sunder/shield.svg
   :target: https://pyup.io/repos/github/marskar/sunder/
