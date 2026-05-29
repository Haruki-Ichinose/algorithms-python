def main():
    n = 5
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] += dp[i]
    print(dp[n])


if __name__ == "__main__":
    main()
