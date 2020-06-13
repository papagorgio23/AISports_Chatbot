## Sign up Form
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou OR affirm
    - utter_anything_else

## Greet with Name
* inform{"name":"Jason"}
    - slot{"name":"Jason"}
    - utter_greet_name
* ask_howdoing
    - utter_ask_howdoing
    - utter_help_you

## How doing
* ask_howdoing
    - utter_ask_howdoing
    - utter_help_you

## Name Greeting
* greet_name
    - utter_greet_name
    - utter_how_are_you
* mood_great
    - utter_happy
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
  - utter_help_you

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_cannot_help
  - utter_ai_sports

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
* opinion+negative
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

## Apologize
* apology
  - utter_ok

## Start Help
* greet
    - utter_greet
* ask_howdoing
    - utter_ask_howdoing
    - utter_help_you

## Pleasant Intro
* greet
    - utter_pleasant_greet
    - utter_how_are_you
* mood_great
    - utter_good
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
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou OR affirm
    - utter_anything_else

## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_languagesbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR telljoke OR ask_whatismyname
    - action_chitchat
    - utter_help_you

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
    - utter_anything_else

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
    - utter_anything_else

## Fifa sad
* fifa
    - utter_fifa
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## NCAAB sad
* ncaab
    - utter_ncaab
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## NCAAF sad
* ncaaf
    - utter_ncaaf
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## NBA sad
* nba
    - utter_nba
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## NFL sad
* nfl
    - utter_nfl
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## MLB sad
* mlb
    - utter_mlb
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## NHL sad
* nhl
    - utter_nhl
    - utter_sign_up
* deny
    - utter_signup_2
* deny
    - utter_signup_deny
    - utter_anything_else

## Sign up ChitChat
* sign_up
    - utter_form
    - picks_form
    - form{"name": "picks_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_languagesbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR telljoke OR ask_whatismyname
    - action_chitchat
    - form{"name": "picks_form"}
    - form{"name": null}
    - utter_slots_values
* thankyou
    - utter_anything_else

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
    - utter_anything_else

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
    - utter_anything_else

## A.I. Sports
* ai_sports
  - utter_ai_sports
  - utter_sign_up

## A.I. Sports 1
* ai_sports
  - utter_ai_sports
* opinion+positive
  - utter_sign_up

## Tools
* tools
  - utter_ai_sports
  - utter_tools
* opinion+positive
  - utter_sign_up

## Invest
* invest
  - utter_invest
  - utter_sign_up

## Picks Positive
* picks
  - utter_ai_sports
  - utter_picks
* opinion+positive
  - utter_sign_up

## Picks Negative
* picks
  - utter_ai_sports
  - utter_picks
* opinion+negative
  - utter_good_value
  - utter_sign_up

## Sports
* sports
  - utter_sports
  - utter_sign_up

## Greet Pups
* greet_name{"name":"Pups"}
    - slot{"name":"Pups"}
    - utter_greet_pups

## Greet Ammon
* greet_name{"name":"Ammon"}
    - slot{"name":"Ammon"}
    - utter_greet_ammon

## Betting Partner 1
* bet_partner
    - utter_bet_partner
    - utter_sign_up
* affirm
    - utter_form
    - picks_form
    - form{"name":"picks_form"}
    - slot{"requested_slot":"name"}

## Betting Partner
* bet_partner
    - utter_bet_partner
    - utter_sign_up
