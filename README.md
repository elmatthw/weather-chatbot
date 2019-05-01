# Порядок запуска
В одной консоли:
```
python -m rasa_core_sdk.endpoint --actions actions
```
В другой консоли:
```
python -m rasa_core.run --enable_api -d models/dialogue -u models/nlu/default/weathernlu/ --debug -o out.log --cors * --endpoints endpoints.yml
```
В третьей консоли:
```
node code.js
```
