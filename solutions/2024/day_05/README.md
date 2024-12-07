# Day 5 (2024)

`Print Queue` ([prompt](https://adventofcode.com/2024/day/5))

This script processes order rules and changes to determine the correct sequence of pages. It reads input from a file, parses the rules and changes, and then validates and corrects the order of pages based on the rules.

## Part 1

After sketching out the problem on paper I noticed something. For all valid changes, if you generated a full list of in order pairs, each pair would be in the rules. I also noticed that the first element in the list always as the most pairs, with each element having less and less until the last which has none. I used these two facts to easily parse out valid changes. 

I iterated through each generated rule in each change to determine if it is found in the list of rules. If not, it isn't valid. The already valid case was easy, simply find the middle and add the sum. Part 2 was a little trickier.

## Part 2

I have GitHub CoPilot at work and decided to see how it could help me out. I understood what I needed to do for part 2, but just couldn't figure out how to do it in python. What I wanted to do was remove invalid rules, find the valid versions of those rules, and re-make the rules. This part I could do on my own fairly easy after some stack-overflowing. 

The part I was having issue with was regenerating the page list. Conceptually, it was following my rules I set forth. The first element in the list has the most rules, etc. I just couldn't figure out how to get a count of occurances for the rules. Here was my prompt:

`
Write me a function in python that given a list of Orderrule, returns the count of occurances each 'before' number, and the before number
`

This got me what I was looking for. After that, it was a simple matter of taking the keys sorted by value, and appending the `after` of the rule that only appears once to the list.

CoPilot also wrote the outline for this readme!

## Possible Improvements
This would not work with implied rules. Example 94, 56, 57, 38 with only two rules 94|56, 56|57, 94|38. This would be valid but in this solution it would not be.

## Classes

### OrderRule
Represents a rule that defines the order of pages.
- `before`: The page that should come before.
- `after`: The page that should come after.
- Methods: `__init__`, `__str__`, `__eq__`, `Contains`.

### Change
Represents a change in the order of pages.
- `orderPages`: List of pages in the current order.
- `rules`: List of `OrderRule` objects Generated from `orderpages`.
- Methods: `__init__`, `__str__`, `GetMiddle`, `FixRules`, `ReGenerateOrder`.

## Functions

### Part1(changes, rules)
Calculates the sum of the middle pages of valid changes.

### Part2(changes, rules)
Fixes invalid changes, regenerates the order, and calculates the sum of the middle pages.