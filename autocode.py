import os
import shutil

source_directory = 'C:/Users/tta/Downloads/document'


destination_directory = 'C:/Users/tta/Desktop/koiOcrTester'


files = [f for f in os.listdir(source_directory) if f.endswith('.jpg')]

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

for i, file in enumerate(files):

    sample_folder = os.path.join(destination_directory, f'sample{i+1}')
    
    if not os.path.exists(sample_folder):
        os.makedirs(sample_folder)
    
    source_file_path = os.path.join(source_directory, file)
    
    destination_file_path = os.path.join(sample_folder, file)
    
    shutil.copy(source_file_path, destination_file_path)

    print(f'{file} has been copied to {sample_folder}')
