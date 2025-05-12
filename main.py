from src.dealer import Deal, FilterCard

if __name__ == '__main__':
    draws = 3
    target_card = FilterCard(suit='Diamond')
    instance = Deal()
    instance.shuffle()
    instance.draw(draws=draws)
    my_hand = instance.hand
    probability = instance.next_card_prob(target_card=target_card)

    print(f"My hand has: {my_hand}")
    print(f"The probability of drawing {target_card} is: {probability}")