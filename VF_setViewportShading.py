bl_info = {
	"name": "VF Set Viewport Shading",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 0, 1),
	"blender": (2, 80, 0),
	"location": "View3D > View",
	"description": "Sets viewport shading from the menu, allowing for keyboard shortcuts to specific modes",
	"warning": "inexperienced developer, use at your own risk",
	"wiki_url": "",
	"tracker_url": "",
	"category": "3D View"}

import bpy
from bpy.types import Operator

# Helpful resources:
# https://blender.stackexchange.com/questions/137844/changing-the-shading-type-in-python
# https://blender.stackexchange.com/questions/124347/how-can-i-switch-the-shading-mode-between-wireframe-and-solid-mode
# https://blender.stackexchange.com/questions/201367/how-assign-shortcut-to-custom-function

###########################################################################
# Main class

class VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading(Operator): ## stuff to be able to make a menu item
	bl_idname = "object.my_class"
	bl_label = "Test"
	bl_description = "My Description"
	bl_space_type = "VIEW_3D"
	bl_region_type = 'UI'
	
	rendertype: bpy.props.StringProperty()
	
	def invoke(self, context, event):
		context.area.spaces[0].shading.type = self.rendertype
#		context.space_data.shading.type = self.rendertype
		return {'FINISHED'}



###########################################################################
# Menu UI

def menu_func(self, context):
	op0 = self.layout.operator(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading.bl_idname, text = "Wireframe", icon = "SHADING_WIRE")
	op0.rendertype = "WIREFRAME"
	op1 = self.layout.operator(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading.bl_idname, text = "Solid", icon = "SHADING_SOLID")
	op1.rendertype = "SOLID"
	op2 = self.layout.operator(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading.bl_idname, text = "Preview", icon = "SHADING_TEXTURE")
	op2.rendertype = "MATERIAL"
	op3 = self.layout.operator(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading.bl_idname, text = "Rendered", icon = "SHADING_RENDERED")
	op3.rendertype = "RENDERED"



###########################################################################
# Addon Registration

def register():
	bpy.utils.register_class(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading)
	bpy.types.VIEW3D_MT_view.append(menu_func)

def unregister():
	bpy.utils.unregister_class(VFSETVIEWPORTSHADING_OT_Set_Viewport_Shading)
	bpy.types.VIEW3D_MT_view.remove(menu_func)

if __name__ == "__main__":
	register()