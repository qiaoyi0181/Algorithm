def kara(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)), len(str(y)))
        m2 = m // 2

        a = x // 10**(m2)
        b = x % 10**(m2)
        c = y // 10**(m2)
        d = y % 10**(m2)

        ac = kara(a,c)
        bd = kara(b,d)
        ab_cd = kara(a+b, c+d)-ac-bd

        prod = (10**(2*m2))*ac + (10**(m2))*ab_cd + bd

        return prod

print(kara(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
