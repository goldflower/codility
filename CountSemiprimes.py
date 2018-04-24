def make_primes(N):
    primes=[-1]*N
    c=2
    while c*c < N:
        ii=2*c
        while(ii<N):
            primes[ii]=c
            ii+=c
        c+=1
    return primes
def solution(N, P, Q):
    N=N+1
    primes=make_primes(N)
 
    prefix=[0]*N
 
    for x in xrange(1,N):
        prefix[x]=prefix[x-1]
        first_factor=primes[x]
        second_factor=x/first_factor
        if(primes[x]!=-1 and primes[first_factor]==-1 and primes[second_factor]==-1):
            prefix[x]+=1
 
    results=[]
    for r in xrange(len(P)):
        results.append(prefix[Q[r]]-prefix[P[r]-1])
    return results