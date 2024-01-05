def min_swaps_to_arrange_books(books):
    l_count, m_count, s_count, swaps = 0, 0, 0, 0

    for book in books:
        if book =='L':
            l_count += 1
            swaps += m_count + l_count + s_count - 1
        elif book == 'M':
            m_count += 1
        elif book == 'S':
            s_count += 1
    return swaps


def main():
    books = input().strip()
    result = min_swaps_to_arrange_books(books)
    print (result)



if __name__ == "__main__":
    main()