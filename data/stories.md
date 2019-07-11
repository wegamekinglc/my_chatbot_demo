## greet checkpoint
* greet
  - utter_greet
> check_greet

## goodbye checkpoint
* goodbye
  - utter_goodbye
> check_goodbye

## god ask checkpoint
* ask_question
  - search_question
  - slot{"match_status": "exact"}
  - exact_resp
  - slot{"match_status": null}
> check_asked_question_success

## bad ask checkpoint
* ask_question
  - search_question
  - slot{"match_status": "not"}
  - not_known
  - slot{"match_status": null}
> check_asked_question_fail

## path1
> check_greet
> check_goodbye

## path2
> check_greet
> check_asked_question_success
> check_goodbye

## path3
> check_greet
> check_asked_question_fail
> check_goodbye

## path4
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_goodbye

## path5
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_goodbye

## path6
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_goodbye

## path7
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_goodbye

## path8
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_asked_question_success
> check_goodbye

## path9
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_asked_question_success
> check_goodbye

## path10
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_asked_question_success
> check_goodbye

## path11
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_asked_question_success
> check_goodbye

## path12
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_asked_question_fail
> check_goodbye

## path13
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_asked_question_fail
> check_goodbye

## path14
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_asked_question_fail
> check_goodbye

## path15
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_asked_question_fail
> check_goodbye

## Greet path
> check_greet

## Goodbye path
> check_goodbye

## Good ask path
> check_asked_question_success

## Bad ask path
> check_asked_question_fail

## fallback story
* not_understand
  - action_default_fallback