from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from weather import Weather
from location_exception import NoLocationRecognized
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level='INFO')


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher: 'Dispatcher', tracker: 'DialogueStateTracker',
            domain: 'Domain'):

        try:
            loc = tracker.get_slot('location')
            weather = Weather(loc)

            response = """It is currently {} in {} at the moment. The temperature is {:.1f} degrees Celsius. 
                    Humidity is {}%, wind speed is {} meters per second\n""".format(weather.get_weather(),
                                                                                  loc.capitalize(),
                                                                                  weather.get_temperature(),
                                                                                  weather.get_humidity(),
                                                                                  weather.get_wind_speed())
            dispatcher.utter_message(response)
            return [SlotSet('location', loc)]
        except NoLocationRecognized:
            response = "Didn't get what the location you are asking for"
            dispatcher.utter_message(response)



