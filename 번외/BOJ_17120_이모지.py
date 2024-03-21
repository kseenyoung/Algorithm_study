while True:
    try:
        data = input()
        if ":cat:" in data:
            print("YES")
        elif ":caT:" in data:
            print("YES")
        elif ":cAT:" in data:
            print("YES")
        elif ":cAt:" in data:
            print("YES")
        elif ":Cat:" in data:
            print("YES")
        elif ":CaT:" in data:
            print("YES")
        elif ":CAT:" in data:
            print("YES")
        elif ":CAt:" in data:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
