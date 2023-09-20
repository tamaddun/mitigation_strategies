import streamlit as st
from PIL import Image, ImageOps

# Load images with transparent backgrounds
ground = Image.open("./Images_resized/ground.png").convert("RGBA")
landscape1 = Image.open("./Images_resized/landscape1.png").convert("RGBA")
landscape2 = Image.open("./Images_resized/landscape2.png").convert("RGBA")
facility1 = Image.open("./Images_resized/facility1.png").convert("RGBA")
facility2 = Image.open("./Images_resized/facility2.png").convert("RGBA")
fence = Image.open("./Images_resized/fence.png").convert("RGBA")
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
st.sidebar.markdown("<h1 style='font-size: 24px;'>Customize Scene</h1>", unsafe_allow_html=True)

# Create a dropdown menu to select a plant type
selected_landscape = st.sidebar.selectbox("Choose Landscape Type", ["Rainforest", "Desert"])
selected_facility = st.sidebar.selectbox("Choose Building Type", ["Wide", "Narrow"])
selected_vegetation = st.sidebar.selectbox("Choose Vegetation Type", ["Evergreen", "Perennial"])

# Create color pickers to set colors to images
facility_color = st.sidebar.color_picker("Choose Facility Color", "#FFFAF6")  # Default color is white
fence_color = st.sidebar.color_picker("Choose Fence Color", '#FFFFFF')  # Default color is white
casks_color = st.sidebar.color_picker("Choose Casks Color", '#ECFBFF')  # Default color is white
light_color = st.sidebar.color_picker("Choose Light", '#FFFF00')  # Default color is white
lift_color = st.sidebar.color_picker("Choose Forklift Color", '#f36e21')  # Default color is white
truck_color = st.sidebar.color_picker("Choose Truck Color", '#FF9C10')  # Default color is white

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
facility1_recolored = recolor_image(facility1, facility_color)
facility2_recolored = recolor_image(facility2, facility_color)
fence_recolored = recolor_image(fence, fence_color)
casks_recolored = recolor_image(casks, casks_color)
pole_recolored = recolor_image(pole, "#808080")
light_recolored = recolor_image(light, light_color)
shaft_recolored = recolor_image(shaft, '#FFFFFF')
lift_recolored = recolor_image(lift, lift_color)
engine_recolored = recolor_image(engine, '#FFFFFF')
truck_recolored = recolor_image(truck, truck_color)
wheels_recolored = recolor_image(wheels, '#FFFFFF')
plant1_recolored = recolor_image(plant1, '#7ac143')
plant2_recolored = recolor_image(plant2, '#7ac143')
cloud_recolored = recolor_image(cloud, '#FFFFFF')
sun_recolored = recolor_image(sun, '#FFFF00')
frame_recolored = recolor_image(frame, "#FFFFFF")
text_recolored = recolor_image(text, "#FFFFFF")

# Overlay each image separately on a blank canvas
composite = Image.alpha_composite(composite, ground_recolored)
composite = Image.alpha_composite(composite, fence_recolored)
# composite = Image.alpha_composite(composite, turf_recolored)
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
if selected_landscape == "Rainforest":
    composite = Image.alpha_composite(composite, landscape1_recolored)
elif selected_landscape == "Desert":
    composite = Image.alpha_composite(composite, landscape2_recolored)
if selected_facility == "Wide":
    composite = Image.alpha_composite(composite, facility2_recolored)
elif selected_facility == "Narrow":
    composite = Image.alpha_composite(composite, facility1_recolored)
if selected_vegetation == "Evergreen":
    composite = Image.alpha_composite(composite, plant1_recolored)
elif selected_vegetation == "Perennial":
    composite = Image.alpha_composite(composite, plant2_recolored)
composite = Image.alpha_composite(composite, frame_recolored)
composite = Image.alpha_composite(composite, text_recolored)

# Display the composite image using Streamlit and customize its font size
st.markdown("<h1 style='font-size: 32px; text-align: center;'>Visual Impact Mitigation Strategies</h1>", unsafe_allow_html=True)
# st.image(composite, caption="Illustrated CISF", use_column_width=True)
st.image(composite, use_column_width=True)

# Run the Streamlit app with `streamlit run your_script.py`
