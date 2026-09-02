from itertools import permutations

def is_lucky_ticket(digits:tuple[int]):
    if len(digits) != 6:
        return False

    sum_first_half = sum(digits[:3])
    sum_second_half = sum(digits[3:])

    return sum_first_half == sum_second_half

def can_form_lucky_ticket(digits:list[int]):
    if len(digits) != 6:
        return False

    for perm in set(permutations(digits)):
        if sum(perm[:3]) == sum(perm[3:]):
            return True
        return False

if __name__ == '__main__':
    ticket1 = (1,2,3,4,5,6)
    print(f"Билет счастливый: {is_lucky_ticket(ticket1) or can_form_lucky_ticket(ticket1)}")

    ticket2 = (0,0,0,0,0,0)
    print(f"Билет счастливый: {is_lucky_ticket(ticket2) or can_form_lucky_ticket(ticket2)}")

    ticket3 = (1,2,6,3,4,2)
    print(f"Билет счастливый: {is_lucky_ticket(ticket3) or can_form_lucky_ticket(ticket3)}")

    ticket4 = (1,2,6,0,0,6)
    print(f"Билет счастливый: {is_lucky_ticket(ticket4) or can_form_lucky_ticket(ticket4)}")