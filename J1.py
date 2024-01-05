def KPA (B):
    P = 5*B-400

    sea_level=0

    if (B>100):
        sea_level = -1
    elif (B<100):
        sea_level = 1
    else:
        sea_level = 0

    return P, sea_level


def main():
    try: 
        B = int(input())
        KPA(B)
    except ValueError: 
        print("Enter a number")

    P, sea_level = KPA(B)
    print(P)
    print(sea_level)


if __name__ == "__main__":
    main()