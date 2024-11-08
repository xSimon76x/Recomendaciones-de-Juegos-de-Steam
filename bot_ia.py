import os
from langchain_openai import OpenAI,ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain.memory import SimpleMemory
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from models import JuegosRecomendados

def bot_chat(user_input, history):

    model = os.environ["OPENAI_MODEL"]
    api_key = os.environ["OPENAI_API_KEY"]
    llmModel = ChatOpenAI(model=model, api_key=api_key)

    response_schemas = [
        ResponseSchema(name="respuesta", description="responder la pregunta del usuario"),
        ResponseSchema(
            name="source",
            description="source used to answer the user's question, should be a website.",
        ),
    ]
    
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    
    prompt  = PromptTemplate(
        template="answer the users question as best as possible.\n{format_instructions}\n{pregunta}",
        input_variables=['pregunta'],
        partial_variables={"format_instructions": format_instructions},
    )


    json_chain = prompt  | llmModel | output_parser

    response = json_chain.invoke({"pregunta": "Necesito que me digas cual juego me recomiendas jugar, que sea de acción, basandote en las siguientes opciones: "+user_input})

    if response and 'respuesta' in response:

        history.add_user_message(response['respuesta'])


        print(history)


    # Realiza la consulta al modelo
    # response = chatbot(formatted_input)
    
    # Almacena la nueva entrada en la memoria
    # response = memory.save_memory(user_input)

    return response
