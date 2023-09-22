import streamlit as st
from PIL import Image, ImageOps
import cv2
import numpy as np


# Load images with transparent backgrounds
ground = Image.open("./Images_resized/ground.png").convert("RGBA")
landscape1 = Image.open("./Images_resized/landscape1.png").convert("RGBA")
landscape2 = Image.open("./Images_resized/landscape2.png").convert("RGBA")
facility1 = Image.open("./Images_resized/facility1.png").convert("RGBA")
facility2 = Image.open("./Images_resized/facility2.png").convert("RGBA")
fence = Image.open("./Images_resized/fence.png").convert("RGBA")
turf = Image.open("./Images_resized/turf.png").convert("RGBA")
casks = Image.open("./Images_resized/casks.png").convert("RGBA")
pole = Image.open("./Images_resized/pole.png").convert("RGBA")
light = Image.open("./Images_resized/light.png").convert("RGBA")
truck = Image.open("./Images_resized/truck.png").convert("RGBA")
engine = Image.open("./Images_resized/engine.png").convert("RGBA")
wheels = Image.open("./Images_resized/wheels.png").convert("RGBA")
lift = Image.open("./Images_resized/lift.png").convert("RGBA")
shaft = Image.open("./Images_resized/shaft.png").convert("RGBA")
plant1 = Image.open("./Images_resized/plant1.png").convert("RGBA")
plant2 = Image.open("./Images_resized/plant2.png").convert("RGBA")
cloud = Image.open("./Images_resized/cloud.png").convert("RGBA")
sun = Image.open("./Images_resized/sun.png").convert("RGBA")
frame = Image.open("./Images_resized/frame.png").convert("RGBA")
text = Image.open("./Images_resized/texts.png").convert("RGBA")

# Set the page title and header
st.set_page_config(page_title="Visual Impact Mitigation", layout="centered")

# Apply Arial font to the entire Streamlit app using CSS
st.markdown(
    """
    <style>
    /* Apply Arial font to all text */
    body, h1, h2, h3, h4, h5, h6, p, span, div {
        font-family: Arial, sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject custom CSS to set the width of the sidebar
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 300px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a title to the Streamlit sidebar and customize its font size
# st.sidebar.markdown("<h1 style='font-size: 24px;'>Customize Scene</h1>", unsafe_allow_html=True)

# Create a dropdown menu to select a plant type
st.sidebar.header("Customize Scene")
selected_landscape = st.sidebar.selectbox("Choose Landscape Type", ["Forest", "Desert"])
selected_facility = st.sidebar.selectbox("Choose Facility Type", ["Wide", "Narrow"])
selected_vegetation = st.sidebar.selectbox("Choose Vegetation Type", ["Conifers", "Succulent"])

# Display the composite image using Streamlit and customize its font size
st.markdown("<h1 style='font-size: 32px; text-align: center;'>Visual Impact Mitigation Strategies</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([0.5,1,1,0.5])

with col2:
    # st.sidebar.header("Customize Facility")
    selected_texture_facility = st.selectbox("Choose Facility Texture", ["Texture 1", "Texture 2", "Texture 3"])
with col3:
    # st.sidebar.header("Customize Grass")
    selected_grass_turf = st.selectbox("Choose Grass Texture", ["Grass 1", "Grass 2", "Grass 3"])

# Create color pickers to set colors to images
# facility_color = st.sidebar.color_picker("Choose Facility Color", "#FFFFFF")  # Default color is white
st.sidebar.header("Customize Color")
equip_color = st.sidebar.color_picker("Choose Equipment Color", '#f36e21')  # Default color is white
fence_color = st.sidebar.color_picker("Choose Fence Color", '#FFFFFF')  # Default color is white
# casks_color = st.sidebar.color_picker("Choose Casks Color", '#ECFBFF')  # Default color is white
light_color = st.sidebar.color_picker("Choose Light", '#FFFF00')  # Default color is white

# Create a blank canvas with the size of the first image (ground in this case)
composite = Image.new("RGBA", ground.size, (135, 206, 235, 255))
# composite = Image.new("RGBA", ground.size, (14, 166, 223, 126))

# Function to recolor an image while preserving transparency
from PIL import Image, ImageOps
def recolor_image(image, color):
    image.load()
    r, g, b, alpha = image.split()
    gray = ImageOps.grayscale(image)
    result = ImageOps.colorize(gray, (0, 0, 0, 0), color) 
    result.putalpha(alpha)
    return result

# Recolor the images based on selected images
ground_recolored = recolor_image(ground, "#808080")
landscape1_recolored = recolor_image(landscape1, "#858585")
landscape2_recolored = recolor_image(landscape2, "#858585")
facility1_recolored = recolor_image(facility1, "#FFFFFF")
facility2_recolored = recolor_image(facility2, "#FFFFFF")
fence_recolored = recolor_image(fence, fence_color)
turf_recolored = recolor_image(turf, "#FFFFFF")
casks_recolored = recolor_image(casks, '#FFFFFF')
pole_recolored = recolor_image(pole, "#808080")
light_recolored = recolor_image(light, light_color)
shaft_recolored = recolor_image(shaft, '#FFFFFF')
lift_recolored = recolor_image(lift, equip_color)
engine_recolored = recolor_image(engine, '#FFFFFF')
truck_recolored = recolor_image(truck, equip_color)
wheels_recolored = recolor_image(wheels, '#929191')
plant1_recolored = recolor_image(plant1, '#7ac143')
plant2_recolored = recolor_image(plant2, '#7ac143')
cloud_recolored = recolor_image(cloud, '#FFFFFF')
sun_recolored = recolor_image(sun, '#FFFF00')
frame_recolored = recolor_image(frame, "#FFFFFF")
text_recolored = recolor_image(text, "#FFFFFF")

# Overlay each image separately on a blank canvas
composite = Image.alpha_composite(composite, ground_recolored)
composite = Image.alpha_composite(composite, fence_recolored)
composite = Image.alpha_composite(composite, casks_recolored)
composite = Image.alpha_composite(composite, pole_recolored)
composite = Image.alpha_composite(composite, light_recolored)
composite = Image.alpha_composite(composite, shaft_recolored)
composite = Image.alpha_composite(composite, lift_recolored)
composite = Image.alpha_composite(composite, engine_recolored)
composite = Image.alpha_composite(composite, wheels_recolored)
composite = Image.alpha_composite(composite, truck_recolored)
composite = Image.alpha_composite(composite, cloud_recolored)
composite = Image.alpha_composite(composite, sun_recolored)
if selected_landscape == "Forest":
    composite = Image.alpha_composite(composite, landscape1_recolored)
elif selected_landscape == "Desert":
    composite = Image.alpha_composite(composite, landscape2_recolored)

def apply_texture(img, texture):
    # Convert the PIL Image to a NumPy array
    img_array = np.array(img)

    # Create a mask for the white cutout (non-transparent portion)
    white_mask = (img_array[:, :, 0] == 255) & (img_array[:, :, 1] == 255) & (img_array[:, :, 2] == 255)

    # Resize the texture image to match the truck image dimensions
    texture = cv2.resize(texture, (img_array.shape[1], img_array.shape[0]))

    # Apply the texture only to the white cutout portion
    result = img_array.copy()
    result[white_mask, :3] = texture[white_mask, :3]

    # Convert the modified NumPy array back to a PIL Image
    result_image = Image.fromarray(result)

    return result_image

# Create a dictionary to map texture names to file paths (assuming textures are in jpg format)
textures = {
    "Texture 1": "./textures/texture1.jpg",
    "Texture 2": "./textures/texture2.jpg",
    "Texture 3": "./textures/texture3.jpg",
}
# Apply texture to facility1

texture_img_facility = cv2.imread(textures[selected_texture_facility], cv2.IMREAD_UNCHANGED)
texture_img_facility = texture_img_facility[:, :, ::-1]  # BGR to RGB conversion
facility1_recolored = apply_texture(facility1_recolored, texture_img_facility)
facility2_recolored = apply_texture(facility2_recolored, texture_img_facility)

if selected_facility == "Wide":
    composite = Image.alpha_composite(composite, facility2_recolored)
elif selected_facility == "Narrow":
    composite = Image.alpha_composite(composite, facility1_recolored)

# Create a dictionary to map texture names to file paths (assuming textures are in jpg format)
grass = {
    "Grass 1": "./textures/grass1.jpg",
    "Grass 2": "./textures/grass2.jpg",
    "Grass 3": "./textures/grass3.jpg"
}
# Apply grass to turf
grass_img_turf = cv2.imread(grass[selected_grass_turf], cv2.IMREAD_UNCHANGED)
# Perform BGR to RGB conversion on the loaded image
grass_img_turf = cv2.cvtColor(grass_img_turf, cv2.COLOR_BGR2RGB)
turf_recolored = apply_texture(turf_recolored, grass_img_turf)

if selected_vegetation == "Conifers":
    composite = Image.alpha_composite(composite, plant1_recolored)
elif selected_vegetation == "Succulent":
    composite = Image.alpha_composite(composite, plant2_recolored)
composite = Image.alpha_composite(composite, frame_recolored)
composite = Image.alpha_composite(composite, turf_recolored)
composite = Image.alpha_composite(composite, text_recolored)

# st.image(composite, caption="Illustrated CISF", use_column_width=True)
st.image(composite, use_column_width=True)

# Run the Streamlit app with `streamlit run your_script.py`
