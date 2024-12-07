# Day 6 (2024)

`Guard Gallivant` ([prompt](https://adventofcode.com/2024/day/6))

This was a really fun day! Reminds me of pokemon ice puzzles!

## Part 1

Part 1 I was able to do on my own. It isn't clean, but I spent a lot of time writing out a guard and a grid to move them on. I apparently was thinking in the wrong demensions because I had to switch the x and y of all my positions when checking. But other than that (which frankly was annoying to find and instead of rewriting everything I only rewrote the base checking funcs), the puzzle went pretty smooth. I just updated every position along the way as X and then counted all the x's.

## Part 2

Part 2 I got some help with. I learned from the subreddit that brute forcing all positions was a popular way to approach it. I also learned that you can short cut this by just checking all positions along the original path since anything else is a no-op. This was, okay. No matter how much I increased the max iterations (up to 10,000,000 at one point) I was still getting too many answers. I realized that my loop detection is actually just in-correct when I found a loop from the example that doesn't cross the starting path.

This kind of sent me down a spiral where I just couldn't figure out how to fix my code. I believe my original (named solution_original.py) would work with a high enough max iteration count. But, that could take hours or days to find a high enough max count. Currently, the original code gets an answer of 1950 in a resonable amount of time.

This lead my to look at other people's answers and try to find ways to tackle part 2. I found a good solution [here](https://github.com/WinslowJosiah/adventofcode/blob/main/aoc/2024/day06/__init__.py), thanks for the suggestions! I saw this user tracked the path of the guard with not only position, but direction. This was the key since finding a point where the guard is going the same direction on a tile they visited means they will loop.

I still wanted to reuse my classes, so I went about modifying my code to fit this new approach. However, this got me slightly higher at 1952, and still correct for part 1. During the test, my code successfully gets the correct looping paths and amount, but when expanded fails. I am not sure. I will come back to this