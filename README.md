## Project Descriptions

This project is a collection of scripts that aims to automate the training of an Image Classification model for the purpose of classifying each CAD component as either a fastener or part. The scripts are written in Python and use the Blender API to generate images of CAD components in various orientations and lighting conditions. The images are then stored as training data for an Image Classification model developed through Transfer Learning and based off the ResNet50 model. 

The project is a small part of a larger project that aims to automate the development of a disassembly ontology through CAD files.

## Project Structure

### create_parts_graph (wip)

This part hasn't been completed yet. The idea for this module / script is to take in a list of components in a CAD assembly which have been identified as either a fastener or a part and then generate a graph of the assembly with each component as a node. This can then be used to generate a disassembly sequencem that can be fed into a disassembly ontology alongside part metadata.

### disassemble_model

This script takes in a CAD assembly and outputs each individual component as a separate file. This can be specified as either a fastener or a component which is then saved in the respective folder under `resources/models/`. This design decision is because we want to create a good sample of different
fasteners and parts. Simply generating images would reduce the flexibility of being able to combine different parts or test the model with specific
parts.

For future development, it may also be nice to have functionality to create a `component.json` file which contains metadata on each component which can then be used to develop the ontoloy further.

### generate_classification_model (wip)

This script takes in a folder of images and trains an Image Classification model based off ResNet50. Note that this model isn't currently finished.

Note that currently we don't have enough training data to develop a good model.

### generate_images

This script takes in a folder of CAD components and generates images of each component in various orientations and lighting conditions. The images are then saved in the `resources/dataset/train` folder.

### identify_images (wip)

This script takes in a folder of images and identifies each image as either a fastener or a component. This uses our Image Classification model to identify each image.

Note that currently we don't have enough training data to create a good model so as a subtitute this is just a script that uses the Yolov8 model to identify each image. This is just a placeholder until we have enough training data to develop the first iteration of the ResNet50 model.

### resources

This folder contains all the resources used by the scripts. This includes the CAD components, the Image Classification model, and the training data.

## Installation Requirements

This project relies on the Python module bpy which has the same requirements as Blender itself. We are also using `bpy 3.5` which runs on `Python 3.10`. To run on your own machine use this command:

```
pip install -r requirements.txt
python generate_images/generate.py
```

Note: If you want code autocomplete, you'll have to install a wrapper API such as `blender_autocomplete` or `fake_bpy_module`. This is because bpy uses Cython which obscures function calls. I would also recommend using some sort of environment manager such as `pipenv` or `conda` to manage your dependencies.