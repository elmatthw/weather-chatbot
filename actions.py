from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from weather import Weather
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher: 'Dispatcher', tracker: 'DialogueStateTracker',
            domain: 'Domain'):

        loc = tracker.get_slot('location')
        weather = Weather(loc)

        response = """It is currently {} in {} at the moment. The temperature is {:.1f} degrees Celsius. Humidity is {}%, 
        wind speed is {} meters per second""".format(weather.get_weather(), loc, weather.get_temperature(), weather.get_humidity(), weather.get_wind_speed())
        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

