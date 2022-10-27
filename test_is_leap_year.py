from is_leap_year import isLeapYear

# == Testing the function as a whole first ==
# ANEL HADZIC

def test_verify_that_year_is_a_leap_year():
    assert isLeapYear(2000)

def test_verify_that_year_is_not_a_leap_year():
    assert not isLeapYear(1800)

# -- When the year is a leap year --
# Når det er delelig med 4, men ikke 100
def test_veryify_that_year_is_divisible_by_four_but_not_100():
    assert isLeapYear(4)

# Når det er delelig med 400
def test_verify_that_year_is_divisable_by_400():
    assert isLeapYear(400)

# -- When the year is not a leap year --
# Når det ikke er delelig med 4
def test_verify_that_year_is_not_divisable_by_4():
    assert not isLeapYear(5)

# Når det er delelig med 100, men ikke 400.
def test_verify_that_year_is_divisable_by_100_but_not_400():
    assert not isLeapYear(200);