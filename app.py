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
    #audioName = filename[:-4] + ".mp3" 
    audioName = filename[:-4] + f".{selected_ext}"
    clip.audio.write_audiofile(audioName)
    clip.close()
    return audioName

st.set_page_config(page_title="Video Converter")

# Headings for Web App
st.title("YouTube converter")

extensions = dict(mp3="mp3", wav="wav")
selected_ext = st.selectbox("Choose the file extension you want", extensions)

# textbox used for getting video link
st.subheader("Enter the video link below")
vidLink = st.text_input("Enter Link: ")

if vidLink:
    
    # display converted mp3 file for download
    st.subheader("Result")

    filename = download_video(vidLink)
    st.text("Downloaded video as " + filename)

    audioFile = convert_to_mp3(filename)
    st.text(f"Converted video to {selected_ext}")

    os.remove(filename)
    
    
    # Defaults to 'application/octet-stream'
    with open(audioFile, "rb") as file:

        st.audio(data=file, format=f'audio/{selected_ext}', start_time=0)

        vidName = ""
        vidName = st.text_input("(Optional) Save as: (default= {0}) ".format(audioFile[:-4]))

        if vidName == "":
            vidName = audioFile[:-4]

        btn = st.download_button(
                label="Download",
                data=file,
                #file_name= audioFile ,
                file_name= vidName+f".{selected_ext}",
            )
      

    os.remove(audioFile)
    # this works! - st.text("Audio file removed from system")


