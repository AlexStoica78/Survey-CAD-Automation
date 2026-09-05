# Automated Georeferenced Topographical Survey Pipeline

An automation pipeline built to bridge geospatial field survey datasets directly with CAD production environments, removing manual data entry and drafting human error.

## Technical Capabilities
* **Data Ingestion:** Systematically parses multi-column Total Station ASCII data files (`.txt`/`.csv`).
* **Spatial Structuring:** Automatically maps coordinates to the British National Grid (OSGB36) system.
* **Auto-Linework Logic:** Uses a custom Python data parser to sort matching survey features (`BLDG_CORNER`, `FENCE_POST`) into contiguous Polylines (`_PLINE`).
* **Auto-Layering Management:** Dynamically instantiates and configures layer parameters (Layer Name, Index Color Assignment) inside AutoCAD seamlessly via code.

## The Workflow
1. **Field Telemetry:** The script reads raw coordinates (`Easting`, `Northing`, `Elevation`, `Description`).
2. **Translation Engine:** Python compiles thousands of precise tracking vectors into an AutoCAD Command Script file (`.scr`).
3. **Execution Canvas:** Running the script in AutoCAD automatically formats layers, draws geometries, configures node types (`PTYPE`), and centers views natively.
