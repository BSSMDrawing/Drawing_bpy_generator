import bpy

# 각 평면의 XY 좌표와 생성할 위치 정보
plane_positions = [
    (2, 0, 0),
    (0, 2, 0),
    (-2, 0, 0),
    (0, -2, 0),
    (0, 0, 2),
    (0, 0, -2)
]

# 각 평면 생성 및 위치 설정
for x, y, z in plane_positions:
    bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(x, y, z))
