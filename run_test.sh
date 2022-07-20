# INPUTS: path to python binary
PYTHON_BIN=${1:-python}
$PYTHON_BIN -m unittest discover -v tests