### PokerHands:

[Problem](https://www.hackerrank.com/contests/projecteuler/challenges/euler054/problem)

### Variables

#### Static (once)

- `RANK_MAP`

```json
{
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 5,
  "8": 8,
  "9": 9,
  "T": 10,
  "J": 11,
  "Q": 12,
  "K": 13,
  "A": 14
}
```

- CATEGORY_MAP

```json
{
  "High": 0,
  "Pair": 1,
  "TwoPair": 2,
  "Trips": 3,
  "Straight": 4,
  "Flush": 5,
  "FullHouse": 6,
  "Quads": 7,
  "StraightFlush": 8
}
```

#### Per hand (derived)

- `cards`: list of `(rank: int, suit: char)` from the 5 tokens
- `ranks`: list of 5 ints (with dups)
- `suits`: list of 5 chars

#### Counters & Sorted views

Example: `5H 5C 6S 7S KD`

- `rank_count`: dict[int -> int]
  - Maps the frequency of each rank

```json
{
  "5": 2,
  "6": 1,
  "7": 1,
  "13": 1
}
```

- `suit_count`: dict[char -> int]
  - Maps the frequency of each suit

```json
{
  "H": 1,
  "C": 1,
  "S": 2,
  "D": 1
}
```

- `ranks_desc`: ranks sorted high-> low (with dups) for high-card/flush tiebreaks

```
[13, 7, 6, 7, 5, 5]
```

- `unique_ranks_asc`: sorted low -> high with unique ranks (no dups) for straight checks

```
[5, 6, 7, 13]
```

### Boolean & signatures

- `is_flush`: check for flush
  - `max(suit_count.values()) == 5`

```
False
```

- `straight_high`: None or `5...14`
  - Make sure to handle wheel `14,2,3,4,5 -> 5`

```
None
```

- `counts_sorted_desc`: multiple count sorted in descending order

```
[2, 1, 1, 1]
```

- `ranks_by_freq`: dict[count -> List[rank]], helps build tie breaks

```
{2:[5], 1:[13, 7, 6]}
```

### Output:

- `category_number`: `0..8`

```
1
```

- `tiebreak_vector`: list[int]

```
[5, 13, 7, 6]
```

- `score`: `(category_number, tiebreak_vector)`

```
(1, [5, 13, 7, 6])
```

## Run

```
python3 solution.py < input.txt
```
