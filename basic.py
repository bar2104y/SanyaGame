"""
17/09/21
SanyaGame
"""
import math, random

class SanyaGameError(Exception):
    pass

class NegativeNumber(SanyaGameError):
    def __init__ (self, num):
        self.num = num
        self.message = 'Число должно быть неотрицательным трехзначным'
        super.__init__(self.message)

    def __str__(self):
        return f'{self.num} : {self.message}'

class Digit():
    def __init__(self, val,pos):
        self.val = val
        self.pos = pos
    
    def __repr__(self):
        #return {'Number':self.val, 'Position': self.pos}
        return f'Number {self.val} on position {self.pos}'

    def __str__(self):
        return f'Number {self.val} on position {self.pos}'


class Number:
    def __init__ (self, number):
        self.number = number
        self.length = self.get_length( self.number )
        self.num_list = self.to_arr( self.number )

    def get_length(self, num):
        return int(math.log10(num))+1
        #return len(str(num))

    def valide_number(self, number):
        is_valide = True

        # Проверка на минимальность
        if number < 100:
            is_valide = False
            #raise NegativeNumber(number)

        return is_valide

    def to_arr(self, num):
        res = []
        
        tmp = num
        length = self.get_length(tmp)

        for i in range(length):
            digit = tmp % 10
            d = Digit(digit, length-i)
            tmp = int(tmp/10)
            
            res.append(d)
        
        return res

    def print_stat(self):
        #As arr: {self.num_list}
        print(f'Number is {self.number} \nLength is {self.length}\nAs arr: {self.num_list} ')

    def check(self, second_num):
        a=0
        b=0
        for i in self.num_list:
            for j in second_num.num_list:
                if i.val == j.val:
                    a+=1
                    if i.pos == j.pos:
                        b+=1
        if a==self.length and b==self.length:
            return 'True'
        else:
            return str(a)+str(b)

def main():
    print('Начало игры:')
    l = int(input('Сколько знаков угадываем? '))
    win = False
    a = Number(random.randint(10**(l-1), 10**l-1))
    print(10**(l-1), 10**l-1)
    # a.print_stat()

    while not win:
        b = Number(int(input('Ваше предположение: ')))
        res = a.check(b)
       
        if res == 'True':
            print('Победа')
            win = True
        else:
             print('Мой ответ: ', res)
        
    

if __name__ == "__main__":
    main()