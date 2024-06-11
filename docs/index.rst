Sphinx Syft Theme
===================

.. banner::
   :color: rgba(40,40,60,0.8)
   :image: _static/images/pexels-jeff-stapleton-5792818.jpg
   :caption: Photo by Jeff Stapleton from Pexels
   :class: dark-banner

|jbook|

This is the Sphinx Syft Theme, a Sphinx theme for use with Jupyter Books.
The Sphinx Syft Theme inherits from the Sphinx Book Theme, which is used
by default in Jupyter Books.  It can be used on its own, outside of a Jupyter
Book, however, just like the Sphinx Book Theme, itself.

.. raw:: html

   <span class="d-flex justify-content-center py-4">
     <a href="about.html" role="button" class="btn btn-light btn-lg">
       Read more about the Sphinx Syft Theme
     </a>
   </span>

Beyond Sphinx Book Theme
------------------------

The Sphinx Syft Theme adds some new features to the existing features
provided by the Sphinx Book Theme and the PyData Sphinx Theme, upon which the
Sphinx Book Theme is built.

Banner Layouts
^^^^^^^^^^^^^^

One new feature is the use of alternate layouts for main pages, such as
the **banner** layout.  The banner layout converts all *titles* and *sections*
(i.e., ``#`` and ``##`` blocks) into *banners* that are full-width, have plenty
of padding (to separate them from the other content), and allow you to specify
background colors and images for the banner sections.

The page you are now reading is a *banner* layout page!

Standalone Layouts
^^^^^^^^^^^^^^^^^^

Another kind of alternate layout is the *standalone* layout, which displays
text exactly the same way as the *banner* layout, but it does not separate out
the sections into separate "banners."  The heading fonts and styling
are the same.

Glossary
--------

The Sphinx Syft Theme brings back the fixed top navigation bar provided by the PyData Sphinx Theme.
Where the Sphinx Book Theme places your ``html_logo`` at the top of the left sidebar, the PyData Sphinx
Theme places the logo on the left of the top navigation bar.  The PyData Sphinx Theme allows the user
to set the link attached to the logo with the ``logo_link`` option in your Sphinx ``html_theme_options``
dictionary.

.. rst-class:: text-center

   Click the button below to look at the Sphinx Syft Theme documentation.

.. raw:: html

   <span class="d-flex justify-content-center py-4">
     <a href="glossary.html" role="button" class="btn btn-light btn-lg">
       Read the documentation glossary
     </a>
   </span>

.. |jbook| image:: _static/images/badge.svg
   :target: https://jupyterbook.org
