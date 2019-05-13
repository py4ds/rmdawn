Rmdawn: a Python package for programmatic R markdown workflows
==============================================================

1. Create R markdown (Rmd) files from YAML, code, and markdown files.
2. Extract YAML, code, and markdown files from R markdown files.

|PyPI| |Updates|

The ``rmdawn`` Python package consists of 2 shell commands and
functions:

- ``rmdawn``, which concatenates input files to output an `R Markdown <https://rmarkdown.rstudio.com/authoring_quick_tour.html>`__ (Rmd) file.
- ``rmdusk``, which extracts 1) a YAML file, 2) Python or R scripts and 3) `Markdown <https://www.markdownguide.org/>`__ (md) files from Rmd files.


Installation
------------

.. code:: sh

    pip install rmdawn

or clone the `repo <https://github.com/marskar/rmdawn>`__, e.g. ``git clone https://github.com/marskar/rmdawn`` and install locally using setup.py (``python setup.py install``) or ``pip`` (``pip install .``).


Creating an R markdown file with the ``rmdawn`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    rmdawn header.yml intro.md scrape.py plot.R notes.txt > example.Rmd


Extract YAML, markdown, and code files from R markdown files with the ``rmdusk`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    rmdusk example.Rmd


Basic usage: Python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from pathlib import Path

    from rmdawn import rmdawn, rmdusk

    # Create an R markdown file from source files
    Path("example.Rmd").write_text(
        rmdawn(["header.yml", "intro.md", "scrape.py", "plot.R", "notes.txt"])
        )

    # Extract source files from an R markdown file
    rmdusk("example.Rmd")


.. |PyPI| image:: https://img.shields.io/pypi/v/rmdawn.svg
   :target: https://pypi.python.org/pypi/rmdawn
.. |Updates| image:: https://pyup.io/repos/github/marskar/rmdawn/shield.svg
   :target: https://pyup.io/repos/github/marskar/rmdawn/
