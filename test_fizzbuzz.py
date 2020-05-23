class TestFizzBuss():
    def test_get_fizz_when_input_is_3(self):
        result = fizzbuzz(3)
        assert result == 'Fizz'

    def test_get_buzz_when_input_is_5(self):
        result = fizzbuzz(5)
        assert result == 'Buzz'

    def test_get_fizzbuzz_when_input_is_15(self):
        result = fizzbuzz(15)
        assert result == 'FizzBuzz'

    def test_get_1_when_input_is_1(self):
        result = fizzbuzz(1)
        assert result == 1


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    if number % 3 == 0:
        return 'Fizz'
    if number % 5 == 0:
        return 'Buzz'
    else:
        return number

