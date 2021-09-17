Documentation "how to" in depth
===============================

Our documentation is build using `Sphinx <http://www.sphinx-doc.org/en/master/>`_, which uses
``reStructuredText`` (and with extensions ``Markdown``) to compile documentation as ``html``, ``LaTeX``,
``PDF`` and more.
It takes care of linking all pages together, building a search index and also extraction the documentation
written in the docstrings of the code.

How to use Sphinx in general
----------------------------

First you have enter your virtual env (if you don't know how, have a look here:
:ref:`virtual-envs-in-depth`)

When you are in your virtual env (here called ``glotaran``) navigate to glotarans ``docs`` folder::

    (glotaran)$cd docs


.. note::  Consider for the following steps that, if you are on a Posix system
           (Linux, MacOS, BSD or Git Bash/migwin on Windows) use ``make``,
           on normal Windows cmd/PS use ``make.bat`` instead.
           If your Git Bash is missing the `make` functionality you can follow this
           `guide <https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058>`_.

Once you are in the ``docs`` folder, generating/compiling the documentation is as easy as running::

    (glotaran)$make html

The documentation than can be found is the folder ``docs/_build/html``, where you can open it by
double clicking ``index.html``

.. warning:: The ``reStructuredText`` Syntax isn't as forgiving as ``html`` (where browsers correct most
             of the falsey). It's more like ``LaTeX``, which is why it is recommended to compile often,
             for errors not to stack up.


It might happen, that you change the documentation and can't see the changes after a refresh in the browser.
Since Sphinx to reduce the compile time, it only recompiles the changed files, which can lead to problems
if you add new files, because the indexing wasn't updated. If this happens, you can force Sphinx to rebuild
the whole documentation by first running::

    (glotaran)$make clean


Workflow
^^^^^^^^

1. Change the docs
2. Build the docs::

    (glotaran)$make html

3. Look at the commandline interface and make sure no errors happened.
4. Refresh the you browser to see the changes.

5. If there are no changes, even so there was no error, force Sphinx to rebuild all::

    (glotaran)$make clean html

6. Start with step 1 again.

Useful resources:
    * `Sphinx reST Docs <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
    * `Sphinx/reST Memo <https://rest-sphinx-memo.readthedocs.io/en/latest/index.html>`_
    * `reST Cheatsheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_
    * `Restructured Text (reST) and Sphinx CheatSheet <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
    * `Read the Docs Sphinx Theme <https://sphinx-rtd-theme.readthedocs.io/en/latest/>`_
    * `Sphinx Configuration <http://www.sphinx-doc.org/en/master/usage/configuration.html>`_

Often used commands (for Windows replace ```make`` with ```make.bat``):
    * ``(glotaran)$make html``
    * ``(glotaran)$make clean``
    * ``(glotaran)$make clean html``
    * ``(glotaran)$make help``


Generate API Documentation
--------------------------

The API Documentation will be generated automatically form the docstrings.
Those Docstrings should be formatted in the
`NumPyDoc <https://numpydoc.readthedocs.io/en/latest/example.html>`_ style.
Please make use of all available features as you see fit.

The features are:
    * Parameters
    * Returns
    * Raises
    * See Also
    * Notes
    * References
    * Examples

If you add ``packages``, ``modules``, ``classes``, ``methods``, ``attributes``,
``functions`` or ``exceptions``, please read the introduction of :ref:`api-docs-new-entry`: api-docs-new-entry_.

Often used commands (for Windows replace ```make`` with ```make.bat``):

    * ``(glotaran)$make html``
    * ``(glotaran)$make clean_all``
    * ``(glotaran)$make api_docs``
    * ``(glotaran)$make clean_all api_docs html``

---------------

.. _api-docs-new-entry:

Api Documentation Creation Helper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The helper Module to generate the API documentation is located at ``docs/generate_api_documentation.py``.

The functionality is available by calling ``make api_docs`` on a Posix system
or ``make.bat api_docs`` on Windows.

If you add ``packages``, ``modules``, ``classes``, ``methods``, ``attributes``,
``functions`` or ``exceptions``, you might need to run ``make clean_all`` on a Posix system
or ``make.bat clean_all`` on Windows to see changes in the documentation.

The generation of the API is done by traversing the main package
``traverse_module`` and listing all child modules for autosummary to process
(see ``write_api_documentation``, ``api_documentation.rst`` and
``_templates/api_documentation_template.rst``).

If the child module is also a package all its contained modules will be listed
(see ``write_known_packages``, ``known_packages.rst``, ``_templates/known_packages_template.rst`` and ``_templates/autosummary/module.rst``).

To understand how it works in detail the following links might be of help:

* `Sphinx Templating Docs <http://www.sphinx-doc.org/en/master/templating.html>`_

* `Jinja Templating <http://jinja.pocoo.org/docs/2.10/templates/>`_

* `Sphinx autosummary Docs <http://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html?highlight=autosummary%20>`_

* `Sphinx autodoc Docs  <http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#module-sphinx.ext.autodoc>`_
