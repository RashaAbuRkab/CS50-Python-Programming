class Jar:
    def __init__(self, capacity=12):
        # Ensure the capacity is valid
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # Initialize the jar as empty

    def __str__(self):
        # Return a string with the current number of cookies
        return f"{'🍪' * self._size}"

    def deposit(self, n):
        # Validate the number of cookies to deposit
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Not enough capacity in the jar")
        self._size += n

    def withdraw(self, n):
        # Validate the number of cookies to withdraw
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


# Test the functionality manually
def main():
    jar = Jar()
    jar.deposit(5)  # Deposit 5 cookies
    print(jar)      # Should print 5 cookies 🍪🍪🍪🍪🍪
    jar.withdraw(2) # Withdraw 2 cookies
    print(jar)      # Should print 3 cookies 🍪🍪🍪


if __name__ == "__main__":
    main()
