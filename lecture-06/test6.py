fruits_with_duplicates = ["apple", "banana", "cherry", "apple", "banana", "kivi"]
while "apple" in fruits_with_duplicates:
    fruits_with_duplicates.remove("apple")
print(f"The updated fruits are: {fruits_with_duplicates}")