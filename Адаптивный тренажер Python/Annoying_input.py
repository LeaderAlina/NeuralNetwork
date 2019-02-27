def get_int(start_message, error_message, end_message):
    n = input()
    print(start_message+'\n'+n)
    while True:
        try:
            int(n)
            break
        except:
            None
        n = input()
        print(error_message+'\n'+n)
    print(end_message)
    return int(n)
