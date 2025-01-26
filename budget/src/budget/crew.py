from datetime import datetime
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task


llm=LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

# Format the date and time
run_timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")


@CrewBase
class Budget():
	"""Budget crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def finance_commission_president(self) -> Agent:
		return Agent(
			config=self.agents_config['finance_commission_president'],
			verbose=True,
			llm=llm
		)

	@agent
	def prime_minister(self) -> Agent:
		return Agent(
			config=self.agents_config['prime_minister'],
			verbose=True,
			llm=llm
		)

	@task
	def comission_proposal(self) -> Task:
		return Task(
			config=self.tasks_config['comission_proposal'],
			output_file="output/"+run_timestamp+'_comission_proposals.md'
		)

	@task
	def decide_and_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['decide_and_report_task'],
			output_file="output/"+run_timestamp+'_prime_minister_decision.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Budget crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
