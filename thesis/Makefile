# Makefile for LuaLaTeX thesis compilation
# Usage:
#   make          — full build (lualatex × 2 + biber)
#   make quick    — single lualatex pass (for proofreading)
#   make clean    — remove auxiliary files
#   make open     — open PDF in Preview (macOS)

MAIN = main
LATEXCMD = lualatex --shell-escape --synctex=1

.PHONY: all quick clean open

all:
	$(LATEXCMD) $(MAIN)
	biber $(MAIN)
	$(LATEXCMD) $(MAIN)
	$(LATEXCMD) $(MAIN)

quick:
	$(LATEXCMD) $(MAIN)

clean:
	latexmk -c $(MAIN) 2>/dev/null || true
	rm -f $(MAIN).{aux,bbl,bcf,blg,lof,log,lot,out,run.xml,synctex.gz,toc}
	rm -f chapters/*.aux

open:
	open $(MAIN).pdf
