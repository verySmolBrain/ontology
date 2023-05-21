import bpy
import addon_utils
import os


'''
1. Generate images from .obj files
2. Detect the object in each image (Exploded view)
3. Classify each image as either a fastener or a non-fastener
'''

def main():
    # print(bpy.path.abspath("//"))
    cad_file = bpy.ops.wm.open_mainfile(filepath = "resources/gripper.blend")
    print(cad_file)
    
    for collection in bpy.data.collections:
        print(collection.name)
        for obj in collection.all_objects:
            print("obj: ", obj.name)
    
    print("AAAA")
    print("BBBBB")

if __name__ == "__main__":
    print("------------ Ignore the above error message ------------")
    
    main()