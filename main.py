'''
Christopher R. Simpson
SimpsonAerospace (c) 2023
christopher.r.simpson@simpsonaerospace.com
'''
'''
Generate Subtitles from Video
'''
#libraries
import moviepy.editor as mpe
import speech_recognition as sr

def transcribe_video(video_file_path):
  """Transcribes a video to text.

  Args:
    video_file_path: The path to the video file.

  Returns:
    A string containing the transcript of the video.
  """

  # Load the video file.
  video = mpe.VideoFileClip(video_file_path)

  # Extract the audio from the video.
  audio = video.audio

  # Convert the audio to a WAV file.
  audio_file_path = audio.write_audiofile("audio.wav")

  # Load the audio file.
  audio_file = sr.AudioFile(audio_file_path)

  # Create a speech recognizer.
  recognizer = sr.Recognizer()

  # Transcribe the audio.
  with audio_file as source:
    audio_data = recognizer.record(source)

  transcript = recognizer.recognize_google(audio_data)

  return transcript

# Transcribe the video.
transcript = transcribe_video("video.mp4")

# Print the transcript.
print(transcript)

