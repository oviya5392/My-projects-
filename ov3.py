import time

print("Typing Speed Test!")
text = "Ovi is learning Python and having fun!"
print(f"Type this exactly: {text}")

input("Press Enter when ready...")

start = time.time()
typed = input("Start typing: ")
end = time.time()

time_taken = end - start
accuracy = sum(1 for a, b in zip(text, typed) if a == b) / len(text) * 100

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy:.2f}%")