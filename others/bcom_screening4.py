class Problem4(object):
    N = None
    items = None
    result = 0 # default output
    """
    Sum of 2 numbers in an array
    Identify whether there exists a pair of numbers in an array such that their sum is equal to N.

    Input:
    The first line contains one integer N, which is the sum we are trying to find
    The second line contains one integer M, which is length of the array
    This is followed by M lines each containing one element of the array.

    Output:
    Output 1 if there exists a pair of numbers in the array such that their sum equals N. If such a pair does not exist, output 0.
    """

    def naive_input(self):
        self.N = int(raw_input("N:"))
        M = int(raw_input("M:"))
        self.items = []
        for _ in range(0, M):
            self.items.append(int(raw_input()))

    def naive_impl(self):
        i = 0
        l = len(self.items)
        while i <= l - 2:
            num = self.N - self.items[i]
            k = i+1
            while k <= i - 1:
                if self.items[k] == num:
                    self.result = 1
                    return
                k += 1
            i += 1

    def store_in_hash(self):
        self.items = {}
        self.N = int(raw_input("N:"))
        M = int(raw_input("M:"))
        for _ in range(0, M):
            item = int(raw_input())
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

    def hash_impl(self):
        for k in self.items.keys():
            num = self.N - k
            # handle special case
            if num == k and self.items[k] != 1:
                self.result = 1
                return
            if num in self.items:
                self.result = 1
                return

    def output(self):
        self.naive_impl()
        print(self.result)




def test():
    p = Problem4()
    p.naive_input()
    p.output()
