ASM=atasm

all: fstbt.py

fstbt: fstbt.s
	$(ASM) -o$@ -L$@.var -g$@.lst $@.s

fstbt.py: fstbt
	python stringify.py fstbt

clean:
	rm fstbt fstbt.py fstbt.var fstbt.lst
