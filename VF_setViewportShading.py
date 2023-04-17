bl_info = {
	"name": "VF Set Viewport Shading",
	"author": "John Einselen - Vectorform LLC",
	"version": (0, 0, 2),
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
# https://blender.stackexchange.com/questions/200815/how-to-create-a-keyboard-shortcut-to-call-a-custom-menu-in-a-floating-window-wit

###########################################################################
# Main class

class VF_SET_SHADING_OT_set_viewport_shading(Operator):
	bl_idname = "view3d.vfviewportshading"
	bl_label = "Set Viewport Shading"
	bl_description = "Sets viewport shading mode"
	bl_space_type = "VIEW_3D"
	bl_region_type = 'UI'
	
	rendertype: bpy.props.StringProperty()
	
	def invoke(self, context, event):
		context.area.spaces[0].shading.type = self.rendertype
#		context.space_data.shading.type = self.rendertype
		return {'FINISHED'}



###########################################################################
# Menu UI

def vf_viewport_shading_menu(self, context):
	self.layout.separator()
	op0 = self.layout.operator(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, text = "Wireframe", icon = "SHADING_WIRE")
	op0.rendertype = "WIREFRAME"
	op1 = self.layout.operator(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, text = "Solid", icon = "SHADING_SOLID")
	op1.rendertype = "SOLID"
	op2 = self.layout.operator(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, text = "Preview", icon = "SHADING_TEXTURE")
	op2.rendertype = "MATERIAL"
	op3 = self.layout.operator(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, text = "Rendered", icon = "SHADING_RENDERED")
	op3.rendertype = "RENDERED"



###########################################################################
# Addon Registration

addon_keymaps = []

def register():
	bpy.utils.register_class(VF_SET_SHADING_OT_set_viewport_shading)
	bpy.types.VIEW3D_MT_view.append(vf_viewport_shading_menu)

	# Add keyboard shortcuts
	wm = bpy.context.window_manager
	kc = wm.keyconfigs.addon
	if kc:
		km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
#		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'NUMPAD_0', 'PRESS')
		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'F1', 'PRESS', alt=True)
		kmi.properties.rendertype = 'WIREFRAME'
		addon_keymaps.append((km, kmi))
	if kc:
		km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
#		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'NUMPAD_1', 'PRESS')
		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'F2', 'PRESS', alt=True)
		kmi.properties.rendertype = 'SOLID'
		addon_keymaps.append((km, kmi))
	if kc:
		km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
#		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'NUMPAD_2', 'PRESS')
		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'F3', 'PRESS', alt=True)
		kmi.properties.rendertype = 'MATERIAL'
		addon_keymaps.append((km, kmi))
	if kc:
		km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
#		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'NUMPAD_3', 'PRESS')
		kmi = km.keymap_items.new(VF_SET_SHADING_OT_set_viewport_shading.bl_idname, 'F4', 'PRESS', alt=True)
		kmi.properties.rendertype = 'RENDERED'
		addon_keymaps.append((km, kmi))

def unregister():
	bpy.utils.unregister_class(VF_SET_SHADING_OT_set_viewport_shading)
	bpy.types.VIEW3D_MT_view.remove(vf_viewport_shading_menu)
	
	# Remove keyboard shortcuts
	for km, kmi in addon_keymaps:
		km.keymap_items.remove(kmi)
	addon_keymaps.clear()

if __name__ == "__main__":
	register()