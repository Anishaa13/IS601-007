a1 = [10.001, 11.591, 0.011, 5.991, 16.121, 0.131, 100.981, 1.001]
a2 = [1.99, 1.99, 0.99, 1.99, 0.99, 1.99, 0.99, 0.99]
a3 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
a4 = [10.01, -12.22, 0.23, 19.20, -5.13, 3.12]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    total = 0.00
    for i in range(len(arr)):
        total=total+arr[i]
        i+=1
    # TODO add necessary code here for sum; every number must have two decimal places shown
    print("\nThe total is {:.2f}:\n".format(total))
    print("UCID- as4283, Date - 09/24/2022, Explaination- I have used for loop for printing the total of the list of values")


print("Problem 2")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)