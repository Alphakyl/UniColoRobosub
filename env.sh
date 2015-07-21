# Source this file to load the correct paths into your environment: "source ./env.sh" or ". ./env.sh" in zsh/bash.

BASE_DIR=`pwd`/`dirname $0`
SRC_DIR=$BASE_DIR/src
BIN_DIR=$BASE_DIR/bin
LOGFILE=$BASE_DIR/logs/main.log

export PYTHONPATH=$SRC_DIR:$PYTHONPATH
export PATH=$BIN_DIR:$PATH
export LOGFILE=$LOGFILE
