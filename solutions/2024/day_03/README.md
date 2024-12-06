# Day 3 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/3))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Part 1 was pretty easy once I realized I could simply use regex to parse out where I needed any muls. For some reason, when I used regex101.com my patern grabbed the entire mul operation, but here in python it simply grabbed the numbers. This ended up beign fine because the mul's where still being matched and not returning extra data. This is my first time doing regex parsing in python so I assume there is a fix for this.

## Part 2

Part 2 made me realize I would likely have to work on parsing the entire string charecter by charecter. I tried to 'look ahead' with my parsing and instead of trying to build strings I looked ahead to see if the start of what could be an instruction was valid before continuing. I didn't implement any sort of skipping feature so I still read the entire string, but skipping wouldn't save any time complexity anyways.

I am not sure if there would be a way to parse this string with regex that somehow followed instruction order. I bet I could make it work and that would be where I would go first for improvements.