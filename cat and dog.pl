dog(fido).
dog(rover).
dog(jane).
dog(tom).
dog(fred).
dog(henry).
dog(fido).
cat(mary).
cat(harry).
cat(bill).
cat(steve).

small(henry).

medium(harry).
medium(fred).

large(fido).
large(mary).
large(tom).
large(fred).
large(steve).
large(jim).
large(mike).

small_animal(X):- dog(X),small(X).
small_animal(Z):- cat(Z),small(Z).

medium_animal(X):- dog(X),medium(X).
medium_animal(Z):- cat(Z),medium(Z).

large_animal(X):- dog(X),large(X).
large_animal(Z):- cat(Z),large(Z).

INPUT/OUTPUT
?- medium(X).
