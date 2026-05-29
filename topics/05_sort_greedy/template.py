def main():
    intervals = [(1, 3), (2, 4), (3, 5)]
    intervals.sort(key=lambda x: x[1])
    print(intervals)


if __name__ == "__main__":
    main()
