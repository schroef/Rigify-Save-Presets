import bpy
import os
import re
from .utils import write_metarig
from bpy.types import Operator, Menu
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bl_operators.presets import AddPresetBase


class RIGIFY_MT_SettingsPresetMenu(Menu):
    #bl_idname = "rigify.setting_preset_menu"
    bl_label = "Rigify Settings Presets"
    preset_subdir = "rigify/settings_presets"
    preset_operator = "script.execute_preset"
    draw = Menu.draw_preset

def ReturnBoneGroupsColorSets(context):
    '''Return Bone groups with color sets'''
    bl_idname = "rigify.return_bone_color_sets"
    bl_label = "Return Bone Groups + Color Set"

    #def execute(self, context):
    obj = context.object
    armature = obj.data
    colorSet = []
    print("### Rigify color index: %s" % armature.rigify_colors_index)
    for g in armature.rigify_colors:
        colorSet.append((g))
        print("### Rigify color index: %s" % g)

    return colorSet



class RIGIFY_OT_AddSettingsPreset(AddPresetBase, Operator):
    '''Add or remove Rigify settings preset'''
    bl_idname = "rigify.add_settings_presets"
    bl_label = "Save Rigify Settings as preset"
    preset_menu = "RIGIFY_MT_SettingsPresetMenu"

    #items = ReturnBoneGroupsColorSets()
    # variable used for all preset values
    preset_defines = [
        "obj = bpy.context.object",
        "armature = obj.data"
        ]

    #preset_values = [""]
    preset_values = [
        "armature.rigify_colors[0].name",
        "armature.rigify_colors[0].normal",
        "armature.rigify_colors[0].select",
        "armature.rigify_colors[0].active",
        "armature.rigify_colors[1].name",
        "armature.rigify_colors[1].normal",
        "armature.rigify_colors[1].select",
        "armature.rigify_colors[1].active",
        "armature.rigify_colors[2].name",
        "armature.rigify_colors[2].normal",
        "armature.rigify_colors[2].select",
        "armature.rigify_colors[2].active",
        "armature.rigify_colors[3].name",
        "armature.rigify_colors[3].normal",
        "armature.rigify_colors[3].select",
        "armature.rigify_colors[3].active",
        "armature.rigify_colors[4].name",
        "armature.rigify_colors[4].normal",
        "armature.rigify_colors[4].select",
        "armature.rigify_colors[4].active",
        "armature.rigify_colors[5].name",
        "armature.rigify_colors[5].normal",
        "armature.rigify_colors[5].select",
        "armature.rigify_colors[5].active",

        "armature.layers[0]",
        "armature.rigify_layers[0].name",
        "armature.rigify_layers[0].row",
        "armature.rigify_layers[0].set",
        "armature.rigify_layers[0].group",
        "armature.layers[1]",
        "armature.rigify_layers[1].name",
        "armature.rigify_layers[1].row",
        "armature.rigify_layers[1].set",
        "armature.rigify_layers[1].group",
        "armature.layers[2]",
        "armature.rigify_layers[2].name",
        "armature.rigify_layers[2].row",
        "armature.rigify_layers[2].set",
        "armature.rigify_layers[2].group",
        "armature.layers[3]",
        "armature.rigify_layers[3].name",
        "armature.rigify_layers[3].row",
        "armature.rigify_layers[3].set",
        "armature.rigify_layers[3].group",
        "armature.layers[4]",
        "armature.rigify_layers[4].name",
        "armature.rigify_layers[4].row",
        "armature.rigify_layers[4].set",
        "armature.rigify_layers[4].group",
        "armature.layers[5]",
        "armature.rigify_layers[5].name",
        "armature.rigify_layers[5].row",
        "armature.rigify_layers[5].set",
        "armature.rigify_layers[5].group",
        "armature.layers[6]",
        "armature.rigify_layers[6].name",
        "armature.rigify_layers[6].row",
        "armature.rigify_layers[6].set",
        "armature.rigify_layers[6].group",
        "armature.layers[7]",
        "armature.rigify_layers[7].name",
        "armature.rigify_layers[7].row",
        "armature.rigify_layers[7].set",
        "armature.rigify_layers[7].group",
        "armature.layers[8]",
        "armature.rigify_layers[8].name",
        "armature.rigify_layers[8].row",
        "armature.rigify_layers[8].set",
        "armature.rigify_layers[8].group",
        "armature.layers[9]",
        "armature.rigify_layers[9].name",
        "armature.rigify_layers[9].row",
        "armature.rigify_layers[9].set",
        "armature.rigify_layers[9].group",
        "armature.layers[10]",
        "armature.rigify_layers[10].name",
        "armature.rigify_layers[10].row",
        "armature.rigify_layers[10].set",
        "armature.rigify_layers[10].group",
        "armature.layers[12]",
        "armature.rigify_layers[12].name",
        "armature.rigify_layers[12].row",
        "armature.rigify_layers[12].set",
        "armature.rigify_layers[12].group",
        "armature.layers[13]",
        "armature.rigify_layers[13].name",
        "armature.rigify_layers[13].row",
        "armature.rigify_layers[13].set",
        "armature.rigify_layers[13].group",
        "armature.layers[14]",
        "armature.rigify_layers[14].name",
        "armature.rigify_layers[14].row",
        "armature.rigify_layers[14].set",
        "armature.rigify_layers[14].group",
        "armature.layers[15]",
        "armature.rigify_layers[15].name",
        "armature.rigify_layers[15].row",
        "armature.rigify_layers[15].set",
        "armature.rigify_layers[15].group",
        "armature.layers[16]",
        "armature.rigify_layers[16].name",
        "armature.rigify_layers[16].row",
        "armature.rigify_layers[16].set",
        "armature.rigify_layers[16].group",
        "armature.layers[17]",
        "armature.rigify_layers[17].name",
        "armature.rigify_layers[17].row",
        "armature.rigify_layers[17].set",
        "armature.rigify_layers[17].group",
        "armature.layers[18]",
        "armature.rigify_layers[18].name",
        "armature.rigify_layers[18].row",
        "armature.rigify_layers[18].set",
        "armature.rigify_layers[18].group",
        "armature.layers[19]",
        "armature.rigify_layers[19].name",
        "armature.rigify_layers[19].row",
        "armature.rigify_layers[19].set",
        "armature.rigify_layers[19].group",
        "armature.layers[20]",
        "armature.rigify_layers[20].name",
        "armature.rigify_layers[20].row",
        "armature.rigify_layers[20].set",
        "armature.rigify_layers[20].group",
        "armature.layers[21]",
        "armature.rigify_layers[21].name",
        "armature.rigify_layers[21].row",
        "armature.rigify_layers[21].set",
        "armature.rigify_layers[21].group",
        "armature.layers[22]",
        "armature.rigify_layers[22].name",
        "armature.rigify_layers[22].row",
        "armature.rigify_layers[22].set",
        "armature.rigify_layers[22].group",
        "armature.layers[23]",
        "armature.rigify_layers[23].name",
        "armature.rigify_layers[23].row",
        "armature.rigify_layers[23].set",
        "armature.rigify_layers[23].group",
        "armature.layers[24]",
        "armature.rigify_layers[24].name",
        "armature.rigify_layers[24].row",
        "armature.rigify_layers[24].set",
        "armature.rigify_layers[24].group",
        "armature.layers[25]",
        "armature.rigify_layers[25].name",
        "armature.rigify_layers[25].row",
        "armature.rigify_layers[25].set",
        "armature.rigify_layers[25].group",
        "armature.layers[26]",
        "armature.rigify_layers[26].name",
        "armature.rigify_layers[26].row",
        "armature.rigify_layers[26].set",
        "armature.rigify_layers[26].group",
        "armature.layers[27]",
        "armature.rigify_layers[27].name",
        "armature.rigify_layers[27].row",
        "armature.rigify_layers[27].set",
        "armature.rigify_layers[27].group",
        "armature.layers[28]",
        "armature.rigify_layers[28].name",
        "armature.rigify_layers[28].row",
        "armature.rigify_layers[28].set",
        "armature.rigify_layers[28].group",
        "armature.layers[29]",
        "armature.layers[30]",
        "armature.layers[31]",

        "bpy.context.window_manager.rigify_advanced_generation",
        "bpy.context.window_manager.rigify_generate_mode",
        "bpy.context.window_manager.rigify_rig_basename",
        "bpy.context.window_manager.rigify_target_rig",
        "bpy.context.window_manager.rigify_rig_ui",
        "bpy.context.window_manager.rigify_force_widget_update",
        ]

    # where to store the preset
    preset_subdir = "rigify/settings_presets"



#Get preset folders
def PresetFolders():
    """Return paths for both local and user preset folders"""

    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(script_file)
    localDir = os.path.join(directory, "metarigs")

    #rig_presets = os.path.join(localDir,"rig_presets")

    #if os.path.isdir(rig_presets):
    #    pass
    #else:
    #    os.makedirs(rig_presets)

    return localDir


def RigFolderItems(self, context):
    rigFolderItems = []
    rigFolderItems.append(("0", "Rig Presets", PresetFolders()))
    for folder in os.listdir(PresetFolders()):
        if os.path.isdir(PresetFolders()+"/"+folder):
            path = os.path.abspath(os.path.abspath(folder))
            rigFolderItems.append((folder, folder, path))

    return rigFolderItems




## NEW PRESET SECTION
IDStore = bpy.types.WindowManager
IDStore.rigify_presets = bpy.props.BoolProperty(name="Rigify Presets",
                                                description="Save/load Rigify rig presets",
                                                default=False)

IDStore.rigify_addfolder = bpy.props.BoolProperty(name="Add Folder",
                                                description="Adds new folder in preset folder",
                                                default=False)

IDStore.rigify_presetName = bpy.props.StringProperty(name='Preset Name',
                        description='Name of the preset to be saved. Use lowercase only, don\'t use special characters, dashes or spaces, numbers. All of these will be striped or replaced by underscore.',
                        default='',
                        subtype='FILE_NAME')

IDStore.rigify_presetFolder = bpy.props.StringProperty(name='New Folder',
                        description='Name new folder to be added in presets folder',
                        default='')

IDStore.rigify_overwrite = bpy.props.BoolProperty(name='Overwrite',
        description='When checked, overwrite existing preset files when saving',
        default=False)


IDStore.rigify_folders = bpy.props.EnumProperty(items=RigFolderItems,
                                                   name="Rigify Preset Folders",
                                                   description="Choose folder to add preset")


class AddRigPreset(bpy.types.Operator):
    """ Creates Python code that will generate the selected metarig.
    """
    bl_idname = "armature.rigify_add_rig_preset"
    bl_label = "Add Rig Preset"
    bl_options = {'UNDO'}

    #@classmethod
    #def poll(self, context):
        #return context.mode == 'EDIT_ARMATURE'

    def execute(self, context):
        bpy.ops.object.mode_set(mode='EDIT')
        C = context
        id_store = C.window_manager

        filename = id_store.rigify_presetName
        filename = re.sub(' ', '_', filename)
        filename = re.sub('-', '_', filename)
        filename = filename.lower()
        filename = re.sub('[^0a-z_]+', '', filename)
        print("## filename: %s" % filename)
        if id_store.rigify_addfolder:
            subf = "/"+id_store.rigify_presetFolder
            makeDir = PresetFolders()+"/"+subf
            print("## check dir: %s" % os.path.isdir(makeDir))
            if os.path.isdir(makeDir):
                pass
            else:
                os.makedirs(makeDir)
        else:
            if id_store.rigify_folders == "0":
                subf = ""
            else:
                subf = "/"+id_store.rigify_folders

        fpath = os.path.join(PresetFolders()+subf, filename + '.py')

        if (filename == "") or (id_store.rigify_addfolder and (id_store.rigify_presetFolder=="")):
            bpy.ops.object.mode_set(mode='OBJECT')
            self.report({'ERROR'}, 'No name set')
            return {'CANCELLED'}
        elif (not os.path.exists(fpath)) or (os.path.exists(fpath) and id_store.rigify_overwrite):
            data = write_metarig(context.active_object, layers=True, func_name="create", groups=True)
            #text_block.write(text)
            #f = open(os.path.join(PresetFolders(), subf, filename + '.py'), 'w')
            f = open(os.path.join(fpath), 'w')
            f.write(data)
            f.close()
            bpy.ops.object.mode_set(mode='OBJECT')
            return {'FINISHED'}
        else:
            bpy.ops.object.mode_set(mode='OBJECT')
            self.report({'ERROR_INVALID_INPUT'}, 'Preset Already Exists')
            return {'CANCELLED'}



# Draw into an existing panel
def panel_func(self, context):
    C = context
    id_store = C.window_manager
    layout = self.layout
    col = layout.column()
    row = col.row()
    if id_store.rigify_advanced_generation:
        icon="DISCLOSURE_TRI_DOWN"
    else:
        icon="DISCLOSURE_TRI_RIGHT"

    row.prop(id_store, "rigify_presets", toggle=True, icon=icon)

    if id_store.rigify_presets:
        #Add Rigify Settings Prest Menu
        #row = layout.row(align=True)
        #row.menu(RIGIFY_MT_SettingsPresetMenu.__name__, text=RIGIFY_MT_SettingsPresetMenu.bl_label)
        #row.operator(RIGIFY_OT_AddSettingsPreset.bl_idname, text="", icon='ZOOMIN') #preset_values = context
        #row.operator(RIGIFY_OT_AddSettingsPreset.bl_idname, text="", icon='ZOOMOUT').remove_active = True
        #layout.separator()


        #layout.label(text="Save Rig Setup:")
        split = layout.split(percentage=0.3)
        split.label(text="Preset name:")
        sub = split.row(align=True)
        sub.prop(id_store, "rigify_presetName", text="")

        split = layout.split(percentage=0.3)
        split.label(text="Folder:")
        sub = split.row(align=True)
        sub.prop(id_store, "rigify_folders", text="")
        sub.prop(id_store, "rigify_addfolder", text="", icon='NEWFOLDER')
        #sub.active = id_store.rigify_addfolder == False

        if id_store.rigify_addfolder:
            setattr(id_store,'rigify_folders', "0")
            split = layout.split(percentage=0.3)
            split.label("Preset Folder:")
            subs = split.row(align=True)
            subs.prop(id_store, "rigify_presetFolder", text="")
            subs.active =  id_store.rigify_addfolder == True

        split = layout.split(percentage=0.3)
        split.prop(id_store, "rigify_overwrite")
        sub = split.row(align=True)
        sub.operator('armature.rigify_add_rig_preset')

    # OLD ADD SETUP
    #row = layout.row(align=True)
    #row.prop(arm, 'rig_presets')
    #row.operator('rigify.add_rig_preset', text="", icon='ZOOMIN')

    #row.prop(arm, 'overwrite')
    #sub = layout.row()
    #sub.operator('rigify.import_rig')
    #sub.active =  arm.rig_presets != "0"
    #sub.enabled =  arm.rig_presets != "0"
    #



classes = (
    RIGIFY_MT_SettingsPresetMenu,
    RIGIFY_OT_AddSettingsPreset,
    AddRigPreset,
    )


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.types.DATA_PT_rigify_bone_groups.prepend(panel_func)
    bpy.types.DATA_PT_rigify_buttons.append(panel_func)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.DATA_PT_rigify_buttons.remove(panel_func)


if __name__ == "__main__":
    register()
