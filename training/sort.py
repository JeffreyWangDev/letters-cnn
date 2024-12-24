import csv
import os
import shutil

def sort_images_by_latex(csv_filepath, base_image_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(csv_filepath, mode="r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            image_path = os.path.join(base_image_path, row["path"])
            latex_folder = os.path.join(output_dir, row["latex"].replace("\\",""))

            try:
                if not os.path.exists(latex_folder):
                    os.makedirs(latex_folder)

                shutil.copy(image_path, latex_folder) 
            except:
                print(f"Error copying {image_path} to {latex_folder}")
                continue

csv_filepath = "./data/HASYv2/hasy-data-labels.csv"
base_image_path = "./data/HASYv2"
output_dir = "./out"
sort_images_by_latex(csv_filepath, base_image_path, output_dir) 
