# Makefile for building Jupyter Book

html:
	rm -rf docs/_build && jupyter-book build docs/ --builder html --all


book_links:
	jupyter-book build docs/ --builder linkcheck

book_html:
	jupyter-book build docs/ --builder html

book_pdfhtml:
	jupyter-book build docs/ --builder pdfhtml

book_pdflatex:
	jupyter-book build docs/ --builder pdflatex
