#!/bin/bash
echo "Starting two background processes"
sleep 300 &
task_pid1=$!
sleep 300 &
task_pid2=$!
echo "first : $task_pid1 , second : $task_pid2"

echo "Checking status of first process "
ps -p $task_pid1

echo "Checking status of second process "
ps -p $task_pid2

#pausing both processes
kill -STOP $task_pid1
echo "Checking task status after pausing first process..."
ps -o pid,stat,cmd -p$task_pid1
kill -STOP $task_pid2
echo "Checking task status after pausing second process..."
ps -o pid,stat,cmd -p$task_pid2

#resuming both processes
kill -CONT $task_pid1
echo "Checking task status after resuming first process..."
ps -o pid,stat,cmd -p$task_pid1
kill -CONT $task_pid2
echo "Checking task status after resuming second process..."
ps -o pid,stat,cmd -p$task_pid2
