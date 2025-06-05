from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap,RunnableLambda,RunnableParallel
load_dotenv()

# messages = [
#     SystemMessage("you are professional therapist"),
#     HumanMessage("suggest in three sentences how to deal with depression")
# ]

# chat_model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# response = chat_model.invoke(messages)

# print(f"Doctor AI: {response.content}")




# -------------conversional chat with chat history------------------

# chat_history = []

# system_message = SystemMessage(content="Your a professional Financial Auditor")

# chat_history.append(system_message)

# while True:
#     my_query = input("message:")
#     if my_query == "exit":
#         break
#     chat_history.append(HumanMessage(my_query))
#     model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
#     results = model.invoke(chat_history)
#     response = results.content
#     print(f"{response}")
#     chat_history.append(AIMessage(response))

# print("--------Chat History-----------")
# print(chat_history)
# firebase project id = langchain-23ed6
# firebase project number = 447319267519


# ------------------------------prompt templates---------------
# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# template = "generate a {tone} email to {company} about how you can use your {skills} to add value to them in just 4 lines"
# prompt_template = ChatPromptTemplate.from_template(template)

# prompt = prompt_template.invoke({
#     "tone":"funny",
#     "company":"Interswitch",
#     "skills":"full stack ai engineer"
# })

# response = llm.invoke(prompt)
# print(response.content)

# =============chaining==============================

# llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# email_template = ChatPromptTemplate.from_template(
#     "generate a {tone} email to {company} about how you can use your {skills} to add value to them in just 4 lines"
# )


# language_template = ChatPromptTemplate.from_template(
#     "translate the following email into {language}:\n\n{email}"
    
# )

# email_chain = email_template | llm | StrOutputParser() 


# combine_inputs = RunnableMap({
#     "email": lambda x: x["email"],  # Extract the email from the previous step
#     "language": lambda x: x["original_input"]["language"]
# })

# language_chain = language_template | llm | StrOutputParser()

# def prepare_input(input_dict):
#     return {
#         "email": email_chain.invoke(input_dict),
#         "original_input": input_dict  # Preserve the original input for language
#     }


# chain =  prepare_input | combine_inputs | language_chain
# response = chain.invoke({
#     "tone":"professional",
#     "company":"microsoft",
#     "skills":"fullstack ai developer",
#     "language":"latin"
# })
# print(response)


# ===========parallel chaining=============
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