# Makefile for compiling the LaTeX paper
.PHONY: all clean

all: paper.pdf

paper.pdf: paper.tex
	pdflatex paper
	bibtex paper || true
	pdflatex paper
	pdflatex paper

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *.synctex.gz paper.pdf
