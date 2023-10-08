# [Cube Rubric Site](http://cuberubrics.org)

The public hosting site for the CubeRubric

## Planned Site Map

Roughly organized from least to most "inside baseball"

### Index

A splash page for navigation, most designed page, intended to appeal to a new
audience member or curious passerby

### News

Blog posts about the site and/or the cubing world

### Events

Upcoming events and tournaments

### Stats

HTML table of statistics for all the fastest times in each event or whatever

### Analysis

Algorithms, learning and optimization tools

--- 

## Preliminary notes

Outline of ideas for the new speed cubing website from 
[Patrick Ingham](mailto:pingham1991@cuberubrics.org) and 
[Crystal Calvert](mailto:crystal@cuberubrics.org).

### Notation

In standard notation, the faces of a 3 dimensional cube are

- U = upper
- D = down
- B = back
- F = front
- R = right
- L = left

A trailing apostrophe indicating a counterclockwise turn: **U'**

A leading 2 indicates a 180 degree turn: **2U**

A trailing lowercase w indicates a "wide" turn, by default turning 2 columns: **Uw**

In cubes larger than 3x3, these wide turns can be specified to n columns: **4Uw**

#### WCA Regulations

[Current notation standards set by the Word Cube Association](https://www.worldcubeassociation.org/regulations/#article-12-notation)
and leave a lot to be desired and improved on.

#### Functional Trigger Notation

The current standard uses brackets (), [], {}, etc. to indicate functional
groups ("triggers") of moves, but it would be an improvement to take this a 
step further and introduce "functions" to the system. 

#### ECO Codes

[ECO codes in chess](https://www.365chess.com/eco.php)

An equivalent to these for Rubiks cubes, allowing both an "absolute"
alpha-numeric code reference and a "common name" (or multiple). The exact
designation codes are yet to be determined but the format would be roughly:

R024    R U R' U'   "Sexy Move"

U025    U R U' R'   "Reverse Sexy"
