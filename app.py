import streamlit as st
import pytube
from moviepy.editor import VideoFileClip
import os

def download_video(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    audioName = filename[:-4] + ".mp3"
    clip.audio.write_audiofile(audioName)
    clip.close()
    return audioName

# Headings for Web App
st.title("YouTube to MP3 converter")

# textbox used for getting video link
st.subheader("Enter the video link below")
vidLink = st.text_input("Enter Link: ")

vidName = st.text_input("Enter save file name: ")

if vidLink:
    
    # display converted mp3 file for download
    st.subheader("Result")

    filename = download_video(vidLink)
    st.text("Downloaded video as " + filename)

    audioFile = convert_to_mp3(filename)
    st.text("Converted video to mp3")

    os.remove(filename)
    
    
    # Defaults to 'application/octet-stream'
    with open(audioFile, "rb") as file:
        btn = st.download_button(
                label="Download",
                data=file,
                file_name= audioFile[:5] ,
            )

    os.remove(audioFile)
    # this works! - st.text("Audio file removed from system")


