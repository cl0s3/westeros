#!/usr/bin/env bash

echorun() {
	
	echocommand"$@"
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

if [[ "$(basename -- "$0")" == "$(basename -- ${BASH_SOURCE[0]})" ]]; then
    echoerror "Don't run $0, source it!" >&2
    exit 1
fi

if [[ $# -eq 0 ]]; then
	VENV_NAME="westeros"
else
	VENV_NAME="$1"
fi
rootdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/..
cd ${rootdir}

source ${VENV_NAME}/bin/activate

if [ -n "$VIRTUAL_ENV" ]; then
	echocolor "Activated $(python -V) virtual environment ${VIRTUAL_ENV}."
else
	echoerror "Could not activate virtual environment '${VENV_NAME}'."
	exit 1
fi
