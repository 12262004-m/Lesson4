from sys import argv
a, hourly_production, hourly_rate, award = argv
print("Заработная плата сотрудника равна: ",(int(hourly_production)*int(hourly_rate))+int(award))