from flask import *
from database import *

def estimate_charging_time(current_battery_level, desired_battery_level, charging_power):
    """
    Estimate the EV charging time based on current battery level, desired battery level, and charging power.
    Args:
        current_battery_level (float): Current battery level in percent.
        desired_battery_level (float): Desired battery level in percent.
        charging_power (float): Charging power in kW.
    Returns:
        float: Estimated charging time in hours.
    """
    # Battery capacity in kWh.
    # battery_capacity = 60.0

    q="select * from recharge_center where center_id='%s'"%(session['bunk_id']) #Changes HERE
    res=select(q)
    print(res)
    battery_capacity=res[0]['power']

    # Calculate the amount of energy needed to charge the battery.
    energy_needed = (desired_battery_level - current_battery_level) / 100.0 * battery_capacity

    # Calculate the charging time in hours.
    charging_time = energy_needed / charging_power

    return charging_time

# Get user input data.
current_battery_level = float(input("Enter the current battery level in percent: "))
desired_battery_level = float(input("Enter the desired battery level in percent: "))
charging_power = float(input("Enter the charging power in kW: "))

# Estimate the charging time.
charging_time = estimate_charging_time(current_battery_level, desired_battery_level, charging_power)

# Print the estimated charging time.
print(f"Estimated charging time: {charging_time:.2f} hours")
