import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



# Load the audio files
sampling_rate3, data3 = wav.read('_nn_filtered_sample.wav')
sampling_rate2, data2 = wav.read('_filtered_sample.wav')
sampling_rate1, data1 = wav.read('_noisy_sample.wav')

# Convert stereo to mono by averaging channels
if len(data1.shape) > 1:
    data1 = np.mean(data1, axis=1)
if len(data2.shape) > 1:
    data2 = np.mean(data2, axis=1)
if len(data3.shape) > 1:
    data3 = np.mean(data3, axis=1)

# Get the duration of the audio in seconds
duration1 = len(data1) / sampling_rate1
duration2 = len(data2) / sampling_rate2
duration3 = len(data3) / sampling_rate3

# Create the time array for each waveform
time_array1 = np.linspace(0, duration1, data1.shape[0])
time_array2 = np.linspace(0, duration2, data2.shape[0])
time_array3 = np.linspace(0, duration3, data3.shape[0])

# Plot each waveform on a separate subplot
fig, axs = plt.subplots(3, 1, figsize=(10,10))

axs[0].plot(time_array1, data1)
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Noisy Sample')

axs[1].plot(time_array2, data2)
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Filtered Speech')

axs[2].plot(time_array3, data3)
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Amplitude')
axs[2].set_title('Model_Filtered_Sampled')

plt.tight_layout()


# Save the plot to a file
plt.savefig('waveforms1.png')
img = mpimg.imread('waveforms1.png')
plt.imshow(img)
plt.axis('off')
plt.show()
#img = mpimg.imread('figure1 (1).png')
#plt.imshow("waveforms1.png")
# Load the PNG file
# img = mpimg.imread('figure1 (1).png')

# # Show the image as a figure
# plt.imshow(img)
# plt.axis('off')
# plt.show()