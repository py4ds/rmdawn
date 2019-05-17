Rmdawn: a Python package for programmatic R markdown workflows
==============================================================

|PyPI| |Updates|

Introduction
------------

The ``rmdawn`` Python package allows you to (de)construct, convert, and render `R Markdown <https://rmarkdown.rstudio.com/authoring_quick_tour.html>`__ (Rmd) files in

- your terminal (e.g. ``bash``, ``zsh``, ``fish``, etc.) or
- your favorite Python environment (e.g. `PyCharm <https://www.jetbrains.com/pycharm/>`__ or `Visual Studio Code <https://code.visualstudio.com/docs/python/python-tutorial>`__).

The ``rmdawn`` Python package consists of 6 shell commands and functions:

- ``rmdawn``, which concatenates input files to generate an Rmd file.
- ``rmdusk``, which extracts 1) a YAML file, 2) Python or R scripts and 3) `Markdown <https://www.markdownguide.org/>`__ (md) files from Rmd files.
- ``rmdtor``, which converts Rmd files into R scripts using `knitr::purl <https://www.rdocumentation.org/packages/knitr/versions/1.20/topics/knit>`__.
- ``rtormd``, which converts R scripts into Rmd files using `knitr::spin <https://yihui.name/knitr/demo/stitch/#spin-comment-out-texts>`__.
- ``render``, which creates rendered versions of R scripts or Rmd files into HTML, PDF, Word, and `other output file formats <https://rmarkdown.rstudio.com/lesson-9.html>`__.
- ``catren``, which combines the functionality of ``rmdawn`` and ``render`` to generate an Rmd file from source files and then create an output file.

All ``rmdawn`` functions and commands, except for ``rmdawn`` and ``rmdusk``, rely on the `rpy2 <https://rpy2.readthedocs.io/>`__ Python library.
The command line interface relies on the `click <https://click.palletsprojects.com/>`__ Python library.

For a related package that provides programmatic tools for working with `Jupyter
Notebooks <http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/What%20is%20the%20Jupyter%20Notebook.html>`__,
check out the `Nbless Python package <https://marskar.github.io/nbless/>`__.

Documentation and Code
----------------------

The documentation is hosted at https://marskar.github.io/rmdawn/.

The code is hosted at https://github.com/marskar/rmdawn.

Installation
------------

.. code:: sh

    pip install rmdawn

or clone the `repo <https://github.com/marskar/rmdawn>`__, e.g. ``git clone https://github.com/marskar/rmdawn`` and install locally using setup.py (``python setup.py install``) or ``pip`` (``pip install .``).


Creating an R markdown file with the ``rmdawn`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    rmdawn header.yml intro.md scrape.py plot.R notes.txt > example.Rmd

Instead of redirecting to a file (``>``), you can use the ``--out_file`` or ``-o`` flag:

.. code:: sh

    rmdawn header.yml intro.md scrape.py plot.R notes.txt -o example.Rmd

The easiest way to handle large numbers of files is to use the ``*`` wildcard in the shell.

.. code:: sh

    rmdawn source_file* -o example.Rmd

Extract YAML, markdown, and code files from R markdown files with the ``rmdusk`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    rmdusk example.Rmd

Convert between R markdown and R code files with the ``rmdtor`` and ``rtormd`` shell commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    rmdtor example.Rmd

    rtormd example.R

You can also specify an new filename with ``--out_file`` or ``-o`` flag.

.. code:: sh

    rmdtor example.Rmd -o new.R

    rtormd example.R -o new.Rmd

Render R markdown and R code files with the ``render`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default output format is HTML.

.. code:: sh

    render example.Rmd
    render example.R

You can specify output format with the ``--format`` or ``-f`` flag.

.. code:: sh

    render example.Rmd -f word_document
    render example.R -f word_document

If you only specify output filename with the ``--out_file`` or ``-o`` flag,
``render`` will try to infer the output format from the file extension.
This will not work for slides or R markdown notebooks.

.. code:: sh

    render example.Rmd -o example.pdf
    render example.R -o example.pdf

Create an R markdown file from source files with the ``catren`` shell command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pass ``--rmd_file`` (``-r``), ``--out_file`` (``-o``), and ``--format`` (``-f``) arguments to ``catren``.

.. code:: sh

    catren header.yml intro.md scrape.py plot.R notes.txt -r example.Rmd -f html_notebook

If you only specify an output filename with the ``--out_file`` or ``-o`` flag,
``catren`` will try to infer the R markdown file name and output format from the file extension.

.. code:: sh

    catren header.yml intro.md scrape.py plot.R notes.txt -o example.pdf

If you only specify an output format with the ``--format`` or ``-f`` flag or do not provide any optional arguments,
``catren`` will create a temporary file in a temporary location.

.. code:: sh

    catren header.yml intro.md scrape.py plot.R notes.txt -f word_document
    catren header.yml intro.md scrape.py plot.R notes.txt

Basic usage: Python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from pathlib import Path

    from rmdawn import rmdawn
    from rmdawn import rmdusk
    from rmdawn import rtormd
    from rmdawn import rmdtor
    from rmdawn import render
    from rmdawn import catren

    # Create an R markdown file from source files
    Path("example.Rmd").write_text(
        rmdawn(["header.yml", "intro.md", "scrape.py", "plot.R", "notes.txt"])
        )

    # Extract source files from an R markdown file
    rmdusk("example.Rmd")

    # Convert R markdown files into R scripts
    rmdtor("example.Rmd")

    # Convert R scripts into R markdown files
    rtormd("example.R")

    # Generate output files from R scripts or R markdown files
    render("example.Rmd") # The default format is HTML
    render("example.R") # The default format is HTML
    render("example.Rmd", out_format="pdf_document")
    render("example.R", out_format="word_document")

    # Create an R markdown file from source files output files and render it
    file_list = ["header.yml", "intro.md", "scrape.py", "plot.R", "notes.txt"]
    catren(file_list, rmd_file="example.Rmd") # The default format is HTML
    catren(file_list, rmd_file="example.Rmd", out_format="pdf_document")
    catren(file_list, out_file="example.html")

    # Another alternative is to import the package and use it as a namespace.
    import rmdawn

    rmdawn.rmdawn(["header.yml", "intro.md", "scrape.py", "plot.R", "notes.txt"])
    rmdawn.rmdusk("example.Rmd")
    rmdawn.rtormd("example.R")
    rmdawn.rmdtor("example.Rmd")
    rmdawn.render("example.Rmd") # The default format is HTML

.. |PyPI| image:: https://img.shields.io/pypi/v/rmdawn.svg
   :target: https://pypi.python.org/pypi/rmdawn
.. |Updates| image:: https://pyup.io/repos/github/marskar/rmdawn/shield.svg
   :target: https://pyup.io/repos/github/marskar/rmdawn/
