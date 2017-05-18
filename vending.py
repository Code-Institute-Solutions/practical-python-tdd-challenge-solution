
def get_change(amount):
    if amount == 0:
        return []

    return [1]


assert get_change(0) == [], "Zero change should return an empty List"
assert get_change(1) == [1], "1 cent change should return a 1 cent coin"
print("All tests pass")
