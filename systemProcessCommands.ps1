#! /bin/bash

# System Process Commands
# Victor Sullivan
# 20210806



****Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.****
(Get-Counter '\Process(*)\% Processor Time').CounterSamples | Where-Object {$_.CookedValue -gt 0}