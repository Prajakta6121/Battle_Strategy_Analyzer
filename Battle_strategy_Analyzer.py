# Battle Strategy Analyzer

# 1. Data Collection
units=[]
print(" Battle Strategy Analyzer")
n = int(input("Enter number of army units: "))

for i in range(n):
    print(f"\nEnter details for unit {i+1}:")
    name = input("Unit Name: ")
    missions = int(input("Missions completed: "))
    injured = int(input("Soldiers injured: "))
    enemies = int(input("Enemies neutralized: "))
    units.append((name, missions, injured, enemies))

# 2. Display All Unit Details
print("\n📊 Unit Report:")
print("| {:<8} | {:<9} | {:<7} | {:<20} |".format("Unit", "Missions", "Injured", "Enemies Neutralized"))
print("|" + "-"*8 + "|" + "-"*11 + "|" + "-"*9 + "|" + "-"*22 + "|")
for u in units:
    print("| {:<8} | {:<9} | {:<7} | {:<20} |".format(u[0], u[1], u[2], u[3]))

# 3. Identify Top Performing Unit
top_unit = units[0]
for u in units[1:]:
    if u[3] > top_unit[3]:
        top_unit = u
    elif u[3] == top_unit[3] and u[2] < top_unit[2]:
        top_unit = u

print(f"\n🏆 Top Performing Unit: {top_unit[0]} (Enemies: {top_unit[3]}, Injured: {top_unit[2]})")

# 4. Classify Unit Readiness
readiness_dict = {}
print("\n📋 Unit Readiness Status:")
for u in units:
    name, missions, injured, enemies = u
    if missions >= 10 and injured < 5:
        status = "Excellent"
    elif missions >= 8 and injured < 8:
        status = "Good"
    elif injured >= 8 or missions < 5:
        status = "Needs Rest"
    else:
        status = "Average"
    readiness_dict[name] = status
    print(f"{name}: {status}")

# 5. Casualty Alert Report
print("\n🚨 Casualty Alert Report:")
alert_units = [u[0] for u in units if u[2] > 6]
if alert_units:
    for name in alert_units:
        print(f"- {name}")
else:
    print("All units are in healthy condition.")

# 🔄 6. Update Unit Data by Name
choice = input("\nDo you want to update a unit's data? (yes/no): ").lower()
if choice == 'yes':
    update_name = input("Enter the name of the unit to update: ").lower()
    found = False
    for i in range(len(units)):
        if units[i][0].lower() == update_name:
            print(f"\nCurrent data for {units[i][0]}:")
            print(f"Missions: {units[i][1]}, Injured: {units[i][2]}, Enemies: {units[i][3]}")
            
            # New input
            new_missions = int(input("Enter updated missions: "))
            new_injured = int(input("Enter updated injuries: "))
            new_enemies = int(input("Enter updated enemies neutralized: "))
            
            # Update the tuple
            units[i] = (units[i][0], new_missions, new_injured, new_enemies)
            print(f"✅ Data for unit '{units[i][0]}' updated successfully.")
            found = True
            break
    if not found:
        print("❌ Unit not found.")
else:
    print("No updates made.")

# 🧾 7. Generate Final Command Report
print("\n🪖 Final Command Report")
print("| {:<8} | {:<9} | {:<7} | {:<8} | {:<15} |".format("Unit", "Missions", "Injured", "Enemies", "Readiness"))
print("|" + "-"*8 + "|" + "-"*11 + "|" + "-"*9 + "|" + "-"*10 + "|" + "-"*17 + "|")

# Re-calculate readiness after update
for u in units:
    name, missions, injured, enemies = u
    if missions >= 10 and injured < 5:
        status = "Excellent"
    elif missions >= 8 and injured < 8:
        status = "Good"
    elif injured >= 8 or missions < 5:
        status = "Needs Rest"
    else:
        status = "Average"
    print("| {:<8} | {:<9} | {:<7} | {:<8} | {:<15} |".format(name, missions, injured, enemies, status))
Battle_strategy_Analyzer.py