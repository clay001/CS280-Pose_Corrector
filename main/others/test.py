import os
import sys
import subprocess
import numpy as np

subprocess.call( ['../openpose/build/examples/openpose/openpose.bin',
            '--model_folder', '../openpose/models',
            '--image_dir' , '../openpose/examples/media/',
            '--write_images', 'output_test',
            '--display', '0',
            '--num_gpu', '1',
            '--num_gpu_start', '1'])
