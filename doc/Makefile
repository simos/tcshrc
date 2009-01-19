#############################################################################
##
## Makefile             2Sep2001, Simos Xenitellis (simos@hellug.gr)
##

## This is the makefile, part of the TCSHRC project
## at http://tcshrc.sourceforge.net

FILE=tcshrc

all:
	db2dvi $(FILE).sgml
	dvipdf $(FILE).dvi
	db2ps $(FILE).sgml
	db2html $(FILE).sgml
	
clean:
	rm -fr $(FILE).dvi
	rm -fr $(FILE).ps
	rm -fr $(FILE).pdf
	rm -fr $(FILE).junk
	rm -fr $(FILE).tex
	rm -fr $(FILE)
