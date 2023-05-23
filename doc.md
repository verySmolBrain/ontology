## Installation Requirements

This project relies on the Python module bpy which has the same requirements
as Blender itself. We are also using `bpy 3.5` which runs on `Python 3.10`.
To run on your own machine use this command:

```
pip install -r requirements.txt
python generate_images/generate.py
```

Note for VScode users: If you want code autocomplete, you'll have to install
a wrapper API such as `blender_autocomplete` or `fake_bpy_module`. This is
because bpy uses Cython which obscures function calls.