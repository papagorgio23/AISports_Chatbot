## Sign up Form
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

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
* handleinsult
  - utter_respond_insult
* handleinsult
  - utter_respond_insult2
  - utter_goodbye

## Start Help

* greet
    - utter_greet
* ask_howdoing
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

* fifa
    - utter_fifa
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## Greet with Name

* inform{"name":"Jason"}
    - slot{"name":"Jason"}
    - utter_greet_name
* ask_howdoing
    - utter_well_being
    - utter_help_you

## Not helpful

* help
    - utter_help_you

## Sign up Form 1

* greet_name
    - utter_pleasant_greet
    - utter_how_are_you
* mood_great
    - utter_good
    - utter_help_you
* ask_howold
    - utter_good
    - utter_help_you
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_languagesbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR telljoke OR ask_whatismyname
    - action_chitchat

## NCAAB 1

* ncaab
    - utter_ncaab
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NCAAF 1

* ncaaf
    - utter_ncaaf
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NBA 1

* nba
    - utter_nba
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NFL 1

* nfl
    - utter_nfl
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## MLB 1

* mlb
    - utter_mlb
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NHL 1

* nhl
    - utter_nhl
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NHL 2

* nhl
    - utter_nhl
    - utter_sign_up
* deny
    - utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NHL 1

* nhl
    - utter_nhl
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## Fifa 2

* fifa
    - utter_fifa
    - utter_sign_up
* deny
    - utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## MLB 2

* mlb
    - utter_mlb
    - utter_sign_up
* deny
	- utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NFL 2

* nfl
    - utter_nfl
    - utter_sign_up
* deny
	- utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NCAAB 2

* ncaab
    - utter_ncaab
    - utter_sign_up
* deny
	- utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NCAAF 2

* ncaaf
    - utter_ncaaf
    - utter_sign_up
* deny
	- utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NBA 2

* nba
    - utter_nba
    - utter_sign_up
* deny
	- utter_signup_2
* affirm
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## NHL sad

* nhl
    - utter_nhl
    - utter_sign_up
* deny
    - utter_signup_2
* deny
	- utter_signup_deny
    - utter_help_you

## NBA sad

* nba
    - utter_nba
    - utter_sign_up
* deny
	- utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## NCAAF sad

* ncaaf
    - utter_ncaaf
    - utter_sign_up
* deny
	- utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## NCAAB sad

* ncaab
    - utter_ncaab
    - utter_sign_up
* deny
	- utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## NFL sad

* nfl
    - utter_nfl
    - utter_sign_up
* deny
	- utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## MLB sad

* mlb
    - utter_mlb
    - utter_sign_up
* deny
	- utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## Fifa sad

* fifa
    - utter_fifa
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_help_you

## Sign up ChitChat
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
* chitchat
    - utter_chitchat
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_help_you

## Sign up Stop
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
* stop
    - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_help_you

## Sign up Stop-Go
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
* stop
    - utter_ask_continue
* affirm
    - picks_form
    - form{"name": null}
    - utter_help_you

## A.I. Sports
* ai_sports
  - utter_ai_sports
