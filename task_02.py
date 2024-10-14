def binary_search(arr, target):
    #Початкові значення для лівого (low) і правого (high) країв масиву
    low = 0
    high = len(arr) - 1
    
    iterations = 0
    
    #Верхня межа 
    upper_bound = None

  
    while low <= high:
        iterations += 1  
        
        mid = (low + high) // 2  

        #Якщо середній елемент рівний шуканому значенню, повертаємо його
        if arr[mid] == target:
            return (iterations, arr[mid])

        #Якщо середній елемент менший за шуканий
        if arr[mid] < target:
            low = mid + 1 
        else:
            upper_bound = arr[mid]  
            high = mid - 1  

    #Якщо не знайдено точного збігу, повертаємо кількість ітерацій та верхню межу
    return (iterations, upper_bound)

# Тестування функції
arr = [0.1, 1.2, 2.5, 3.3, 4.7, 5.8, 6.9, 7.5, 8.6]
target = 5.0

#Викликаємо функцію
result = binary_search(arr, target)

#Виводимо результат
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
