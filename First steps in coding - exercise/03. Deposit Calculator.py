depositSum = float(input())
expDeposit = int(input())
yearlyInterestProcentage = float(input())
sumInterest = depositSum * (yearlyInterestProcentage / 100)
yearlySumInterest = sumInterest / 12
totalSum = depositSum + expDeposit * yearlySumInterest
print(totalSum)