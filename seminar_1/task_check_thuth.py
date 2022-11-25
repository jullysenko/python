# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def check_thuth(x, y, z):
    print(not (x or y or z) == (not x and not y and not z))


check_thuth(False, False, False)
check_thuth(True, False, False)
check_thuth(False, True, False)
check_thuth(False, False, True)
check_thuth(True, True, False)
check_thuth(False, True, True)
check_thuth(True, False, True)
check_thuth(True, True, True)


# решение преподавателя 
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
