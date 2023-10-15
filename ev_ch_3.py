def estimate_charging_time(current_battery_level, desired_battery_level,battery_capacity):
    """
    Estimate the EV charging time based on current battery level, desired battery level, and charging power.
    Args:
        current_battery_level (float): Current battery level in percent.
        desired_battery_level (float): Desired battery level in percent.
        charging_power (float): Charging power in kW.
    Returns:
        float: Estimated charging time in hours.
    """
    data={}
    # Battery capacity in kWh.
    # battery_capacity = 60.0

    # charging power in kW.
    charging_power = 50

    # Calculate the amount of energy needed to charge the battery.
    energy_needed = (desired_battery_level - current_battery_level) / 100.0 * battery_capacity

    # Calculate the charging time in hours.
    data['charging_time'] = charging_time = energy_needed / charging_power
    data['energy_consumed'] = charging_time * charging_power
    print(data['energy_consumed'])

    return data

# # Get user input data.
# current_battery_level = float(input("Enter the current battery level in percent: "))
# desired_battery_level = float(input("Enter the desired battery level in percent: "))
# # charging_power = float(input("Enter the charging power in kW: "))

# # Estimate the charging time.
# charging_time = estimate_charging_time(current_battery_level, desired_battery_level)

# # Calculate the total energy consumed in kWh.
# # energy_consumed = charging_time * charging_power

# # Print the estimated charging time and total energy consumed.
# print(f"Estimated charging time: {charging_time:.2f} hours")
# # print(f"Total energy consumed: {energy_consumed:.2f} kWh")
