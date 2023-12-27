import bpy
from bpy.types import Panel, Operator
from bpy.utils import register_class, unregister_class
from localization_test.translations import translations_dict


bl_info = {
    'name': 'Localization Test',
    'category': 'All',
    'version': (1, 0, 0),
    'blender': (2, 91, 0),
}

class LOCALIZATION_TEST_OT_test(Operator):
    bl_idname = 'localization_test.test'
    bl_label = 'Operator name' # translated
    bl_description = "Operator description" # not translated

    def execute(self, context):
        text = 'Test text for printing in system console'
        print(bpy.app.translations.pgettext(text))
        self.report({"INFO"}, text) # auto translated
        return {'FINISHED'}

class LOCALIZATION_TEST_PT_panel(Panel):
    bl_idname = 'LOCALIZATION_TEST_PT_panel'
    bl_label = 'Panel Header'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Localization test'

    def draw(self, context):
        layout = self.layout
        layout.label(text='Test text in Blender UI')
        layout.operator('localization_test.test', icon='BLENDER')

# https://docs.blender.org/api/current/bpy.app.translations.html
# https://wiki.blender.jp/Dev:Doc/Process/Translate_Blender
# https://wiki.blender.org/wiki/Process/Translate_Blender
# make sure to set i18n branches in File Paths -> Development to some valid folder

def register():
    register_class(LOCALIZATION_TEST_OT_test)
    register_class(LOCALIZATION_TEST_PT_panel)
    # automatically will replace all string using locale from `bpy.app.translations.locale`
    # which is a bit annoying since it will replace the strings used by other addons and UI parts
    bpy.app.translations.register(__name__, translations_dict)



def unregister():
    unregister_class(LOCALIZATION_TEST_PT_panel)
    unregister_class(LOCALIZATION_TEST_OT_test)
    bpy.app.translations.unregister(__name__)


if __name__ == '__main__':
    register()
