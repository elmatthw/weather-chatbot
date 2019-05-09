## story 01
* greet
    - utter_greet
    
## story 02
* goodbye
    - utter_goodbye
    
## story 03
* inform
    - utter_ask_location
    
## story 04
* inform
    - action_weather
    
## story 05
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location":"Vilnius"}
    - slot{"location": "Vilnius"}
    - action_weather
## Generated Story 2728064048116389211
* greet
    - utter_greet
* inform{"location": "minsk", "GPE": "Minsk"}
    - slot{"location": "minsk"}
    - action_weather
* goodbye
    - utter_goodbye

## Generated Story 4650793181582508968
* inform{"location": "london", "GPE": "London"}
    - slot{"location": "london"}
    - action_weather
    - slot{"location": "london"}
* goodbye
    - utter_goodbye

## Generated Story -131467750487057889
* greet
    - utter_greet
* inform{"location": "tokio", "ORG": "Tokio"}
    - slot{"location": "tokio"}
    - action_weather
    - slot{"location": "tokio"}
    - action_revert_fallback_events
* goodbye
    - utter_goodbye

