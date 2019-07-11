## greet path
* greet
  - utter_greet
> check_greet

## goodbye path
* goodbye
  - utter_goodbye
> check_goodby

## ask path1
* ask_question
  - search_question
  - slot{"match_status": "exact"}
  - exact_resp
  - slot{"match_status": null}
> check_asked_question_success

## ask path2
* ask_question
  - search_question
  - slot{"match_status": "not"}
  - not_known
  - slot{"match_status": null}
> check_asked_question_fail

## path1
> check_greet
> check_goodby

## path2
> check_greet
> check_asked_question_success
> check_goodby

## path3
> check_greet
> check_asked_question_fail
> check_goodby

## path4
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_goodby

## path5
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_goodby

## path6
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_goodby

## path7
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_goodby

## path8
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_asked_question_success
> check_goodby

## path9
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_asked_question_success
> check_goodby

## path10
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_asked_question_success
> check_goodby

## path11
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_asked_question_success
> check_goodby

## path12
> check_greet
> check_asked_question_success
> check_asked_question_fail
> check_asked_question_fail
> check_goodby

## path13
> check_greet
> check_asked_question_fail
> check_asked_question_success
> check_asked_question_fail
> check_goodby

## path14
> check_greet
> check_asked_question_success
> check_asked_question_success
> check_asked_question_fail
> check_goodby

## path15
> check_greet
> check_asked_question_fail
> check_asked_question_fail
> check_asked_question_fail
> check_goodby

## fallback story
* not_understand
  - action_default_fallback