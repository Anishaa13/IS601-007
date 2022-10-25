from array import array


a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    if (type(arr[0])==str):
        for value in arr:
            if int(value)<0:
                print(str(-1*int(value)))
            else:
                print(str(int(value)))
    else:
        for value in arr:
            if value <0:
                print(-1*value)
            else:
                print(value)            
    # TODO add new code here to print the desired result

print("UCID: as4283 , Date-09/24/2022, Explaination: I have used if loop to print positive values")
print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)