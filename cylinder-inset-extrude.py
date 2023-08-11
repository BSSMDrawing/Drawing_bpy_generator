import bpy

# Mesh 생성 (Cylinder)
bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, location=(0, 0, 0))
obj = bpy.context.active_object

# 특정 면 선택
face_index = 30  # 생성하는 Mesh가 Cylinder라면 30을 넣기
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode(type="FACE")
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')
obj.data.polygons[face_index].select = True

# Inset 작업
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.inset(thickness=0.2)  # Inset을 적용하고자 하는 두께를 지정

# Extrude 작업 (역으로)
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value": (0, 0, -0.2)})  # Extrude의 깊이를 지정
