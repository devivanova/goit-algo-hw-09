import time

coins = [50, 25, 10, 5, 2, 1]


def count_coins(amount, coins):
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin
    return coin_count


# Функція жадібного алгоритму
def find_coins_greedy(amount):
    return count_coins(amount, coins)


# Функція динамічного програмування
def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

    return count_coins_using_array(amount, coin_used)


def count_coins_using_array(amount, coin_used):
    coin_count = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin
    return coin_count


# Функція для вимірювання часу виконання
def measure_execution_time(func, amount):
    start_time = time.time()
    result = func(amount)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


test_amounts = [113, 1370, 10062, 150073]

for amount in test_amounts:
    greedy_result, greedy_time = measure_execution_time(
        find_coins_greedy, amount)
    dp_result, dp_time = measure_execution_time(find_min_coins, amount)

    print(f"Amount: {amount}")
    print(f"Greedy result: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"DP result: {dp_result}, Time: {dp_time:.6f} seconds\n")
