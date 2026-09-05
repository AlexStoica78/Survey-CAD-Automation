import csv
from collections import defaultdict

input_file = "site_survey.txt"
output_file = "plot_points.scr"

print("Starting expert-level survey parsing with layers and linework...")

features = defaultdict(list)

# Define a color chart for our layers
# 1 = Red (Buildings), 5 = Blue (Fences), 3 = Green (Utilities/Manholes), 7 = White
layer_settings = {
    "BLDG_CORNER": {"layer": "SURVEY_BUILDINGS", "color": "1"},
    "FENCE_POST": {"layer": "SURVEY_FENCES", "color": "5"},
    "MANHOLE_CL": {"layer": "SURVEY_UTILITIES", "color": "3"},
    "KERB_LINE": {"layer": "SURVEY_ROADS", "color": "7"}
}

try:
    with open(input_file, mode='r') as txt_file, open(output_file, mode='w') as scr_file:
        reader = csv.DictReader(txt_file)

        scr_file.write("REGENAUTO ON\n")

        # Pre-create all specialized layers in AutoCAD automatically
        for key, info in layer_settings.items():
            scr_file.write(f"-LAYER _M {info['layer']} _C {info['color']} {info['layer']} \n")

        # Read and plot data
        for row in reader:
            east = row['Easting'].strip()
            north = row['Northing'].strip()
            desc = row['Description'].strip()

            features[desc].append(f"{east},{north}")

            # Find matching layer or default to standard Layer 0
            layer_name = layer_settings.get(desc, {"layer": "0"})["layer"]

            # Switch to correct layer before drawing the point and text
            scr_file.write(f"-LAYER _S {layer_name} \n")
            scr_file.write(f"_POINT {east},{north}\n")
            scr_file.write(f"_TEXT {east},{north} 0.5 0 {desc}\n")

        # Draw the connecting lines on their correct layers
        for desc, coords in features.items():
            if len(coords) >= 2:
                layer_name = layer_settings.get(desc, {"layer": "0"})["layer"]
                scr_file.write(f"-LAYER _S {layer_name} \n")
                scr_file.write("_PLINE\n")
                for coord in coords:
                    scr_file.write(f"{coord}\n")
                scr_file.write("\n")

        scr_file.write("_ZOOM _E\n")
        print("Success! Your layer-ready script is generated.")

except FileNotFoundError:
    print(f"Error: Could not find '{input_file}'.")
