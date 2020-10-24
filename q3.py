def main(int1, int2):
    low = int1

    if int2 < int1:
        low = int2

    for i in list(range(low)).__reversed__():
        i += 1

        if int1 % i == 0 and int2 % i == 0:
            int1 /= i
            int2 /= i
            

    return "The reduced fraction is: {}/{}".format(int(int1), int(int2))

if __name__ == "__main__":
    print(
        main(
            int(input("Enter numerator: ")),
            int(input("Enter denominator: "))
        )
    )