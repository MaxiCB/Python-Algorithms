import sys

def eating_cookies(n, cache=None):
    # There is only one way to handle 0 cookies
    if n == 0:
        return 1
    # Only one way to handle negative cookies
    elif n < 0:
        return 0
    # If cache and cache[n] greater than 0 return cache[n]
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        # If no cache create it
        if not cache:
            cache = [0 for thing in range(n+1)]
        # Set the cache[n] to the producs of recursive calls to eating_cookies with n-1..n-3
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        # Return cache[n]
        return cache[n]

if __name__ == '__main__':
    print(eating_cookies(3))
