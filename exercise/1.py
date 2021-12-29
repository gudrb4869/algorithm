class Math:
    def gcd(self,m,n):
        if m<n:
            m,n=n,m
        if n==0:
            return m
        if (m%n)==0:
            return n
        else:
            return self.gcd(n,m%n)

if __name__=='__main__':
    math=Math()
    print(math.gcd(4,10))