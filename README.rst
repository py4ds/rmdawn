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
