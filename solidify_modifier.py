import bpy

# 정육면체 큐브 생성
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
cube_obj = bpy.context.active_object

# 모든 면을 분리
for _ in range(5):
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.object.mode_set(mode='OBJECT')
    
    cube_obj.data.polygons[0].select = True
    
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.separate(type='SELECTED')
    bpy.ops.object.mode_set(mode='OBJECT')

# 분리된 면들의 Solidify 모디파이어 추가
for obj in bpy.context.selected_objects:
    # Solidify 모디파이어 추가
    solidify_modifier = obj.modifiers.new("Solidify", 'SOLIDIFY')
    solidify_modifier.thickness = 0.1  # 두께를 설정하세요. 여기서는 0.1로 설정했습니다.
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.modifier_apply(modifier=solidify_modifier.name)
