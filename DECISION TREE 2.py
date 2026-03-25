# Simple Decision Tree

def decision_tree(hours):

    if hours >= 5:
        return "Pass"
    else:
        return "Fail"


h = int(input("Enter study hours: "))

result = decision_tree(h)

print("Result:", result)
