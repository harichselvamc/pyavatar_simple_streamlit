# import streamlit as st
# from PIL import Image
# import py_avataaars as pa

# # Initialize PyAvataaar
# avatar = pa.PyAvataaar()

# # Define avatar options
# styles = [pa.AvatarStyle.CIRCLE, pa.AvatarStyle.TRANSPARENT]
# skin_colors = list(pa.SkinColor)
# hair_colors = list(pa.HairColor)
# # Add more options for other avatar properties

# # Streamlit app
# def main():
#     st.title("Avatar Creator")

#     # Avatar options
#     st.sidebar.title("Options")
#     style = st.sidebar.selectbox("Avatar Style", styles)
#     skin_color = st.sidebar.selectbox("Skin Color", skin_colors)
#     hair_color = st.sidebar.selectbox("Hair Color", hair_colors)
#     # Add more sidebar selectboxes for other avatar properties

#     # Generate avatar
#     avatar.style = style
#     avatar.skin_color = skin_color
#     avatar.hair_color = hair_color
#     # Set other avatar properties based on user selection

#     # Preview avatar
#     st.subheader("Avatar Preview")
#     avatar.render_png_file("avatar.png")
#     resized_image = Image.open("avatar.png").resize((1080, 1080))  # Resize the image
#     st.image(resized_image, use_column_width=True)

#     # Download option
#     st.subheader("Download")
#     if st.button("Download Avatar"):
#         st.download_button("Download", data=open("avatar.png", "rb").read(), file_name="avatar.png")

# if __name__ == "__main__":
#     main()


import streamlit as st
from PIL import Image
import py_avataaars as pa

# Initialize PyAvataaar
avatar = pa.PyAvataaar()

# Define avatar options
styles = [pa.AvatarStyle.CIRCLE, pa.AvatarStyle.TRANSPARENT]
skin_colors = list(pa.SkinColor)
hair_colors = list(pa.HairColor)
facial_hair_types = list(pa.FacialHairType)
top_types = list(pa.TopType)
mouth_types = list(pa.MouthType)
eye_types = list(pa.EyesType)
eyebrow_types = list(pa.EyebrowType)
nose_types = list(pa.NoseType)
accessories_types = list(pa.AccessoriesType)
clothe_types = list(pa.ClotheType)
#clothe_graphic_types = list(pa.ClotheGraphicType)
# Add more options for other avatar properties

# Streamlit app
def main():
    st.title("Avatar Creator")

    # Avatar options
    st.sidebar.title("Options")
    style = st.sidebar.selectbox("Avatar Style", styles)
    skin_color = st.sidebar.selectbox("Skin Color", skin_colors)
    hair_color = st.sidebar.selectbox("Hair Color", hair_colors)
    facial_hair_type = st.sidebar.selectbox("Facial Hair Type", facial_hair_types)
    top_type = st.sidebar.selectbox("Top Type", top_types)
    mouth_type = st.sidebar.selectbox("Mouth Type", mouth_types)
    eye_type = st.sidebar.selectbox("Eye Type", eye_types)
    eyebrow_type = st.sidebar.selectbox("Eyebrow Type", eyebrow_types)
    nose_type = st.sidebar.selectbox("Nose Type", nose_types)
    accessories_type = st.sidebar.selectbox("Accessories Type", accessories_types)
    clothe_type = st.sidebar.selectbox("Clothe Type", clothe_types)
    #clothe_graphic_type = st.sidebar.selectbox("Clothe Graphic Type", clothe_graphic_types)

    # Generate avatar
    avatar.style = style
    avatar.skin_color = skin_color
    avatar.hair_color = hair_color
    avatar.facial_hair_type = facial_hair_type
    avatar.top_type = top_type
    avatar.mouth_type = mouth_type
    avatar.eye_type = eye_type
    avatar.eyebrow_type = eyebrow_type
    avatar.nose_type = nose_type
    avatar.accessories_type = accessories_type
    avatar.clothe_type = clothe_type
    #avatar.clothe_graphic_type = clothe_graphic_type
    # Set other avatar properties based on user selection

    # Preview avatar
    st.subheader("Avatar Preview")
    avatar.render_png_file("avatar.png")
    resized_image = Image.open("avatar.png").resize((1080, 1080))  # Resize the image
    st.image(resized_image, use_column_width=True)

    # Download option
    st.subheader("Download")
    if st.button("Download Avatar"):
        st.download_button("Download", data=open("avatar.png", "rb").read(), file_name="avatar.png")

if __name__ == "__main__":
    main()
