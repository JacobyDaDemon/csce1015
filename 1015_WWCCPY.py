def is_credit_card_valid(card_number):
    card_number_str = str(card_number)
    
    if len(card_number_str) < 13 or len(card_number_str) > 19:
        return False

    digits = [int(d) for d in card_number_str[::-1]]
    
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    total_sum = sum(digits)
    
    return total_sum % 10 == 0

def run_tests():
    assert is_credit_card_valid("4111111111111111"), '4111111111111111 should pass but did not'
    assert is_credit_card_valid("5105105105105100"), '5105105105105100 should pass but did not'
    assert not is_credit_card_valid("134"), '134 should not pass but did'
    assert not is_credit_card_valid("1234567890123456"), '1234567890123456 should not pass but did'
    assert not is_credit_card_valid("000000000000"), 'This is a bad test and we will get an error message'

run_tests()
print("All tests passed!")
