from prettytable import PrettyTable

table = PrettyTable()

table.align = "l"
print(table.align)

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
#table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water" , "Fire"])
#table.add_column("Score", ["9", "4", "6"])

print(table)