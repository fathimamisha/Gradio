gr.close_all()

def getDetails(name, age, preference, hobbies):
    return f"Name: {name}, Age: {age}, Subject Preference: {preference}, Hobbies: {hobbies}"  # Change 1

demo = gr.Interface(
    fn=getDetails,
    inputs=[
        gr.Textbox(label="Name: "),
        gr.Slider(label="Age: ", minimum=1, maximum=100),  # Change 2
        gr.Radio(label="Subject Preference: ", choices=["Science", "Commerce", "Arts"]),
        gr.CheckboxGroup(label="Hobbies:", choices=["Reading", "Sports", "Music"])
    ],
    outputs=gr.Textbox()
)
demo.launch()
