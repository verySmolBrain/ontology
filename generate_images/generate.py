import bpy
import math
import os
import argparse

'''
1. Generate images from .obj files
2. Detect the object in each image (Exploded view)
3. Classify each image as either a fastener or a non-fastener
'''

def read_file(filepath):
    bpy.ops.wm.open_mainfile(filepath = "resources/models/screw.blend")

def get_all_mesh_objects():
    return [o for o in bpy.context.scene.objects if o.type == 'MESH']
    
def rotate_and_render(output_dir, output_file_pattern_string = 'render%d.jpg', rotation_steps = 10, rotation_angle = 360.0, subject = bpy.context.object):
    cam_x_pos = max([v[0] for v in subject.bound_box]) * 5
    cam_y_pos = max([v[1] for v in subject.bound_box]) * 5
    cam_z_pos = max([v[2] for v in subject.bound_box]) * 5
    
    rot_centre = bpy.data.objects.new('rot_centre', None)
    bpy.context.collection.objects.link(rot_centre)
    rot_centre.location = subject.location
    
    camera = bpy.data.objects.new('camera', bpy.data.cameras.new('camera'))
    bpy.context.collection.objects.link(camera)
    camera.location = (cam_x_pos, cam_y_pos, cam_z_pos)
    camera.parent = rot_centre
    m = camera.constraints.new('TRACK_TO')
    m.target = subject
    m.track_axis = 'TRACK_NEGATIVE_Z'
    m.up_axis = 'UP_Y'
    bpy.context.scene.camera = camera
    
    light_data = bpy.data.lights.new(name = "light", type = 'POINT')
    light_data.energy = 100000
    
    light_object = bpy.data.objects.new(name = "light", object_data = light_data)
    bpy.context.collection.objects.link(light_object)
    bpy.context.view_layer.objects.active = light_object
    light_object.location = (cam_x_pos, cam_y_pos, cam_z_pos)
    
    dg = bpy.context.evaluated_depsgraph_get() 
    dg.update() 
    
    original_rotation = subject.rotation_euler
    for step in range(0, rotation_steps):
        subject.rotation_euler[2] = math.radians(step * (rotation_angle / rotation_steps))
        bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
        bpy.ops.render.render(write_still = True)
    subject.rotation_euler = original_rotation

def main():
    parser = argparse.ArgumentParser(description = "Generate images from .obj files")
    parser.add_argument("obj_file", help = "Path to the .obj file to generate images from")
    args = parser.parse_args()
    
    read_file(args.obj_file)
    for mesh_object in get_all_mesh_objects():
        rotate_and_render('resources/training_data', mesh_object.name + '_render_%d.jpg', 10, 360.0, mesh_object)

if __name__ == "__main__":
    print("------------ Ignore the above error message ------------")
    
    main()

