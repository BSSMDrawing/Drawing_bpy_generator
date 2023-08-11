import bpy

# 단위 시스템을 Metric으로 설정하고, 단위를 Centimeters로 설정
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.scale_length = 0.01  # 1 미터 = 100 센티미터
