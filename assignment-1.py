def read_file(my_file):
    data = []

    with open(my_file) as file:
        for line in file:
            data.append([line.strip()])
    return data

def main():
    product_data = read_file("product_data.txt")
    products = []

    for i in range(len(product_data)):
        products.append((product_data[i])[0].split(','))

    def create(id, name, price, category):
        products.append([id, name, price, category])

    def search_by_id(id):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                print(f"{products[i][0]},{products[i][1]},{products[i][2]},{products[i][3]}")

    def search_by_name(name):
        for i in range(len(products)):
            if (products[i][1]).strip() == name:
                print(products[i][0], products[i][1], products[i][2], products[i][3])

    search_by_id(44574)
    # print(products)
    return 0
main()