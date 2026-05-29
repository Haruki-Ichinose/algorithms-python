def compress(values):
    sorted_values = sorted(set(values))
    index = {x: i for i, x in enumerate(sorted_values)}
    return [index[x] for x in values], sorted_values


def main():
    values = [100, 10, 1000, 10]
    print(compress(values))


if __name__ == "__main__":
    main()
