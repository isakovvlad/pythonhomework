
+разновидность абстрактного типа данных в ООП
__init__
self.count
FormulaCar ( ) pass
Git, Mercurial, CVS
git commit -m "Fixed logical error"
... создания ветки с именем velocity ... создания новой ветки с именем velocity (и что-то там ещё)

1.
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def width(self):
        return self.w
        
    def height(self):
        return self.h
        
    def area(self):
        return float(self.w * self.h)
        
    def perimeter(self):
        return float((2 * self.w) + (self.h * 2))
        
a, b = map(int, input().split())
d = Rectangle(a, b)
print(d.area(), d.perimeter())

2.
class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def read(self, input_string):
        a, b = map(int, input_string.split('/'))
        self.numerator = a
        self.denominator = b
        return 0
        
    def equal(self, other):
        return self.numerator * other.denominator == other.numerator * self.denominator

input1 = input().strip()
input2 = input().strip()
frac1 = Fraction()
frac2 = Fraction()
result1 = frac1.read(input1)
result2 = frac2.read(input2)
if frac1.equal(frac2):
    print("YES")
else:
    print("NO")


mkdir kr_git_1
cd kr_git_1
git init
echo -e "Курс \"Промышленное программирование\", контрольная работа.\n27.10.2024\nАвтор работы: Исаков Владислав" > README.txt
git add README.txt
git commit -m "Добавлен файл README.txt"
git checkout -b solution_A
echo -e "# Программа для работы с геометрическими фигурамиnn# Ваш код здесь" > geom.py
git add geom.py
git commit -m "Добавлен файл с решением задачи 'Геометрические фигуры (python)'"
git checkout master
git checkout -b solution_B
echo -e "# Программа для проверки равенства дробейnn# Ваш код здесь" > fract.py
git add fract.py
git commit -m "Добавлен файл с решением задачи 'Дроби: равенство'"
git checkout solution_A
git checkout -b result_AB
git merge solution_B
   echo -e "def run_geom():\n    print('Запуск программы для геометрических фигур')\n\n\ndef run_fract():\n    print('Запуск программы для проверки равенства дробей')nnndef main():\n    print('1. Геометрические фигуры')\n    print('2. Дроби: равенство')\n    choice = input('Введите номер программы (1 или 2): ')\n    if choice == '1':\n        run_geom()\n    elif choice == '2':\n        run_fract()\n    else:\n        print('Неверный выбор')\n\nif __name__ == '__main__':\n    main()" > menu.py
git add menu.py
git commit -m "Добавлено меню для запуска программ"
_____
git checkout solution_A
   геома
   def calculate_area(shape):
       if shape == "circle":
           area = 3.14 * (radius ** 2)
       return area
   shape = input("Введите фигуру: ")
   area = calculate_area(shape)
   output_to_file = input("Выводить результат в файл? (Y/N): ").strip().upper()
   if output_to_file == 'Y':
       with open("output.txt", "w") as f:
           f.write(f"Площадь {shape}: {area}n")
   else:
       print(f"Площадь {shape}: {area}")
git add geom.py
git commit -m "Изменен код решения задачи 'Геометрические фигуры' для вывода в файл"
git checkout solution_B
   дроби
   def check_fraction_equal(numerator1, denominator1, numerator2, denominator2):
       return (numerator1 * denominator2) == (numerator2 * denominator1)
   numerator1 = int(input("Введите числитель первой дроби: "))
   denominator1 = int(input("Введите знаменатель первой дроби: "))
   numerator2 = int(input("Введите числитель второй дроби: "))
   denominator2 = int(input("Введите знаменатель второй дроби: "))
   is_equal = check_fraction_equal(numerator1, denominator1, numerator2, denominator2)
   output_to_file = input("Выводить результат в файл? (Y/N): ").strip().upper()
   if output_to_file == 'Y':
       with open("output.txt", "w") as f:
           f.write(f"Дроби равны: {is_equal}n")
   else:
       print(f"Дроби равны: {is_equal}")
git add fract.py
git commit -m "Изменен код решения задачи 'Дроби: равенство' для вывода в файл"
git checkout result_AB
git merge solution_A
git merge solution_B
   def main():
       write_to_file = input("Do you want to write answer to file? (Y/N): ").strip().upper()
       
       if write_to_file == 'Y':
           output_file = open("output.txt", "w")
           output_func = lambda msg: output_file.write(msg + "n")
       else:
           output_func = print

       output_func("1. Геометрические фигуры")
       output_func("2. Дроби: равенство")
       choice = input("Введите номер программы (1 или 2): ")
       
       if choice == '1':
           run_geom(output_func)
       elif choice == '2':
           run_fract(output_func)
       else:
           output_func('Неверный выбор')

       if write_to_file == 'Y':
           output_file.close()

   def run_geom(output_func):

   def run_fract(output_func):

git add menu.py
git commit -m "Добавлен выбор вывода результата в файл или на экран"
git checkout master
git merge result_AB
