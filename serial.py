"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """Makes the number """
        self.start = start
        self.next_num = start
        
    def __repr__(self):
        return f"SerialGenerator(start = {self.start} next = {self.start + 1})"
    
    def generate(self):
        """Generates the next incrementing serial number"""
        self.next_num += 1
        return self.next_num -1
    
    def reset(self):
        """Resets the serial number to start """
        self.next_num = self.start
