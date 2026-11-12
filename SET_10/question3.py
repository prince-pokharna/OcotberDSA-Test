n = int(input())
prices = list(map(int, input().split()))

lowest_price = prices[0]
best_profit = 0

for i in range(1, n):
    profit = prices[i] - lowest_price
    if profit > best_profit:
        best_profit = profit
    if prices[i] < lowest_price:
        lowest_price = prices[i]

print(best_profit)