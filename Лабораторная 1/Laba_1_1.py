numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_None=4
numbers[index_None]=(sum(numbers[:index_None]+numbers[index_None+1:]))/len(numbers)
print("Измененный список:", numbers)