interpret(true) :- !.
interpret((GoalA,GoalB)) :- !,
interpret(GoalA),
interpret(GoalB).
