## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Early leaving
* greet
  - utter_greet
* goodbye
  - utter_ask_why_leaving

## price reaction
* opinion+negative{"price": "expensive"}
  - utter_good_value
  - utter_ask_continue

## simple acknowledgement
* opinion+positive
  - utter_positive_feedback_reaction

## user asks whats possible
* ask_whatspossible
  - utter_explain_whatspossible

## user asks for something out of scope
* out_of_scope
  - utter_cannot_help
  - utter_explain_whatspossible

## rude user
* insult
  - utter_respond_insult
* insult
  - utter_respond_insult2
  - utter_goodbye

## Start Help

* greet
    - utter_greet
* well_being_ask
    - utter_well_being
    - utter_help_you

## Pleasant Intro

* greet
    - utter_pleasant_greet
    - utter_how_are_you
* mood_great
    - utter_good
    - utter_help_you

## Full Convo 1

* greet
    - utter_greet
* mood_great
    - utter_good
    - utter_help_you
* picks
    - utter_picks
* sports
    - utter_sports
* betting_history
    - utter_betting_history
* opinion+positive
    - utter_thanks
    - utter_anything_else
* goodbye
    - utter_goodbye

## Fifa 1

* greet
    - utter_greet
* well_being_ask
    - utter_well_being
    - utter_help_you
* fifa
    - utter_fifa
    - utter_sign_up
* affirm
    - utter_form

## Greet with Name

* inform{"name":"Jason"}
    - slot{"name":"Jason"}
    - utter_greet_name
* well_being_ask
    - utter_well_being
    - utter_help_you

## Not helpful

* how_to_help
    - utter_help_you
