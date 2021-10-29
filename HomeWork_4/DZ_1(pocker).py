class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Hand:
    def __init__(self):
        self.a = []

    def add(self, card):
        if len(self.a) < 5:
            self.a.append(card)

    def _get_sort(self, k):
        m = []
        for c in self.a:
            if k == 'suit':
                m.append(c.suit)
            if k == 'value':
                c.value = 0 if c.value == 'A' else c.value
                c.value = 13 if c.value == 'K' else c.value
                c.value = 12 if c.value == 'Q' else c.value
                c.value = 11 if c.value == 'J' else c.value
                m.append(int(c.value))
        return sorted(m)

    def check_comb(self):
        suits = sorted(self._get_sort('suit'))
        values = sorted(self._get_sort('value'))
        Min = min(values)

        if len(self.a) == 5:
            if len(set(suits)) == 1 and values == [0, 10, 11, 12, 13]:
                return 'Royal Flush'
            if len(set(suits)) == 1 and sorted(values) == [Min, Min + 1, Min + 2, Min + 3, Min + 4]:
                return 'Straight Flush'
            if len(set(values)) <= 2 and (values[0] == values[1] and values[3] == values[4]):
                return 'Full House'
            if len(set(suits)) == 1:
                return 'Flush'
            if sorted(values) == [Min, Min + 1, Min + 2, Min + 3, Min + 4]:
                return 'Straight'

        if len(self.a) >= 4:
            if values.count(values[1]) == 2 and values.count(values[3]) == 2:
                return 'Two Pair'

        for c in values:
            if values.count(c) == 4:
                return '4 of a Kind'
            if values.count(c) == 3:
                return '3 of a Kind '
            if values.count(c) == 2:
                return 'Pair'

        if len(self.a) >= 1:
            return 'High Card'


My_hand = Hand()

Heart_A = Card('C', 'A')
My_hand.add(Heart_A)
My_hand.add(Card('C', 'J'))
My_hand.add(Card('C', 'Q'))
My_hand.add(Card('C', 'K'))
My_hand.add(Card('C', '10'))
print(My_hand.check_comb())

#INFO:

#COMBINATIONS
#Hight Card - Старшая Карта (Любая старшая карта)
#Pair - Пара (Две карты одного ранга)
#Two Pair - Две пары (Две карты одного ранга и две карты другого ранга)
#3 of a Kind - Тройка/Сет (Три карты одного ранга)
#Straight - Стрит (Пять последовательных карт)
#Flush - Флеш (Пять карт одной масти)
#Full House - Фулл Хаус (Три карты одного ранга и две карты другого ранга)
#4 of a Kind - Каре (Любые четыре карты одного ранга и две карты другого ранга)
#Straight Flush - Стрит Флеш (Пять любых последовательных карт одной масти)
#Royal Flush - Рояль Флеш (Пять карт от 10 до Туза)

#SUITS
#Clubs(C) - Крести
#Hearts(H) - Черви
#Diaomond(D) - Бубны
#Spades(S) - Пики

#PLAYING CARD
#2 -> 10, J, Q, K, A