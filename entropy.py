import math

def entropy_cal(array):

    total_entropy = 0

    for i in array:

        total_entropy += -i*math.log(2, i)

    return total_entropy

def main():

    probabilities = [0.5, 0.5, 0.5, 0.5]
    entropy = entropy_cal(probabilities)

    print(entropy)

if __name__=="__main__":
    main()
