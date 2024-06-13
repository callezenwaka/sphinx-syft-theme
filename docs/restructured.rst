Restructured Text (.rst)
========================

The Syft Theme is a `Sphinx Theme <https://www.sphinx-doc.org/en/master/usage/theming.html>`_
that inherits directly from the `Sphinx Book Theme <https://sphinx-book-theme.readthedocs.io/en/latest/>`_
used by the amazing `Jupyter Book project <https://jupyterbook.org/intro.html>`_.  As a result, the
Sphinx Syft Theme, through the Sphinx Book Theme, inherits from the awesome
`PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`_,
which provides a great deal of functionality.

On top of all of these amazing themes, the Sphinx Syft theme add a few simple new features.

|:man_technologist_dark_skin_tone:| Introduction
------------------------------------------------

This is a Jupyter Book example.

This text includes a man technologist |:man_technologist_dark_skin_tone:| and a woman technologist too! |:woman_technologist:|


Top Navigation Bar
^^^^^^^^^^^^^^^^^^

The Sphinx Syft Theme brings back the fixed top navigation bar provided by the PyData Sphinx Theme.
Where the Sphinx Book Theme places your ``html_logo`` at the top of the left sidebar, the PyData Sphinx
Theme places the logo on the left of the top navigation bar.  The PyData Sphinx Theme allows the user
to set the link attached to the logo with the ``logo_link`` option in your Sphinx ``html_theme_options``
dictionary.

Standalone Pages
----------------

Standalone pages use the ``page-standalone.html`` template in the same way that the
*banner* pages above use the ``page-banner.html`` template.  Standalone pages have
the same heading and text styling used by banner pages, but they do not have extra
padding nor the ability to declare banner backgrounds to the sections.  The
:doc:`/standalone` page is an example of this layout.

Custom Templates
----------------

The Sphinx Syft Theme uses certain custom templates to define how the content in certain
sections of the page will display.  For the links in the top navigation bar, the ``navbar-menu.html``
template is used.  For how to define *banner* and *standalone* page layouts, the ``page-banner.html``
and the ``page-standalone.html`` templates are used.  For footer content, the ``footer-logos.html``,
``footer-info.html``, ``footer-menu.html``, and the ``footer-extra.html`` templates are used.

Anyone can override these templates by putting their own versions of these templates (i.e.,
using the same template filenames) in a ``_templates`` directory within their Sphinx or Jupyter
Book source (at the same level as their ``conf.py`` or ``_config.yml`` files).
