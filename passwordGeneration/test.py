import random
import matplotlib.pyplot as plt

amt = 50
amt_history = [amt]

hit = False
while not hit:
    rand = random.choice([0.33,0.5,0.5, 0.5, 0.5, 0.5,0.5,1, 1, 1,1.5, 1.5, 2, 2, 2,2,5]) 
    amt *= rand
    amt_history.append(amt)

    print(f"Round Number: {len(amt_history)}. Current amt = {amt_history[-1]}")
    if amt >= 100000:
        print(f"Game won in {len(amt_history)} rounds")
        hit = True
    if amt ==0:
        print("Failure")
        break

plt.plot(range(len(amt_history)), amt_history)
plt.xlabel('Number of Rounds')
plt.ylabel('Amount')
plt.title('Amount over Time')
plt.grid(True)
plt.show()