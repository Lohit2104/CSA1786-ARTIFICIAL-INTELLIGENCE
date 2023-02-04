bird (eagle).
       bird (sparrow).
       bird (penguin).
       fly (penguin) :- !, fail.
       fly(X) :- bird(X).
