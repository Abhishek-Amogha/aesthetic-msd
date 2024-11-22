import re

def modify_xvg(input_file, output_file, series_names):
    # Read the content of the .xvg file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
    
    # Ensure the series names match the number of series (s0, s1, s2, etc.)
    assert len(series_names) <= 4, "Too many series for the xvg file (max 4 series)."
    
    # Prepare series name mappings for s0, s1, s2, s3
    series_name_mapping = {f"s{i}": series_names[i] if i < len(series_names) else None for i in range(4)}
    
    # Flags to track if a change has been applied for the specific cases
    modified_xaxis_tick_major = False
    modified_yaxis_tick_major = False
    modified_legend_box = False

    # Iterate through the lines and apply changes
    for i, line in enumerate(lines):
        # 1. Modify 'world' number3 by dividing by 1000
        if "world" in line:
            match = re.search(r'world (\d+), (\d+), (\d+), (\d+)', line)
            if match:
                if "stack" in line or "stacked" in line:
                    continue  # Skip this line and move to the next
                else:
                    num3 = int(match.group(3))
                    modified_num3 = num3 / 1000.0
                    line = line.replace(match.group(3), str(modified_num3))
                    num3 = round(modified_num3/5) * 5
                    line = line.replace(match.group(3), str(num3))
                    num4 = int(match.group(4))  # Extract number 4 (max y-axis)
                    num4 = round(num4/5) * 5
                    line = line.replace(match.group(4), str(num4))
        
        # 2. Modify xaxis bar linewidth
        if "@    xaxis  bar linewidth" in line:
            line = re.sub(r'linewidth \d+(\.\d+)?', 'linewidth 2.0', line)
        
        # 3. Modify xaxis label from "tau (ps)" to "tau (ns)"
        if '@    xaxis  label "tau (ps)"' in line:
            line = '@    xaxis  label "tau (ns)"\n'
        
        # 4. Modify xaxis label char size
        if '@    xaxis  label char size' in line:
            line = '@    xaxis  label char size 2.000000\n'
        
        # 5. Modify xaxis label font
        if '@    xaxis  label font' in line:
            line = '@    xaxis  label font 4\n'
        
        # 6. Modify xaxis tick major
        if '@    xaxis  tick major' in line and not modified_xaxis_tick_major:
            displacement_x = num3 / 5
            line = f'@    xaxis  tick major {displacement_x}\n'
            modified_xaxis_tick_major = True  # Set flag to true after applying the change

        # 7. Modify xaxis tick major linewidth
        if '@    xaxis  tick major linewidth' in line:
            line = '@    xaxis  tick major linewidth 2.0\n'
        
        # 8. Modify xaxis tick minor linewidth
        if '@    xaxis  tick minor linewidth' in line:
            line = '@    xaxis  tick minor linewidth 2.0\n'
        
        # 9. Modify xaxis ticklabel char size
        if '@    xaxis  ticklabel char size' in line:
            line = '@    xaxis  ticklabel char size 1.500000\n'
        
        # 10. Modify xaxis ticklabel font
        if '@    xaxis  ticklabel font' in line:
            line = '@    xaxis  ticklabel font 4\n'
        
        # 11. Modify yaxis bar linewidth
        if '@    yaxis  bar linewidth' in line:
            line = '@    yaxis  bar linewidth 2.0\n'
        
        # 12. Modify yaxis label char size
        if '@    yaxis  label char size' in line:
            line = '@    yaxis  label char size 2.000000\n'
        
        # 13. Modify yaxis label font
        if '@    yaxis  label font' in line:
            line = '@    yaxis  label font 4\n'
            
        if '@    yaxis  tick major' in line and not modified_yaxis_tick_major:
            displacement_y = num4 / 5
            line = f'@    yaxis  tick major {displacement_y}\n'
            modified_yaxis_tick_major = True  # Set flag to true after applying the change
        
        # 14. Modify yaxis tick major linewidth
        if '@    yaxis  tick major linewidth' in line:
            line = '@    yaxis  tick major linewidth 2.0\n'
        
        # 15. Modify yaxis tick minor linewidth
        if '@    yaxis  tick minor linewidth' in line:
            line = '@    yaxis  tick minor linewidth 2.0\n'
        
        # 16. Modify yaxis ticklabel char size
        if '@    yaxis  ticklabel char size' in line:
            line = '@    yaxis  ticklabel char size 1.500000\n'
        
        # 17. Modify yaxis ticklabel font
        if '@    yaxis  ticklabel font' in line:
            line = '@    yaxis  ticklabel font 4\n'
        
        # 18. Modify legend positions
        if '@    legend' in line and not modified_legend_box:
            line = '@    legend 0.189970392, 0.807216876\n'
            modified_legend_box = True  # Set flag to true after applying the change
        
        # Remove line with @    legend 0.15, 0.05
        if '@    legend 0.15, 0.05' in line:
            lines.pop(i)  # Remove this line
            continue  # Skip incrementing i to recheck the current position

        # 19. Modify legend font
        if '@    legend font' in line:
            line = '@    legend font 4\n'
        
        # 20. Modify legend char size
        if '@    legend char size' in line:
            line = '@    legend char size 1.260000\n'
        
        # 21. Modify s0 line linewidth
        if '@    s0 line linewidth' in line:
            line = '@    s0 line linewidth 2.0\n'
        
        # 23. Modify s1 line linewidth
        if '@    s1 line linewidth' in line:
            line = '@    s1 line linewidth 2.0\n'
        
        # 24. Modify s0 legend
        if '@    s0 legend' in line and series_name_mapping.get('s0'):
            line = f'@    s0 legend  "{series_name_mapping["s0"]}"\n'
        
        # 25. Modify s1 line linewidth again
        if '@    s1 line linewidth' in line:
            line = '@    s1 line linewidth 2.0\n'
        
        # 26. Modify s1 legend
        if '@    s1 legend' in line and series_name_mapping.get('s1'):
            line = f'@    s1 legend  "{series_name_mapping["s1"]}"\n'
        
        # 27. Modify s2 line linewidth
        if '@    s2 line linewidth' in line:
            line = '@    s2 line linewidth 2.0\n'
        
        # 28. Modify s2 legend
        if '@    s2 legend' in line and series_name_mapping.get('s2'):
            line = f'@    s2 legend  "{series_name_mapping["s2"]}"\n'
        
        # 29. Modify s3 line linewidth
        if '@    s3 line linewidth' in line:
            line = '@    s3 line linewidth 2.0\n'
        
        # 30. Modify s3 legend
        if '@    s3 legend' in line and series_name_mapping.get('s3'):
            line = f'@    s3 legend  "{series_name_mapping["s3"]}"\n'
        
        # Stop processing when '@target' is encountered
        if line.startswith('@target'):
            break
        
        # Write the modified line back to the list
        lines[i] = line
    
    # Save the modified content to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines)

def process_xy_values(input_file, output_file):
    # Read the content of the .xvg file
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Flag to indicate if '@type xy' is found
    found_type_xy = False

    # Iterate through the lines and apply the transformation to x-values
    for i in range(len(lines)):
        line = lines[i]

        # Check for the '@type xy' line
        if '@type xy' in line:
            found_type_xy = True
            continue  # Skip processing this line itself

        # If '@type xy' is found, process the subsequent lines with two values
        if found_type_xy:
            parts = line.split()

            if len(parts) == 2:  # Ensure there are two values in the line
                try:
                    # Divide the x-value (first value) by 1000
                    x_value = float(parts[0]) / 1000.0
                    lines[i] = f"{x_value} {parts[1]}\n"  # Replace with modified x-value
                except ValueError:
                    pass  # In case there's a line with non-numeric values, we skip it.

    # Write the modified lines to the output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines)
    print(f"Changes applied and saved to {output_file}")



# Example usage:
if __name__ == "__main__":
    # Ask user for the series names
    series_names = input("Enter the series names (separated by space): ").split()

    # Ask the user for input and output file paths
    input_file = input("Enter the path to the input .xvg file: ")
    output_file = input("Enter the path to save the modified output .xvg file: ")

    # Call the function with the user-provided input/output file paths
    modify_xvg(input_file, output_file, series_names)

    # Then process the modified .xvg file to adjust x-values after '@type xy'
    process_xy_values(output_file, output_file)

