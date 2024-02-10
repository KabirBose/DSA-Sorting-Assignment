
def readFile(my_file):
    data = []

    with open(my_file) as file:
        for line in file:
            data.append(line.rstrip())
    return data


def main():
    product_data = readFile("product_data.txt")
    
    ids = []
    names = []
    prices = []
    categories = []

    for i in range(len(product_data)):
        ids.append((product_data[i].split(","))[0])
        names.append((product_data[i].split(","))[1])
        prices.append((product_data[i].split(","))[2])
        categories.append((product_data[i].split(","))[3])
    
    print(names)

    return 0

main()