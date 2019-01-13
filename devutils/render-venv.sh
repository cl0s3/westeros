#!/usr/bin/env bash

echorun() {
	
	echocommand "$@"
	eval "$@"
}

echocommand() {
	echo -e "\n\e[1;36m$@\e[0m"
}

echocolor() {
	echo -e "\n\e[1;35m$@\e[0m"
}

echoerror() {
	echo -e "\n\e[1;31m$@\e[0m"
}

rootdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/..
cd ${rootdir}

if [[ $# -eq 0 ]]; then
	VENV_NAME="westeros-venv"
else
	VENV_NAME="$1"
fi

if [[ ${VENV_NAME} = "dev" ]]; then
	setup_cmd="pip install -e ."
else
	setup_cmd="python setup.py clean --all install"
fi

if [[ $? != 0 ]]; then
	exit $?
fi

echorun "python3 -m venv ${VENV_NAME}"
cd ${rootdir}
echorun "source ${VENV_NAME}/bin/activate"

if [ -n "$VIRTUAL_ENV" ]; then
	echocolor "Activated $(python -V) virtual environment ${VIRTUAL_ENV}."
else
	echoerror "Could not activate virtual environment '${VENV_NAME}'."
	exit $?
fi

echorun "pip install --upgrade pip"
echorun "pip install -r ${rootdir}/devutils/requirements.txt"
echocolor "Done."
