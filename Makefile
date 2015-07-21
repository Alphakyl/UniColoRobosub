CC=g++

SYNLINK=ln -s

BIN_DIR=bin
TMP_DIR=tmp
SRC_DIR=src

all : dirs

dirs :
	mkdir -p $(BIN_DIR)
	mkdir -p $(TMP_DIR)

clean :
	rm -rf $(BIN_DIR)
	rm -rf $(TMP_DIR)
