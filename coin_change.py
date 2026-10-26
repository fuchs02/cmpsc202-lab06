from time import perf_counter
import matplotlib.pyplot as plt

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    minimum = amount + 1

    for coin in coins:
        if coin <= amount:
            coins_needed = 1 + coin_change_recursive(
                coins, amount - coin
            )
            minimum = min(minimum, coins_needed)

    return minimum


# amount = 11
# coins = [1, 2, 5]
# coin_count = coin_change_recursive(coins, amount)
# print(coin_count)

def coin_change_memoized(coins, amount, memo):
    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    if amount in memo:
        return memo[amount]

    minimum = amount + 1
    
    for coin in coins:
        if coin <= amount:
            coins_needed = 1 + coin_change_memoized(
                coins, amount - coin, memo
            )
            minimum = min(minimum, coins_needed)

    memo[amount] = minimum
    return minimum
        

# amount = 11
# coins = [1, 2, 5]
# memo = {0:0}
# coin_count = coin_change_memoized(coins, amount, memo)
# print(coin_count)
# print(memo)


def coin_change_dp(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]

# amount = 11
# coins = [1, 2, 5]
# coin_count = coin_change_dp(coins, amount)
# print(coin_count)


def main():
    # Keep inputs small because the naive recursive algorithm is exponential.
    tests = [5, 10, 15]
    coins = [1,2,5]
    memo = {0:0}
    benchmark_times = []
    memoized_times = []
    dp_times = []
    print("running tests...")
    for t in tests:
        t_difference = 0
        for _ in range(10):
            t_start = perf_counter()
            coin_change_recursive(coins, t)
            t_end = perf_counter()
            t_difference += t_end - t_start
        benchmark_times.append(t_difference/10)

        t_difference = 0
        for _ in range(10):
            t_start = perf_counter()
            coin_change_memoized(coins, t, memo)
            t_end = perf_counter()
            t_difference += t_end - t_start
        memoized_times.append(t_difference/10)

        t_difference = 0
        for _ in range(10):
            t_start = perf_counter()
            coin_change_dp(coins, t)
            t_end = perf_counter()
            t_difference += t_end - t_start
        dp_times.append(t_difference/10)

    plt.figure(figsize=(10, 6))
    plt.plot(tests, benchmark_times, marker="o", label="Baseline algorithm")
    plt.plot(tests, memoized_times, marker="o", label="Memoized strategy")
    plt.plot(tests, dp_times, marker="o", label="DP strategy")
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm Runtime Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.yscale('log')
    plt.plot(tests, benchmark_times, marker="o", label="Baseline algorithm")
    plt.plot(tests, memoized_times, marker="o", label="Memoized strategy")
    plt.plot(tests, dp_times, marker="o", label="DP strategy")
    plt.xlabel("Input size")
    plt.ylabel("Time (seconds)")
    plt.title("Algorithm Runtime Comparison (Log scale)")
    plt.legend()
    plt.grid(True)
    plt.show()

main()