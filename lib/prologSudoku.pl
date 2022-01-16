:- use_module(library(clpfd)).
 
num(1).
num(2).
num(3).
num(4).
num(5).
num(6).
num(7).
num(8).
num(9).

dom([]).
dom([N|Ns]) :-	num(N), dom(Ns).

domain([]).
domain([Row|Rows]) :- dom(Row), domain(Rows).

blocks([], [], []).
blocks([N1,N2,N3|Ns1], [N4,N5,N6|Ns2], [N7,N8,N9|Ns3]) :-
    all_distinct([N1,N2,N3,N4,N5,N6,N7,N8,N9]),
    blocks(Ns1, Ns2, Ns3).
 
diagonalsA([N1|_], [_,N2|_], [_,_,N3|_], [_,_,_,N4|_], [_,_,_,_,N5|_], [_,_,_,_,_,N6|_], [_,_,_,_,_,_,N7|_], [_,_,_,_,_,_,_,N8|_], [_,_,_,_,_,_,_,_,N9]) :-
    all_distinct([N1,N2,N3,N4,N5,N6,N7,N8,N9]).
diagonalsB([_,_,_,_,_,_,_,_,N9], [_,_,_,_,_,_,_,N8|_], [_,_,_,_,_,_,N7|_], [_,_,_,_,_,N6|_], [_,_,_,_,N5|_], [_,_,_,N4|_], [_,_,N3|_], [_,N2|_], [N1|_]) :-
    all_distinct([N1,N2,N3,N4,N5,N6,N7,N8,N9]).

win([_,A1,A2,A3,_,D1,D2,D3,_],[_,B1,B2,B3,_,E1,E2,E3,_],[_,C1,C2,C3,_,F1,F2,F3,_]) :-
    all_distinct([A1,A2,A3,B1,B2,B3,C1,C2,C3]),
    all_distinct([D1,D2,D3,E1,E2,E3,F1,F2,F3]).
    
sudoku(SOL, Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),
    append(Rows, X), X ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [A,B,C,D,E,F,G,H,I],
    blocks(A, B, C),
    blocks(D, E, F),
    blocks(G, H, I),
    domain(Rows),
    SOL = Rows.
    
sudoku_diagonal(SOL, Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),
    append(Rows, X), X ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [A,B,C,D,E,F,G,H,I],
    blocks(A, B, C),
    blocks(D, E, F),
    blocks(G, H, I),
    diagonalsA(A,B,C,D,E,F,G,H,I),
    diagonalsB(A,B,C,D,E,F,G,H,I),
    domain(Rows),
    SOL = Rows.

sudoku_win(SOL, Rows) :-
    length(Rows, 9),
    maplist(same_length(Rows), Rows),
    append(Rows, X), X ins 1..9,
    maplist(all_distinct, Rows),
    transpose(Rows, Columns),
    maplist(all_distinct, Columns),
    Rows = [A,B,C,D,E,F,G,H,I],
    blocks(A, B, C),
    blocks(D, E, F),
    blocks(G, H, I),
    win(B, C, D),
    win(F, G, I),
    domain(Rows),
    SOL = Rows.