import bpy

# 프로젝트 파일 경로 설정
project_file_path = "/path/to/your/project.blend"

# 프로젝트 열기
bpy.ops.wm.open_mainfile(filepath=project_file_path)
