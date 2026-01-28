capitals = {
    "Pakistan":"Karachi",
    "India":"Delhi",
    "China":"Shanghai",
    "Afghanistan":"Kabul",
    "Iran":"Tehran"
}

print(capitals.values())
print(capitals.keys())
print(capitals.items()) # Give key value pairs list in tuple form
capitals.update({"China":"Berlin","Russia":"Moscow"}) # Bcz dictionaires are mutable
print(capitals.values())
