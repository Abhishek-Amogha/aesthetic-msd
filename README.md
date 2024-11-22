# Aestheticise MSD Graphs

This project provides a Python script to aestheticize and modify `.xvg` files generated by molecular simulation software (such as GROMACS). The goal is to enhance the visual presentation of MSD (Mean Squared Displacement) graphs by making adjustments to the graph formatting and labels. This includes changing axis labels, tick marks, line thickness, and adding custom legends.

## Features

- **Modify Axis Labels and Ticks**: Customize x-axis and y-axis labels and their properties (e.g., label font size, tick size, etc.).
- **Change Line Styles**: Adjust line widths and modify the legend.
- **Adjust Data Scaling**: Divide data values by 1000 and present in ns, instead of ps, for easier interpretation.
- **Legend Customization**: Automatically update legend texts based on user input for up to 4 series.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Grace (for generating plots)

Additionally, the Python script relies on the following built-in library:

- `re` (regular expressions)

## Setup

### Clone the Repository

Clone the repository to your local machine using Git:

    git clone https://github.com/yourusername/aesthetic-msd.git
    cd aesthetic-msd'

1.1 Compile the graphs you want to Aesthetise

    xmgrace A_msd.xvg B_msd.xvg C_msd.xvg

Click on *Save As* and save the file with a new name (eg: DEMO.xvg)

The script will prompt you to:

    Enter series names (up to 4, e.g., A B C).
    Enter the input file path of your .xvg file. (e.g., DEMO.xvg)
    Enter the output file path to save the modified .xvg file. (e.g., AestheticDEMO.xvg)

#### 1.2 Process the .xvg Values

The script processes the data by dividing the x-values by 1000 (for time scaling from ps to ns). This is especially useful if the data is in picoseconds (ps) and you wish to convert it to nanoseconds (ns).

### Step 2: Plot the Graph Using Grace

Once the .xvg file is modified, you can use Grace to plot it and generate a high-quality image.

#### 2.1 Running the Grace Plotting Command

You can use the following bash function (MSD_divideAesthetise) to automate the entire process:
    
    MSD_divideAesthetise() {
    # Define the source path for the Python file
    SOURCE_PATH=~/Desktop/Project/AestheticCompileMSD.py

    # Copy the AestheticCompileMSD.py file to the current directory (optional)
    cp "$SOURCE_PATH" .

    # Run the Python file
    python3 AestheticCompileMSD.py

    # Prompt the user for input and output file names
    echo "Enter input file name:"
    read input_file
    echo "Enter output file name:"
    read output_file

    # Execute the grace command to generate the plot
    grace -nxy "$input_file" -hardcopy -hdevice PNG -fixed 6000 6000 -printfile "${output_file}.png"

    # Delete the AestheticCompileMSD.py file after usage
    rm AestheticCompileMSD.py
    }

This function automates the following:

-    Copies the Python script to the current directory.
-    Runs the Python script to modify the .xvg file.
-    Prompts for input and output file names.
-    Generates a PNG plot using Grace.
-    Deletes the Python script after use.

Example Usage of the Function:

      MSD_divideAesthetise

**This will automatically execute all steps: modifying the .xvg file and generating the plot as a PNG file.**

#### Step 3: Output

The output will be a .png file containing the updated plot, with all aesthetic changes applied. You can further adjust the output by tweaking the script's settings or the Grace parameters.

## Customization

You can further customize the script to fit your needs, such as adjusting the font sizes, modifying the color schemes, or setting different axis limits.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests with enhancements or bug fixes.
