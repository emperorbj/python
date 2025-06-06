from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableParallel

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

summary_template = ChatPromptTemplate.from_messages(
    [
        ("system","you are a professional movie critic"),
        ("human","give a brief summary of this movie {movie}")
    ]
)



def analyze_plot(plot):
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system","you are a movie critic"),
            ("human","analyze the plot:{plot} of the movie and highlight its strengths and weaknesses")
        ]
    )
    return plot_template.format_prompt(plot=plot)



def analyze_character(character):
    character_template = ChatPromptTemplate.from_messages(
        [
            ("system","you are a movie critic"),
            ("human","analyze the character:{character} in the movie to get their weakness and strenths")
        ]
    )
    return character_template.format_prompt(character=character)



def final_verdict(analyze_plot,analyze_character):
    return f"Plot Analysis:\n{analyze_plot}\n\nCharacter Analysis:\n{analyze_character}"


plot_chain = (
    RunnableLambda(lambda x:analyze_plot(x)) | llm | StrOutputParser()
)

character_chain = (
    RunnableLambda(lambda x:analyze_character(x)) | llm | StrOutputParser()
)


chain = (
    summary_template
    | llm
    | StrOutputParser()
    | RunnableParallel(branches = {"plot":plot_chain,"character":character_chain})
    | RunnableLambda(lambda x: final_verdict(x["branches"]["plot"],x["branches"]["character"]))
)
results = chain.invoke({"movie":"naruto shippuden"})

print(results)