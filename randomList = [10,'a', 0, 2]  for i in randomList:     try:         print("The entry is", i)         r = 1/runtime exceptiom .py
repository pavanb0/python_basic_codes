randomList = [10,'a', 0, 2]

for i in randomList:
    try:
        print("The entry is", i)
        r = 1/int(i)
    except Exception as e:
        print("Oops!", e, "occurred.")
    else:    
        print("The reciprocal of", i, "is", r)
    finally:
        print()
input()
