if __name__ == "__main__":

    list_input = [-2, 3, 1, -4, 10, -3, 30, -23]
    rearrange = lambda list: [x for x in list if x < 0] + [x for x in list if x == 0] + [x for x in list if x > 0] 
    print(rearrange(list_input))