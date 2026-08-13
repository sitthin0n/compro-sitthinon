animal_dog = ["dog", "cat", "rabbit", "hamster"]
first_dog_index = animal_dog.index("dog")
print(f"The index of 'dog' is: {first_dog_index}")
second_dog_index = animal_dog.index("dog", first_dog_index + 1)
print(f"The index of the second 'dog' is: {second_dog_index}")