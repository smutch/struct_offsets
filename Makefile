CC = cc
OUTPUT_OPTION = -o $@
CFLAGS = -std=gnu99 -O3 -march=native ${incdirs}
CPPFLAGS = 
LDFLAGS = 
LDLIBS = -lm
 
.PHONY: clean

default: offsets
	@echo "\n"
	@./offsets

offsets: offsets.c

offsets.c: templates/offsets.c generate.py
	./generate.py ${header} ${struct}
 
clean:
	rm -f offsets.[oc] offsets
