import timeit

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

text1 = read_file('article_01.txt')
text2 = read_file('article_02.txt')

#Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256  
    q = 101 
    n = len(text)
    m = len(pattern)
    hpattern = 0 
    htext = 0     
    h = 1

  
    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        hpattern = (d * hpattern + ord(pattern[i])) % q
        htext = (d * htext + ord(text[i])) % q

   
    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i+m] == pattern:
                return i 

        if i < n - m:
            htext = (d * (htext - ord(text[i]) * h) + ord(text[i + m])) % q
            if htext < 0:
                htext = htext + q

    return -1

#Алгоритм Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m  
    j = 0  

    #Побудова таблиці LPS
    compute_lps(pattern, m, lps)

    i = 0  
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j  
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def compute_lps(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

#Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = [-1] * 256  

    for i in range(m):
        bad_char[ord(pattern[i])] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            return s 
        else:
            s += max(1, j - bad_char[ord(text[s + j])])

    return -1

#Вимірювання часу виконання
def time_algorithm(algorithm, text, pattern):
    start_time = timeit.default_timer()
    result = algorithm(text, pattern)
    elapsed_time = timeit.default_timer() - start_time
    return elapsed_time, result

#Перевірка
text1 = read_file("article_01.txt")
text2 = read_file("article_02.txt")
pattern_exist = "приклад"  
pattern_fake = "вигаданий підрядок"  


algorithms = [rabin_karp, kmp_search, boyer_moore]
texts = [("Article 01", text1), ("Article 02", text2)]
patterns = [("Existing", pattern_exist), ("Fake", pattern_fake)]

#Виведення результатів
for algorithm in algorithms:
    print(f"\nАлгоритм: {algorithm.__name__}")
    for text_name, text in texts:
        for pattern_name, pattern in patterns:
            time_taken, result = time_algorithm(algorithm, text, pattern)
            status = "Знайдено" if result != -1 else "Не знайдено"
            print(f"{text_name} - {pattern_name}: {status}, Час виконання: {time_taken:.5f} секунд")
