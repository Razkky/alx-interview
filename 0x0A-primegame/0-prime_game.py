#!/usr/bin/python3
"""Contains a function to determine the winner of a game"""

def isWinner(x, nums):
    """Determine the winner of the game"""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            return True

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
