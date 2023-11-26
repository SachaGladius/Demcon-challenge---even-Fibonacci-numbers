
def fibonacci_even(in_0: int, in_1: int, answer: int, cnt_mod3: int) -> tuple[int, int]:
    """
    fibonacci challenge demcon

    Calculates sum of even fibonacci numbers for numbers not exceeding 4 million

    in_0: first of fibonacci pair
    in_1: second of fibonacci pair
    answer: sum of even fibonacci numbers, so far
    cnt_mod3: module 3 counter to follow odd/even pattern

    returns: fibonacci sum and sum of even fibonacci numbers
    """

    if LIMIT <= in_1:
        # stop when fibonacci number exceeds specified limit
        return in_0, answer
    else:
        # fibonacci sum
        in_2 = in_0 + in_1

        # modulo 3 counter
        # follows pattern of odds and evens
        # with this start always need addition of two odds to get even result again
        # counting avoids 'even' testing for each number
        if cnt_mod3 == 2: 
            # combined counter reset
            # and even selection
            cnt_mod3 = 0

            # in_1 has to be even, so add
            answer += in_1
        else:
            # count
            cnt_mod3 += 1

        # print(in_0, in_1, in_2, answer)
        return fibonacci_even(in_1, in_2, answer, cnt_mod3)

# Stop when Fibonacci number exceeds 4 million
LIMIT = 4000000

if __name__ == "__main__":

    _, answer = fibonacci_even(in_0=1, in_1=2, answer=0, cnt_mod3=2)
    print('Answer: {}'.format(answer))
  
