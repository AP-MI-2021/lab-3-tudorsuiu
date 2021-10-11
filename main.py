from typing import List


def all_div_k(lst: List[int], k: int) -> bool:
    """
    Determina daca toate elementele listei sunt divizibile cu k
    :param lst: lista de nr. intregi
    :param k: nr. intreg
    :return: True daca toate elementele listei sunt divizibile cu k, False in caz contrar
    """
    for x in lst:
        if x % k != 0:
            return False
    return True


def test_all_div_k():
    assert all_div_k([], 3) is True
    assert all_div_k([2, 3, 6, 9, 12], 3) is False
    assert all_div_k([3, 6, 9, 12], 3) is True


def get_longest_div_k(lst: List[int], k: int) -> List[int]:
    """
    Determina cea mai lunga subsecventa cu proprietatea ca toate elementele sunt divizibile cu k
    :param lst: lista de nr. intregi
    :param k: nr. intreg
    :return: cea mai lunga subsecventa cu proprietatea ca toate elementele sunt divizibile cu k
    """
    subsecventa_max = []
    for st in range(len(lst)):
        for dr in range(st, len(lst)):
            if all_div_k(lst[st:dr+1], k) is True and len(lst[st:dr+1]) > len(subsecventa_max):
                subsecventa_max = lst[st:dr+1]
    return subsecventa_max


def test_get_longest_div_k():
    assert get_longest_div_k([], 3) == []
    assert get_longest_div_k([2, 3, 6, 9, 5, 12], 3) == [3, 6, 9]
    assert get_longest_div_k([2, 4, 13, 8, 10], 3) == []
    assert get_longest_div_k([2, 3, 4, 6, 9, 12, 10, 15, 18, 21], 3) == [6, 9, 12]


def is_prime(x: int) -> bool:
    """
    Determina daca numarul este prim.
    :param x: nr.intreg
    :return: True daca este prim, False in caz contrar
    """
    if x < 2:
        return False
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


def all_longest_prime_digits(lst: List[int]) -> bool:
    """
    Determina daca toate elementele listei sunt formate doar din cifre prime
    :param lst: lista de nr. intregi
    :return: True daca toate elementele sunt formate doar din cifre prime, False in caz contrar
    """
    for x in lst:
        if x == 0:
            return False
        while x:
            last_digit = x % 10
            if is_prime(last_digit) is False:
                return False
            x = x // 10
    return True


def test_all_longest_prime_digits():
    assert all_longest_prime_digits([0, 2, 3, 5, 7]) is False
    assert all_longest_prime_digits([]) is True
    assert all_longest_prime_digits([2, 3, 5, 7]) is True


def get_longest_prime_digits(lst: List[int]) -> List[int]:
    """
    Determina cea mai lunga subsecventa cu proprietatea ca toate elementele sunt formate doar din cifre prime
    :param lst: lista de nr. intregi
    :return: cea mai lunga subsecventa cu proprietatea ca toate elementele sunt formate doar din cifre prime
    """
    subsecventa_max = []
    for st in range(len(lst)):
        for dr in range(st, len(lst)):
            if all_longest_prime_digits(lst[st:dr+1]) is True and len(lst[st:dr+1]) > len(subsecventa_max):
                subsecventa_max = lst[st:dr+1]
    return subsecventa_max


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([]) == []
    assert get_longest_prime_digits([21, 22, 23, 25, 24, 35, 37, 32, 29]) == [22, 23, 25]
    assert get_longest_prime_digits([21, 24, 34, 29]) == []


def citire_lista():
    lst = []
    n = int(input("Dati numarul de elemente: "))
    for i in range(n):
        lst.append(int(input("lst["+str(i)+"] = ")))
    return lst


def print_menu():
    print("1. Citire date")
    print("2. Determinare cea mai lunga secventa cu proprietatea ca toate numerele sunt divizibile cu k")
    print("3. Determinare cea mai lunga secventa cu proprietatea ca toate numerele sunt formate din cifre prime")
    print("4. Iesire")


def main():
    should_run = True
    lst = []
    while should_run:
        print_menu()
        optiune = input("Selectati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            k = int(input("Citit k-ul: "))
            print("Cea mai lunga subsecventa cu proprietatea ca toate numerele sunt divizibile cu", k, "este: ", get_longest_div_k(lst, k))
        elif optiune == "3":
            print("Cea mai lunga secventa cu proprietatea ca toate numerele sunt formate din cifre prime este: ", get_longest_prime_digits(lst))
        elif optiune == "4":
            should_run = False
        else:
            print("Optiune gresita!")


if __name__ == "__main__":
    test_all_div_k()
    test_get_longest_div_k()
    test_is_prime()
    test_all_longest_prime_digits()
    test_get_longest_prime_digits()
    main()
