def calculateBill(b,tp):
    
    total = b * (1+(0.01*tp))
    return total

bill = int(input("Enter the bill amount: "))
tipPerc = float(input("Ener the tip amount: "))

total = calculateBill(bill,tipPerc)

print(f"\n\nTotal bill with tip: {total}")
print(f"Total Tip: {total-bill}")