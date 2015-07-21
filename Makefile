CC=g++

SYNLINK=ln -s

BIN_DIR=bin
TMP_DIR=tmp
SRC_DIR=src

all : dirs mission

mission : dirs
	$(SYNLINK) ../$(SRC_DIR)/mission/transdec.py $(BIN_DIR)/mission

dirs :
	mkdir -p $(BIN_DIR)
	mkdir -p $(TMP_DIR)

clean :
	rm -rf $(BIN_DIR)
	rm -rf $(TMP_DIR)
