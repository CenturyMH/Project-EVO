def readwrite():
    with open(r"C:\Users\Martin\Desktop\python_test\textfiletest.txt", mode="r") as f:
        for line in f:
            print(line)

readwrite()
