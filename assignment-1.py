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
    
    def update(id, n_id, name, price, category):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                products[i] = [n_id, name, price, category]
        print(f"Product was successfully updated")

    def search_by_id(id):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")

    def search_by_name(name):
        for i in range(len(products)):
            if (products[i][1]).strip().lower() == name.lower():
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")
    
    def delete(id):
        prod_id = 0
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                prod_id = i

        products.pop(prod_id)
        print(f"Product {id} was successfully deleted")

    delete(44574)
    create(39103, "Lobster LBSTR", 63, "Food")
    search_by_id(44574)
    search_by_name("Knife Set ASRHX")
    update(69525, 10293, "Caviar", "102", "Food")

    print(products)

    return 0
main()