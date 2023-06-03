import bpy
import math
import os
import argparse

def read_file(filepath):
    bpy.ops.wm.open_mainfile(filepath = filepath)
    
def get_all_objects():
    return [o for o in bpy.context.scene.objects]

def get_all_mesh_objects():
    return [o for o in bpy.context.scene.objects if o.type == 'MESH']

def main():
    parser = argparse.ArgumentParser(description = "Disassemble .obj files")
    parser.add_argument("obj_file", help = "Path to the .obj file to generate images from")
    args = parser.parse_args()
    
    parsed = set()
    
    while parsed != set(get_all_mesh_objects()):
        read_file(args.obj_file)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        all_objects = get_all_objects()
        mesh_objects = get_all_mesh_objects()
        fastener_or_part = "FASTENER"
        
        for mesh_object in mesh_objects:
            if mesh_object.name in parsed:
                continue
            
            parsed.add(mesh_object.name)
            all_objects.remove(mesh_object)
            
            while True:
                fastener_or_part = input(f"Is part [ {mesh_object.name} ] a fastener or a part? (f/p): ")
                if fastener_or_part == "f" or fastener_or_part == "p":
                    break
                print("Invalid input!")
            break
        
        bpy.ops.object.delete({'selected_objects': all_objects})
        
        if fastener_or_part == 'f':
            num_files = len(os.listdir('resources/dataset/train/fastener'))
            bpy.ops.wm.save_as_mainfile(filepath = os.path.abspath(f"resources/dataset/train/fastener/{num_files}.blend"))
        elif fastener_or_part == 'p':
            num_files = len(os.listdir('resources/dataset/train/part'))
            bpy.ops.wm.save_as_mainfile(filepath = os.path.abspath(f"resources/dataset/train/part/{num_files}.blend"))
        
        read_file(args.obj_file)

if __name__ == "__main__":
    print("------------ Ignore the above error message ------------")
    
    main()