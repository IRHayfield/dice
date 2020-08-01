#!/usr/bin/env python3

import argparse

import analytics

from numpy.random import randint


def rollDice(amount, sides):
    ''' Retuns an array of intergers imitating rolling and amount of sided dice. '''
    sides+=1
    result = randint(1, sides, amount)
    return result


def countSuccessfulRolls(array, target):
    ''' Returns count of how many numbers in an array are equal to or above a target. '''
    count = 0
    for i in array:
        if i >= target:
            count += 1

    return count


def getRollOutput(amount, sides, target):
    output = (f"Rolling {amount} d{sides} with a target of {target}+")

    rollResult=rollDice(amount, sides)
    output += "\n" + str(rollResult)
    output += "\n" + (f"Obtained average of {analytics.averageOfRoll(rollResult):.2f} when expected result is {analytics.averageOfDice(sides):.2f}")
    output += "\n" + (f"Obtained {countSuccessfulRolls(rollResult, target):.2f} positive rolls when expected result is {analytics.expectedCountSuccessfulRolls(sides, amount, target):.2f}")
    return output


def main():

    parser = argparse.ArgumentParser(prog='dice.py', usage='%(prog)s [options]')
    parser.add_argument('-s', '--sides', type=int, required=True, dest="sides", help='Amount of sides the dice to be rolled have.')
    parser.add_argument('-a', '--amount', type=int, required=True, dest="amount", help='Amount of dice to be rolled.')
    parser.add_argument('-t', '--target', type=int, required=True, dest="target", help='Target number you hope the dice rolled are at or above.')
    args = parser.parse_args()

    sides=args.sides
    amount=args.amount
    target=args.target

    output = getRollOutput(amount, sides, target)
    print (output)


if __name__ == '__main__':
    main()