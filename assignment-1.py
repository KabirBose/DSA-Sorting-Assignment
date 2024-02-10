
def read_file(my_file):
    data = []

    with open(my_file) as file:
        for line in file:
            data.append(line.rstrip())
    return data

def create_store(data):
    store = {
        "ids": [],
        "names": [],
        "prices": [],
        "categories": []
    }

    for i in range(len(data)):
        store["ids"].append(((data[i].split(","))[0]).strip())
        store["names"].append(((data[i].split(","))[1]).strip())
        store["prices"].append(((data[i].split(","))[2]).strip())
        store["categories"].append(((data[i].split(","))[3]).strip())
    return store

def main():
    product_data = create_store(read_file("product_data.txt"))

    def add_product(id, name, price, category):
        product_data["ids"].append(id)
        product_data["names"].append(name)
        product_data["prices"].append(price)
        product_data["categories"].append(category)
    
    def delete_product(id):
        for i in range(len(product_data["ids"])):
            if (product_data["ids"])[i] == id:
                (product_data["ids"]).remove((product_data["ids"])[i])
                (product_data["names"]).remove((product_data["names"])[i])
                (product_data["prices"]).remove((product_data["prices"])[i])
                (product_data["categories"]).remove((product_data["categories"])[i])
            else:
                print("This ID does not exist!")

    def search_product(id, name):
        for i in range(len(product_data["ids"])):
            if (product_data["ids"])[i] == id or (product_data["names"])[i] == name:
                print((product_data["ids"])[i], (product_data["names"])[i], (product_data["prices"])[i], (product_data["categories"])[i])
            else:
                print("This product does not exist!")

    search_product(0, "Mystery MGSPG")
    # print(product_data["names"])

    return 0
main()