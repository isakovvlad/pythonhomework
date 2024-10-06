1.
class Swordsman(Warrior):
    def __init__(self, hp=100, attack=10, armor=0):
        super().__init__(hp, attack)
        self.armor = armor

2.
class Swordsman(Warrior):
    def __init__(self, hp=100, armor=0):
        super().__init__(hp, attack=10)
        self.armor = armor

    def get_damage(self, damage):
        if self.armor > 0:
            damage_hp = damage // self.armor
        else:
            damage_hp = damage
        self.hp -= damage_hp

    def __str__(self):
        return f"Мечник: HP = {self.hp}"

3.
class Archer(Warrior):
    def __init__(self, hp=100, attack=10):
        super().__init__(hp, attack)
        
    def reload(self):
        print("Лучник заряжает лук...")
        print("Лучник зарядил лук")

    def __str__(self):
        return f"Лучник: HP = {self.hp}"

4.
class Archer(Warrior):
    def __init__(self, hp=100, attack=10):
        super().__init__(hp, attack)
        
    def reload(self):
        print("Лучник заряжает лук...")
        print("Лучник зарядил лук")

    def do_attack(self, other):
        self.reload()
        super().do_attack(other)

    def __str__(self):
        return f"Лучник: HP = {self.hp}"

5.
def main():
    hp_arc = int(input())
    player1 = Archer(hp=hp_arc)
    hp_swor, armor_swor = map(int, input().split())
    player2 = Swordsman(hp=hp_swor, armor=armor_swor)
    print(player1, "VS", player2)
    while player1.is_alive() and player2.is_alive():
        player1.do_attack(player2)
        if player2.is_alive():
            player2.do_attack(player1)
        if player1.hp != 0 and player2.hp != 0:
            print(player1, "VS", player2)
    if player1.is_alive():
        print(f"Победил {player1}")
    else:
        print(f"Победил {player2}")

if __name__ == "__main__":
    main()

6.
def main(input_file='input.txt', output_file='output.txt'):
    with open(input_file, 'r') as infile:
        n = int(infile.readline().strip())
        arr = list(map(int, infile.readline().strip().split()))
    non_negative = [x for x in arr if x >= 0]
    negative = [x for x in arr if x < 0]
    result = non_negative + negative
    with open(output_file, 'w') as outfile:
        outfile.write(' '.join(map(str, result)) + '\n')
        
if __name__ == "__main__":        
    main()

7.
def main(input_file='input.txt', output_file='output.txt'):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
    total_lines = len(lines)
    total_chars = sum(len(line.rstrip('\n')) for line in lines)
    third_line = lines[2].rstrip('\n') if total_lines >= 3 else '0'
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f"{total_lines}\n")
        outfile.write(f"{total_chars}\n")
        outfile.write(third_line + '\n')
        
if __name__ == "__main__":        
    main()
