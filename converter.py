import subprocess
import os

def convert_engine(file_path, target_ext, val, save_path):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(save_path, f"{base_name}_DLX.{target_ext}")

    if target_ext in ["mp3", "flac", "wav", "m4a"]:
        bitrate = val.replace('k', '')
        cmd = f'ffmpeg -i "{file_path}" -vn -ab {bitrate}k -preset ultrafast -y "{output_path}"'
    else:
        scale = f"scale=-1:{val.replace('p', '')}" if "p" in val else ""
        cmd = f'ffmpeg -i "{file_path}" -vf "{scale}" -c:v libx264 -preset ultrafast -crf 20 -c:a copy -y "{output_path}"'

    subprocess.run(cmd, shell=True, check=True)
    return output_path