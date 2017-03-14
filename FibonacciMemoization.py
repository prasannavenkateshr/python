class Fibonacci_Memoization ():
    def __init__(self):
        self.MAX_SIZE = 100
        self.LookUp = list([-1]* self.MAX_SIZE)

    def FindFibonacci (self, N):
        if (self.LookUp[N] == -1):
            if N <= 1:
                self.LookUp[N] = N
            else:
                self.LookUp[N] = self.FindFibonacci (N-1) + self.FindFibonacci (N-2)
        return self.LookUp[N]
