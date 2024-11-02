import streamlit as st
import plotly.graph_objects as go

# Streamlit title
st.title('First App by Nikita')

# Input for username
username = st.text_input('Give me your name')

# Slider for selecting a number
number = st.slider('Select number', 0, 10)

# Check if the number is even or odd and display a message
if number % 2 == 0:
    st.write(f'Hello {username}, your number is divisible by 2.')
else:
    st.write(f'Hello {username}, your number is not divisible by 2.')

# Button that displays a message when clicked
if st.button('Dumb Ape Button'):
    st.write('Why did you click this button?')

# Sample data for 3D scatter plot
X = [1, 2, 3, 4, 5]
Y = [10, 15, 13, 17, 11]
Z = [5, 6, 7, 8, 9]

# Create a 3D scatter plot with Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=X,
    y=Y,
    z=Z,
    mode='markers',
    marker=dict(
        size=8,
        color=Z,  # Set color based on Z values
        colorscale='Viridis',  # Color scale
        opacity=0.8
    )
)])

# Customize the layout
fig.update_layout(
    title="3D Scatter Plot of X, Y, Z",
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    )
)

# Display the plot in Streamlit
st.plotly_chart(fig)

