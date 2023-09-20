import streamlit as st
from PIL import Image, ImageOps

# Load images with transparent backgrounds
ground = Image.open("./Images/ground.png").convert("RGBA")
facility = Image.open("./Images/facility.png").convert("RGBA")
fence = Image.open("./Images/fence.png").convert("RGBA")
casks = Image.open("./Images/casks.png").convert("RGBA")
pole = Image.open("./Images/pole.png").convert("RGBA")
light = Image.open("./Images/light.png").convert("RGBA")
plant1 = Image.open("./Images/plant1.png").convert("RGBA")
plant2 = Image.open("./Images/plant2.png").convert("RGBA")
cloud = Image.open("./Images/cloud.png").convert("RGBA")
truck = Image.open("./Images/truck.png").convert("RGBA")
cargo = Image.open("./Images/cargo.png").convert("RGBA")
lift = Image.open("./Images/lift.png").convert("RGBA")
shaft = Image.open("./Images/shaft.png").convert("RGBA")

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

# Set the page title and header
st.set_page_config(page_title="Mitigation Strategies", layout="centered")

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
selected_vegetation = st.sidebar.selectbox("Choose Vegetation Type", ["Rainforest", "Desert"])
# Create color pickers to set colors to images
# ground_color = st.sidebar.color_picker("Choose Ground Color", "#808080")  # Default color is gray
facility_color = st.sidebar.color_picker("Choose Facility Color", "#FFFFFF")  # Default color is white
fence_color = st.sidebar.color_picker("Choose Fence Color", '#FFFFFF')  # Default color is white
casks_color = st.sidebar.color_picker("Choose Cask Color", "#FFFFFF")  # Default color is white
light_color = st.sidebar.color_picker("Choose Light", '#FFFF00')  # Default color is white
shaft_color = st.sidebar.color_picker("Choose Forklift Color", '#FFFFFF')  # Default color is white
cargo_color = st.sidebar.color_picker("Choose Truck Color", '#FFFFFF')  # Default color is white

# Recolor the images based on selected images
ground_recolored = recolor_image(ground, "#808080")
facility_recolored = recolor_image(facility, facility_color)
fence_recolored = recolor_image(fence, fence_color)
casks_recolored = recolor_image(casks, casks_color)
pole_recolored = recolor_image(pole, '#FFFFFF')
cloud_recolored = recolor_image(cloud, '#FFFFFF')
light_recolored = recolor_image(light, light_color)
shaft_recolored = recolor_image(shaft, shaft_color)
lift_recolored = recolor_image(lift, '#FFFFFF')
cargo_recolored = recolor_image(cargo, cargo_color)
truck_recolored = recolor_image(truck, '#FFFFFF')
plant1_recolored = recolor_image(plant1, '#7ac143')
plant2_recolored = recolor_image(plant2, '#7ac143')

# Overlay each image separately on a blank canvas
composite = Image.alpha_composite(composite, ground_recolored)
composite = Image.alpha_composite(composite, facility_recolored)
composite = Image.alpha_composite(composite, fence_recolored)
composite = Image.alpha_composite(composite, casks_recolored)
composite = Image.alpha_composite(composite, pole_recolored)
composite = Image.alpha_composite(composite, shaft_recolored)
composite = Image.alpha_composite(composite, lift_recolored)
composite = Image.alpha_composite(composite, truck_recolored)
composite = Image.alpha_composite(composite, cargo_recolored)
composite = Image.alpha_composite(composite, cloud_recolored)
composite = Image.alpha_composite(composite, light_recolored)  # Use the rotated light image
if selected_vegetation == "Rainforest":
    composite = Image.alpha_composite(composite, plant1_recolored)
elif selected_vegetation == "Desert":
    composite = Image.alpha_composite(composite, plant2_recolored)

# Display the composite image using Streamlit and customize its font size
st.markdown("<h1 style='font-size: 32px; text-align: center;'>Mitigation Strategies</h1>", unsafe_allow_html=True)
# st.image(composite, caption="Illustrated CISF", use_column_width=True)
st.image(composite, use_column_width=True)

# Run the Streamlit app with `streamlit run your_script.py`
