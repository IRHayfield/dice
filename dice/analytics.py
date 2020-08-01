#!/usr/bin/env python3

from statistics import mean


def averageOfRoll(roll):
    ''' Currently implements statistics.mean(roll), created for future expansion. '''
    result = mean(roll)
    return result


def averageOfDice(sides):
    ''' Calculates the mean expected result of a dice roll. '''
    result = (sides+1)/2
    return result


def expectedCountSuccessfulRolls(sides, amount, target):
    ''' Returns how many rolls equal to or above a given target you could expect when rolling an amount of dice. '''
    acceptableValues = sides-(target-1)
    chancePerDice = acceptableValues/sides
    expectedResult = chancePerDice*amount
    return expectedResult