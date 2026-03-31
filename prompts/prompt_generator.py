from langchain_core.prompts import PromptTemplate   

# template
template=PromptTemplate(
    template="Hello, I am a researcher interested in {paper_input}. Can you provide an explanation of this paper in a {style_input} style and keep it {length_input}?"
    ,
    input_variables=["paper_input", "style_input", "length_input"]
    ,validate_template=True
)
template.save('template.json')