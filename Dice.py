# region imports
from Die import rollFairDie, rollUnFairDie
# endregion

# region functions
def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    score = [0]

    for i in range (N):
        values = rollFairDie()
        score[0] += values

    return(score[0])



def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    score = [0]

    for i in range(N):
        values = rollUnFairDie()
        score[0] += values

    return(score[0])



# endregion

if __name__ == "__main__":

    print(rollDice())
    print(rollUnFairDice())