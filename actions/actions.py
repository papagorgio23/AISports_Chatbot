# This files contains your custom actions which can be used to run
# custom Python code.

from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class PicksForm(FormAction):
    """Collect information to sign up with A.I. Sports"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "picks_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""


        if tracker.get_slot('age') != 'Over':
            return ["name", "age", "email", "betsize", "betlength", "parents"]
        else:
            return ["name", "age", "email", "betsize", "betlength"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""

    return {
        "age": [
            self.from_entity(entity="age"),
            self.from_intent(intent="affirm", value="Yes"),
            self.from_intent(intent="deny", value="No"),
        ],
        "parents": [
            self.from_entity(entity="parents"),
            self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False),
        ],
    }
        
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "action_chitchat"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_weather', 'ask_howdoing',
                      'ask_howold', 'ask_languagesbot', 'ask_restaurant',
                      'ask_time', 'ask_wherefrom', 'ask_whoami',
                      'handleinsult', 'telljoke', 'ask_whatismyname']:
            dispatcher.utter_template('utter_' + intent, tracker)

        return []
