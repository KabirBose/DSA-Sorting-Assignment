
def main():
    product_data = []

    with open("product_data.txt") as file:
        for line in file:
            product_data.append([line.rstrip()])

    print(product_data)

    return 0

main()