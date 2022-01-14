def safe_input():
    try:
       x = input()
    except KeyboardInterrupt:
        return
    return x
