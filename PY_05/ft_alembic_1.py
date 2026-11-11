import alchemy


print("=== Alembic 1 ===\n"
      "Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")

print("Now show that not all functions can be reached\n"
      "This will raise an exception!\n"
      f"Testing the hidden create_earth: {alchemy.create_earth()}")
