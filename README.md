## Project Descriptions

This project is a collection of scripts that generate images for the ontology project. The images are generated using Blender and the Python API `bpy`. The scripts take in a `.stl` file or `.blend` file and creates
a set of images from different angles. These can be classified as either a fastener or a part. 

The images are then stored as training data for a Computer Vision model
based on the YOLOv8 architecture that aims to classify CAD models as
either a fastener or a part.

## Installation Requirements

This project relies on the Python module bpy which has the same requirements as Blender itself. We are also using `bpy 3.5` which runs on `Python 3.10`. To run on your own machine use this command:

```
pip install -r requirements.txt
python generate_images/generate.py
```

Note: If you want code autocomplete, you'll have to install a wrapper API such as `blender_autocomplete` or `fake_bpy_module`. This is because bpy uses Cython which obscures function calls.