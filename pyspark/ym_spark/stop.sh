#!/usr/bin/env bash
ps -ef | grep "execute_data_process_column.py" | grep -v grep | awk '{ print $2 }' | xargs kill -9