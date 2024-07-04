

cheap_ramp = float(input("Input number of cheap ramp and card draw cards in deck (usually cmc 1-2 spells)"))
avg_cmc = float(input("Average CMC of spells in your deck"))

SuggestedLandCount = 31.42 + 3.13*(avg_cmc) - 0.28*(cheap_ramp)

print(f"Total suggested land count is {round(SuggestedLandCount,3)} lands")