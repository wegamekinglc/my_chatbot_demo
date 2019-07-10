# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from pathlib import Path
import pandas as pd
import numpy as np
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from bert_serving.client import ConcurrentBertClient

bc = ConcurrentBertClient()

def r_square(src, dst):
    error = src - dst
    return 1. - error @ error / (src @ src)

parent_path = Path(__file__).parents[0]
faq = pd.read_csv(parent_path / "data/faq.csv", index_col=0)
category = pd.read_csv(parent_path / "data/category.csv", index_col=0)
embed = pd.read_csv(parent_path / "data/embed.csv", index_col=0)

def convert(x): 
    x = x[2:-2] 
    x = x.split(' ') 
    x = [float(s.strip()) for s in x if s] 
    return np.array(x) 


embed['embed'] = embed['embed'].apply(convert)


class ActionSearchQuestion(Action):

    def name(self) -> Text:
        return "search_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        question = tracker.latest_message['text']
        q_vec = bc.encode([question])[0]

        faq_copy = faq.copy()
        faq_copy.loc[:, 'score'] = [r_square(q_vec, row) for row in embed['embed'].values]
        faq_copy = faq_copy.sort_values('score', ascending=False)
        exact_answer = faq_copy.iloc[0]['answer']

        if faq_copy.iloc[0]['score'] > 0.9:
            return [SlotSet("match_status", "exact"), SlotSet("exact_answer", exact_answer)]
        else:
            return [SlotSet("match_status", "not")]

class ActionExactResp(Action):

    def name(self) -> Text:
        return "exact_resp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(tracker.get_slot('exact_answer'))
        return [SlotSet("match_status", None), SlotSet("exact_answer", None)]


class ActionNotKnown(Action):

    def name(self) -> Text:
        return "not_known"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("这个问题我不知道。。。")

        return [SlotSet("match_status", None), SlotSet("exact_answer", None)]

