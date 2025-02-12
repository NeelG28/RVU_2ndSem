#!/bin/bash
echo "Starting background processes"
sleep 300 &
task_pid=$!

#check if process is running
echo "Checking if the task is running..."
ps -p $task_pid

#killing
echo "Killing the background process..."
kill $task_pid

#confirming killing
echo "Checking status after termination..."

ps -p $task_pid && echo "Process still exists." || echo "Process terminated."

kill $task_pid


#if an attempt to kill after process is terminated ---- ./as4.sh: line 19: kill: (17546) - No such process

