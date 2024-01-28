
def hanoi_rec(num_disks, source, destination):
    if(num_disks == 1):
        print(f"Move disk 1 from {source} to {destination}")
    else:
        tmp = [x for x in ["A","B","C"] if x != source and x != destination]
        auxiliary = tmp[0]

        hanoi_rec(num_disks-1, source, auxiliary)

        print(f"Move disk {num_disks} from {source} to {destination}")

        hanoi_rec(num_disks-1, auxiliary, destination)

def hanoi(num_disks):
    hanoi_rec(num_disks,"A","C")


if __name__ == "__main__":
    hanoi(3)