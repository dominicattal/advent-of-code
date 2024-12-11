#!/bin/bash

grep -Eo "mul\([0-9]+,[0-9]+\)" input.txt | sed -E "s/mul\(([0-9]+),([0-9]+)\)/\1 \2/g" > nums.txt
grep -Eo "(mul\([0-9]+,[0-9]+\)|do|don't)" input.txt | sed -E "s/mul\(([0-9]+),([0-9]+)\)/\1 \2/g" > nums2.txt