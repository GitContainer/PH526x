import random


def majority_vote(votes):
    """
    Find the majority of votes
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winners = []
    max_count = max(vote_counts.values())

    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
        print(vote, count)

    return random.choice(winners)


votes = [1, 2, 3, 1, 2, 3, 1, 2, 3, 3, 3, 2, 2]
winner = majority_vote(votes)

print(winner)
