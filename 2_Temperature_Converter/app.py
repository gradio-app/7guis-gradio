import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown(
        """# Temperature Converter
        Submit the temperature in either Celsius or Fahrenheit to get the other!
        """
    )

    with gr.Row():
        with gr.Box():
            celsius = gr.Number(0, label="Celsius")
            c2f = gr.Button("Submit")

        with gr.Box():
            fahrenheit = gr.Number(32, label="Fahrenheit")
            f2c = gr.Button("Submit")

    c2f.click(lambda c: c * 9 / 5 + 32, celsius, fahrenheit)
    f2c.click(lambda f: (f - 32) * 5 / 9, fahrenheit, celsius)

if __name__ == "__main__":
    demo.launch()
