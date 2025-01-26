# Can AI build a 2025 budget for France ?

Ask LLM to come up with a 2025 budget for France.

## Results

Results can be found in the [this folder](budget/output). The results are broken down in two files:
- `comission_proposals.md`: two detailed proposals for 2025 budget from the AI agent representing the [Comission des finances](https://www.assemblee-nationale.fr/dyn/17/organes/commissions-permanentes/finances). Cost reduction are **broken down by ministries in a table**, a **focus on taxes** per socio-professional class is detailed in a paragraph.
- `prime_minister_decision.md`: the adopted proposal by the French Prime Minister between these two proposals of the comission. Detailed reasons of the choice can be found here

## But why is it hard for France to find such a budget ?

Let's ask AI:

`ollama run llama3.2 "Why is it hard for France to come up with a budget for 2025 ? Answer in two sentences"`

> [!TIP]
> The French government's inability to present a comprehensive budget for 2025 can be attributed to the ongoing debates over pension reform, unemployment benefits, and economic growth strategies that have hindered consensus among parties.
> 
> The country's complex web of social welfare programs, labor laws, and regional disparities also contribute to the difficulty in crafting a unified and realistic budget for 2025.

Here is an extended answer

`ollama run llama3.2 "Why is it hard for France to come up with a budget for 2025 ?"`


> [!TIP]
> The French government has been facing significant challenges in creating a budget for 2025, and there are several reasons contributing to this difficulty. 
Here are some of the key factors:
> 
> 1. **Rising costs**: The French economy is experiencing high inflation, which has led to increased costs for essential goods and services, such as energy, food, and healthcare.
> 2. **Social unrest**: France has been facing ongoing protests and strikes by various groups, including teachers, healthcare workers, and pensioners, demanding better wages, working conditions, and benefits.
> 3. **Pension reform**: The French government is struggling to implement a pension reform that would address the country's aging population and rising retirement costs. The proposed reforms have sparked intense opposition from labor unions and many citizens.
> 4. **Environmental concerns**: France has set ambitious climate change goals, including reducing greenhouse gas emissions by 55% by 2030. Implementing these measures will require significant investments in renewable energy, transportation, and infrastructure, which adds to the budget burden.
> 5. **Coronavirus pandemic legacy**: The COVID-19 pandemic had a significant impact on France's economy, leading to increased healthcare costs, labor market challenges, and economic disruption. The government is still dealing with the consequences of this crisis.
> 6. **Fiscal constraints**: The French government faces fiscal constraints due to high levels of public debt (over 100% of GDP) and limited room for maneuver in terms of taxation and spending reductions.
> 7. **Electoral considerations**: The upcoming presidential election in April 2022 has created uncertainty about the government's priorities and policies, making it challenging to agree on a budget that meets both short-term fiscal needs and long-term strategic objectives.
> 
> These factors have contributed to the French government's difficulty in creating a budget for 2025. The current government is trying to balance competing demands and interests, while also addressing pressing economic and social challenges.

## Usage

```sh
cd budget
# Start the crew work
make run
```
