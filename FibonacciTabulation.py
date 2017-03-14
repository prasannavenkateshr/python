class Fibonacci_Tabulation ():
    def FindFibonacci (self, N):
        self.Fibo = [-1]*(N+1)
        self.Fibo[0], self.Fibo[1] = 0, 1
        for i in xrange(2, N+1):
            self.Fibo[i] = self.Fibo[i-1] + self.Fibo[i-2]
        return self.Fibo[N]
