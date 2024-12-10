import subprocess
import os

# 기본 경로
base_dir = r'C:/Users/tta/Desktop/koiOcrTester'  # 경로에서 슬래시를 일관되게 사용

# sample 폴더 경로 (여기서 1부터 1000까지의 sample 폴더를 실행할 수 있습니다)
for i in range(1, 1001):  # 1부터 1000까지 반복
    sample_folder = os.path.join(base_dir, f'sample{i}')
    
    # sample 폴더가 존재하는지 확인
    if os.path.exists(sample_folder):
        # 명령어 실행 (java -jar koiOcrTester.jar D "sample 폴더 경로")
        command = ['java', '-jar', 'koiOcrTester.jar', 'D', sample_folder]

        # 명령어 출력 (디버깅용)
        print(f"실행 중: {command}")

        # 명령어 실행
        result = subprocess.run(command, shell=True, cwd=base_dir)

        # 실행 결과 출력
        if result.returncode == 0:
            print(f"{sample_folder} 폴더에 대해 명령어 실행 성공")
        else:
            print(f"{sample_folder} 폴더에 대해 명령어 실행 실패")
    else:
        print(f"폴더 {sample_folder}가 존재하지 않습니다.") 
