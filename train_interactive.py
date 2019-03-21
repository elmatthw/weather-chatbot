from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function
import logging
from rasa_core.agent import Agent
from rasa_core.train import interactive
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def run_weather_online(interpreter,
                       domain_file="weather_domain.yml",
                       training_data_file="data/stories.md"):
    agent = Agent(domain_file, policies=[MemoizationPolicy(max_history=2),
                                         KerasPolicy(max_history=3, epochs=200, batch_size=50)], interpreter=interpreter)
    data = agent.load_data(training_data_file)
    agent.train(data)
    interactive.run_interactive_learning(agent, training_data_file, skip_visualization=True)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level='INFO')
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    run_weather_online(nlu_interpreter)
