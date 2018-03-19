# SoundArt
# Copyright 2018 pauldamora.com All rights reserved
#
# Authors: Paul D'Amora
#
# Description: Converts an audio file to a png of its waveform.

from app import app
import matplotlib
matplotlib.use("Agg")  # hides the stupid rocketship
from matplotlib import pyplot as plt
import numpy as np
from pydub import AudioSegment

import os
import tempfile


def convert_to_png(file):
    filename = next(tempfile._get_candidate_names()) + ".png"

    # Read the audio file
    extension = file.filename.split('.')[-1]
    sound = AudioSegment.from_file(file, format=extension)
    data = sound.get_array_of_samples()

    # Transform the data so it can be plotted
    t = np.linspace(0, sound.duration_seconds, len(data))
    n = 50
    data = np.array(data)
    filtDat = np.convolve(n, data, mode='valid')  # Get the running mean

    # Plot the graph
    plt.rcParams["figure.figsize"] = (36, 4)
    plt.plot(t, filtDat, '#242424')
    plt.axis('off')
    plt.savefig(os.path.join(*[app.root_path, app.config['UPLOAD_FOLDER'],
                             filename]), bbox_inches='tight', pad_inches=2)
    plt.close()

    return filename
