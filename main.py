time_list = [
    ["day", 86400, 0],
    ["hour", 1440, 0],
    ["minute", 60, 0],
    ["second", 1, 0]
]

input_time = int(input("Please enter the number of seconds:"))
for time_value in time_list:
    time_value[2] = input_time // time_value[1]
    input_time = input_time - time_value[2] * time_value[1]
output_list = []
for time_value in time_list:
    if time_value[2] != 0:
        if time_value[2] > 1:
            output_list.append(f"{time_value[2]} {time_value[0]}s")
        else:
            output_list.append(f"{time_value[2]} {time_value[0]}")

print(", ".join(output_list).strip())
