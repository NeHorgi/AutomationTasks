class CardDeck:

    def __init__(self):
        self.Deck = 52
        self.card = 0
        self.colors = ['Пик', 'Черви', 'Буби', 'Крести']
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']

    def __next__(self):

        for color in self.colors:
            for card in self.cards:
                if self.card < self.Deck:
                    self.card += 1
                    print(f'{card} {color}')

        print(f'Колода закончилась')
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    deck = CardDeck()
    for cart in deck:
        print(cart)


