class IMovingAverage(object):
    def __init__(self, n):
        """
        This is the interface for moving average of last n element added
        elements (array): Added numbers will be store here
        elements_count (int): Represent the number of elements in elements array
        n (int): Represents how many last elements you want to calculate the average on
        average_last_n_elements (int): The average of last n elements
        Parameters:
        n (int): Define how many last elements to calculate the moving average
        """
        self.elements = []
        self.elements_count = 0
        self.n = n
        self.average_last_n_elements = None

    @property
    def average(self):
        """
        The average of last n elements
        Parameters:
        Returns:
        self.average_last_n_elements (int): The average of last N elements
        """
        return self.average_last_n_elements

    def add(self, num):
        """
        Parameters:
        num (int): The element that is being added to the data structure
        """
        raise NotImplementedError

    def get(self, idx):
        """
        Get element at input index
        Parameters:
        idx (int): index of element we need to get
        """
        raise NotImplementedError


class MovingAverageImpl(IMovingAverage):
    def __init__(self, n):
        """
        This is a implementation of moving average
        last_n_sum (integer): The sum of last n elements
        last_n_count (integer): the number of elements already calculated
        """
        super(MovingAverageImpl, self).__init__(n)
        self.last_n_elements_sum = 0
        self.last_n_elements_count = 0

    def add(self, num):
        """
        Adding number to elements,
        Calculate average of the last n elements.
        Parameters:
        num (int): The element that is being added to the data structure
        Returns:
        """
        self.elements.append(num)
        self.elements_count += 1
        if self.last_n_elements_count == self.n:
            remove = self.elements[self.elements_count-1-self.last_n_elements_count]
            self.last_n_elements_sum = self.last_n_elements_sum-remove+num
        else:
            self.last_n_elements_sum += num
            self.last_n_elements_count += 1
        self.average_last_n_elements = (1.0*self.last_n_elements_sum)/self.last_n_elements_count

    def get(self, idx):
        """
        Get element at input index
        Parameters:
        idx (int): index of element we need to get
        Returns:
          Element at index
        """
        return self.elements[idx]
