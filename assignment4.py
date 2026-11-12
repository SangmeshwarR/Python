components = ["Resistor", "Capacitor", "Inductor", "Diode"]

print("Electronic Components:")

for index, component in enumerate(components):
    print(f"Index {index} : {component}")

print("\n Accessing components by index:")

for i in range(len(components)):
    print("Component at index " + str(i) + ": " + str(components[i]))

new_component = "LED"

new_length = len(components) + 1

new_array = [None] * new_length

for i in range(len(components)):
    new_array[i] = components[i]

new_array[-1] = new_component

components = new_array

print("\nUpdated list of components:")

for index, component in enumerate(components):
    print("Index", index, component)