import streamlit as st 
from api_calling import note_generator, audio_transcription,quiz_generator
from PIL import Image


#title
st.title("Note Summary and Quiz Generator" , anchor = False)
st.markdown("Upload upto 3 images to generate note summary and Quizes")
st.divider()

with st.sidebar:
    st.header("Controls")

    #Images
    images = st.file_uploader(
        "Upload the Photos of Your Notes" ,
        type = ['jpg', 'jpeg', 'png'],
        accept_multiple_files=True,
    )

    pil_images = []

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    if  images:
        if len(images) > 3:
            st.error("Maximum Upload Reached")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))

            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)

    #difficulty
    selected_option = st.selectbox(
        "Enter the Difficulty of Quiz",
        ("Easy", "Medium", "Hard"),
        index = None,
    )
    

    pressed = st.button("Click the button to initiate AI",
              type = "primary",
              
              )
    

if pressed:
    if not images:
        st.error("You must upload atleast 1 image")
    if not selected_option:
        st.error("you must select a difficulty")
    if images and selected_option:

        #note

        with st.container(border = True):
            st.subheader("Your Note")


            with st.spinner("AI is writing notes for you"):
                generated_notes = note_generator(pil_images)    
                st.markdown(generated_notes)

        #audio transcript
        with st.container(border=True):
            st.subheader("Audio Transcription")

            with st.spinner("AI is generating Audio :-"):

                #clearing The Markdown
                generated_notes = generated_notes.replace("#","")
                generated_notes = generated_notes.replace("*","")
                generated_notes = generated_notes.replace("_","")
                generated_notes = generated_notes.replace("`","")
                audio_transcript = audio_transcription(generated_notes)
                st.audio(audio_transcript)



        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected_option}) Difficulty")
            with st.spinner("AI is Generating Quizes, Please wait..."):
                quizzes = quiz_generator(pil_images, selected_option)
                st.markdown(quizzes)