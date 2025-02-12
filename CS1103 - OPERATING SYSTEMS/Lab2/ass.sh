#!/bin/bash
# Start a background task (using sleep to simulate a long-running task)
echo "Starting a background task..."
sleep 300 & # Run for 5 minutes in the background
task_pid=$! # Capture the PID of the background task
echo "Background task started with PID: $task_pid"
# Display the jobs running in the background
echo -e "\nListing jobs:"
jobs

# Check if the process is running using ps
echo -e "\nChecking if the task is running..."
ps -p $task_pid

# Pausing the background task
echo -e "\nPausing the background task..."
kill -STOP $task_pid
ps -o pid,stat,cmd -p$task_pid
kill -CONT $task_pid#res
ps -o pid,stat,cmd -p$task_pid
