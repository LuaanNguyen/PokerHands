
from collections import Counter
import sys 

RANK_MAP = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

HIGH, PAIR, TWO_PAIR, TRIPS, STRAIGHT, FLUSH, FULL_HOUSE, QUADS, STRAIGHT_FLUSH = range(9)


def parse_card(tok):
    return (RANK_MAP[tok[0]], tok[1])
    
def straight_high_check(ranks):
    uniq = sorted(set(ranks))
    if len(uniq) < 5:
        return None
    if uniq[-1] - uniq[0] == 4:
        return uniq[-1] 
    if set(uniq) == {14, 2, 3, 4, 5}:
        return 5
    return None

def evaluate_hand(cards):
    """
    cards: list of 5 (rank:int, suit:str) tuples.
    Returns: (category:int, tiebreak_vector:list[int])
    """
    ranks = [r for r, _ in cards]
    suits = [s for _, s in cards]
    
    rank_count = Counter(ranks)
    suit_count = Counter(suits)
    counts_desc = sorted(rank_count.values(), reverse = True)
    is_flush = max(suit_count.values()) == 5
    straight_high = straight_high_check(ranks)
    
    if is_flush and straight_high is not None:
        return (STRAIGHT_FLUSH, [straight_high])
    if counts_desc == [4, 1]:
        quad = max((r for r, c in rank_count.items() if c == 4))
        kicker = max((r for r, c in rank_count.items() if c == 1))
        return (QUADS, [quad, kicker])
    if counts_desc == [3, 2]:
        trip = max((r for r, c in rank_count.items() if c == 3))
        pair = max((r for r, c in rank_count.items() if c == 2))
        return (FULL_HOUSE, [trip, pair])
    if is_flush:
        return (FLUSH, sorted(ranks, reverse=True))
    if straight_high is not None:
        return (STRAIGHT, [straight_high])
    if counts_desc == [3, 1, 1]:
        trip = max((r for r, c in rank_count.items() if c == 3))
        kickers = sorted((r for r, c in rank_count.items() if c == 1), reverse=True)
        return (TRIPS, [trip] + kickers)
    if counts_desc == [2, 2, 1]:
        # Two Pair
        pairs = sorted([r for r, c in rank_count.items() if c == 2], reverse=True)
        kicker = max((r for r, c in rank_count.items() if c == 1))
        return (TWO_PAIR, pairs + [kicker])
    if counts_desc == [2, 1, 1, 1]:
        # One Pair
        pair = max((r for r, c in rank_count.items() if c == 2))
        kickers = sorted((r for r, c in rank_count.items() if c == 1), reverse=True)
        return (PAIR, [pair] + kickers)
    # High Card
    return (HIGH, sorted(ranks, reverse=True))
    
def winner_for_line(line: str) -> str: 
    tokens = line.split()
    p1 = [parse_card(t) for t in tokens[:5]]
    p2 = [parse_card(t) for t in tokens[5:]]
    s1 = evaluate_hand(p1)
    s2 = evaluate_hand(p2)
    
    return "Player 1" if s1 > s2 else "Player 2"

def main():
    data = [ln.strip() for ln in sys.stdin if ln.strip()]
    num_of_testcases = data[0]
    for i in range(1, int(num_of_testcases) + 1):
        print(winner_for_line(data[i]))
    
if __name__ == "__main__":
    main()