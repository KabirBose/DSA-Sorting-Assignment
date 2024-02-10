# Kabir Bose - 100862410
# DS & A Assignment 1

# function that takes a file name as input, reads each, and returns each line in an array
def read_file(my_file):
    data = []

    # standard python file reading function
    with open(my_file) as file:
        for line in file:
            data.append([line.strip()])
    return data

# simple insertion sort algorithm that sorts id in ascending order
def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index][0]
        i = index - 1
        
        while i >= 0:
            if value < list[i][0]:
                list[i+1][0] = list[i][0]
                list[i][0] = value
                i -= 1
            else:
                break
    return list

# main function that manipulates file data
def main():
    # calls the file reader function and stores the raw, unformatted data
    product_data = read_file("product_data.txt")

    # empty array that will hold the formatted data
    products = []

    # breaks each line from the text file data down into multiple arrays by splitting them by comma separation
    for i in range(len(product_data)):
        products.append((product_data[i])[0].split(','))

    # function to add items to the array
    def create(id, name, price, category):
        products.append([id, name, price, category])
    
    # function to update items in the array
    def update(id, name, price, category):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                products[i] = [id, name, price, category]
        print(f"Product was successfully updated")

    # function that searches for items by id
    def search_by_id(id):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")

    # function that searches for items by name
    def search_by_name(name):
        for i in range(len(products)):
            if (products[i][1]).strip().lower() == name.lower():
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")
    
    # function that deletes items given their id
    def delete(id):
        prod_id = 0
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                prod_id = i

        products.pop(prod_id)
        print(f"Product {id} was successfully deleted")

    # examples of all the function calls being used
    # print(insertion_sort(products))
    # delete(44574)
    # create(39103, "Lobster LBSTR", 63, "Food")
    # search_by_id(44574)
    # search_by_name("Knife Set ASRHX")
    update(57353, "Caviar CVRNB", "102", "Food")

    for i in range(len(products)):
        print(products[i])

    return 0
main()