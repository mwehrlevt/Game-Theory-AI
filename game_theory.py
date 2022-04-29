# Lauren and Michelle
# Implement a game theory game generator

import numpy
import yaml


def main():
    # agent (1, 2, 3)
    # Starting:
    # Agent 1: selects an action uniformly at random
    # Agent 2: Start w/ globally highest payout
    # Agent 3: lowest payout


    # game (take two of the agents, and play them in the game)

    # read in yaml file
    with open('data.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    #gameMatrix = numpy.matrix([[1, 2], [3, 4]])
    # model after Prisoner's Dilemma
    #gameMatrix = numpy.array([[[0, 0], [-2, -5]], [[-5, -2], [-10, -10]]])
    #gameMatrix = numpy.array([[[-2, -2], [0, -15]], [[-15, 0], [-10, -10]]])
    gameMatrix = numpy.array([[[-15, -2], [-10, -15]], [[-2, -10], [0, 0]]])

    print(gameMatrix)

    # Pick the first number in each cell
    knownMatrix1 = numpy.array([[gameMatrix[0][0][0], gameMatrix[0][1][0]],
                             [gameMatrix[1][0][0], gameMatrix[1][1][0]]])
    print("Both parties know this matrix")
    print(knownMatrix1)

    knownMatrix2 = numpy.array([[gameMatrix[0][0][1], gameMatrix[0][1][1]],
                             [gameMatrix[1][0][1], gameMatrix[1][1][1]]])
    print("Second known matrix")
    print(knownMatrix2)

    # play dominant strategy game
    dominantStrategy(gameMatrix, knownMatrix1, knownMatrix2)


def dominantStrategy(gameMatrix, knownMatrix1, knownMatrix2):
    # ----------------- Prisoner's Dilemma ---------------------------
    # both players have a dominant strategy - each player will have the best response no matter what
    # the opponent chooses
    #  -------------- player 1 finds their best option -------------
    player1Response1 = ""
    player1Response2 = ""

    # silence is better
    print(knownMatrix1[0][0], knownMatrix1[1][0])
    if knownMatrix1[0][0] > knownMatrix1[1][0]:
        print("silence is better")
        player1Response1 = "Silence"
    else:
        print("talking is better")
        player1Response1 = "Talk"

    # consider what player 2 may do in relation to player 1
    print(knownMatrix1[0][1],  knownMatrix1[1][1])
    if knownMatrix1[0][1] > knownMatrix1[1][1]:
        print("silence is better")
        player1Response2 = "Silence"
    else:
        print("talking is better")
        player1Response2 = "Talk"

    #  ---------- player 2 options ---------------
    player2Response1 = ""
    player2Response2 = ""

    # silence is better
    print(knownMatrix2[0][0], knownMatrix2[0][1])
    if knownMatrix2[0][0] > knownMatrix2[0][1]:
        print("silence is better")
        player2Response1 = "Silence"
    else:
        print("talking is better")
        player2Response1 = "Talk"

    # consider what player 2 may do
    print(knownMatrix2[1][0], knownMatrix2[1][1])
    if knownMatrix2[1][0] > knownMatrix2[1][1]:
        print("silence is better")
        player2Response2 = "Silence"
    else:
        print("talking is better")
        player2Response2 = "Talk"

    # analyze results
    if player1Response1 == "Silence" and player1Response2 == "Silence" and \
            player2Response1 == "Silence" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[0][0])

    elif player1Response1 == "Talk" and player1Response2 == "Talk" and \
            player2Response1 == "Talk" and player2Response2 == "Talk":
        print("Decision: ", gameMatrix[1][1])

    elif player1Response1 == "Talk" and player1Response2 == "Silence" and \
            player2Response1 == "Silence" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[1][0])

    elif player1Response1 == "Silence" and player1Response2 == "Talk" and \
            player2Response1 == "Silence" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[0][0])

    elif player1Response1 == "Talk" and player1Response2 == "Talk" and \
            player2Response1 == "Silence" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[1][0])

    elif player1Response1 == "Silence" and player1Response2 == "Silence" and \
            player2Response1 == "Talk" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[0][1])

    elif player1Response1 == "Silence" and player1Response2 == "Silence" and \
            player2Response1 == "Silence" and player2Response2 == "Talk":
        print("Decision: ", gameMatrix[0][0])

    elif player1Response1 == "Silence" and player1Response2 == "Silence" and \
            player2Response1 == "Talk" and player2Response2 == "Talk":
        print("Decision: ", gameMatrix[0][1])

    elif player1Response1 == "Talk" and player1Response2 == "Talk" and \
            player2Response1 == "Silence" and player2Response2 == "Talk":
        print("Decision: ", gameMatrix[1][1])

    elif player1Response1 == "Talk" and player1Response2 == "Talk" and \
            player2Response1 == "Talk" and player2Response2 == "Silence":
        print("Decision: ", gameMatrix[1][0])


if __name__ == "__main__":
    main()
