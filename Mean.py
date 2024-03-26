import matplotlib.pyplot as plt

#Data
x = [23, 21, 18, 16, 15, 13, 12, 10, 9, 7, 6, 5,2]
y = sorted(x)
a = len(x)
sumd = 0
for num in x:
    sumd+=num
    
meand = sumd/a
print(y)
print(a)
print('Mean of data is: ', meand)

# Plot the sorted data
plt.figure(figsize=(8, 6))
plt.plot(y, marker='o', linestyle='-')
plt.axhline(y=meand, color='r', linestyle='--', label='Mean')
plt.title('Sorted Data with Mean')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(x, marker='o', linestyle='-')
plt.axhline(y=meand, color='r', linestyle='--', label='Mean')
plt.title('Unsorted Data with Mean')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

