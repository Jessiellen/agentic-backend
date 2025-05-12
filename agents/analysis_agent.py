from crewai import Agent
from langchain.llms import Ollama

class AnalysisAgent:
    def __init__(self):
        self.llm = Ollama(model="llama2")

    def create_agent(self):
        return Agent(
            role="Analista de Dados",
            goal="Processar dados e gerar insights",
            verbose=True,
            llm=self.llm
        )