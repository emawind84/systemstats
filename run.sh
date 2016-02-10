#!/usr/bin/env bash

SCRIPT_BASE_PATH=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
SCRIPT_NAME="${0##*/}"

export PATH=$SCRIPT_BASE_PATH/env/bin:$PATH

set -e

echo "Base path: $SCRIPT_BASE_PATH"
echo "Script name: $SCRIPT_NAME"

cd $SCRIPT_BASE_PATH

#uwsgi --ini systemstats.ini --callable app > $SCRIPT_BASE_PATH/log/uwsgi.log 2>&1 &
uwsgi --ini systemstats.ini --callable app >/dev/null 2>&1 &
