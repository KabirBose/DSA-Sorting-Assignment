
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
        store["ids"].append((data[i].split(","))[0])
        store["names"].append((data[i].split(","))[1])
        store["prices"].append((data[i].split(","))[2])
        store["categories"].append((data[i].split(","))[3])
    return store

def main():
    product_data = create_store(read_file("product_data.txt"))

    print(product_data["ids"])

    return 0
main()