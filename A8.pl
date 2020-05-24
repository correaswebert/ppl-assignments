:-initialization(main).
main :- write('AIRLINE MANAGEMENT SYSTEM').

/* set the mapping of names to codes */
code(1, 'Mumbai').
code(2, 'Delhi').
code(3, 'Kolkata').
code(4, 'Chennai').
code(5, 'Bangalore').
code(6, 'Hyderabad').
code(7, 'Patna').
code(8, 'Jammu').

airline(1, 'Spice Jet').
airline(2, 'Air India').
airline(3, 'Kingfiher').

/* city, airport tax, security delay */
place(1,50,60).
place(2,75,80).
place(3,40,30).
place(4,75,45).
place(5,40,20).
place(6,50,30).
place(7,50,60).
place(8,40,30).

/* from, to, airline, price, duration */
route(1,2,2,500,360).
route(1,2,3,650,420).
route(1,4,1,800,480).
route(1,4,2,900,480).
route(1,4,3,950,540).
route(2,3,1,220,240).
route(3,4,2,100, 60).
route(3,4,1,120, 65).
route(4,5,1,400, 50).
route(4,6,1,500, 60).
route(5,6,1,800,120).
route(7,8,3,350,120).


direct_flight_check(From, To) :-
    /* get the city codes */
    code(A, From),
    code(B, To),

    /* check if route A->B exists */
    route(A,B, Airline_code, Price, Duration),

    /* get airline name */
    airline(Airline_code, Airline),
    
    /* print the details */
    flight_details(From, To, Airline,Price, Duration),
    nl,airport_details(From),
    nl,airport_details(To),
    nl,write('=================================').

connecting_flight_check(From, To) :-
    /* get the city codes */
    code(A, From),
    code(B, To),

    /* check if route A->B exists */
    route(A,X, Airline_code_1, Price_1, Duration_1),
    route(X,B, Airline_code_2, Price_2, Duration_2),

    /* get name of connection */
    code(X, Connect),

    /* get airline name */
    airline(Airline_code_1, Airline_1),
    airline(Airline_code_2, Airline_2),

    nl,write('Connecting flights...'),
    
    /* print the details */
    nl,flight_details(From, Connect, Airline_1,Price_1, Duration_1),
    nl,airport_details(From),
    nl,airport_details(Connect),
    nl,write('---------------------------------'),

    nl,flight_details(Connect, To, Airline_2,Price_2, Duration_2),
    nl,airport_details(Connect),
    nl,airport_details(To),
    nl,write('=================================').

flight(From, To):-
    /* check both ways */
    direct_flight_check(From,To);
    direct_flight_check(To,From);
    connecting_flight_check(From,To);
    connecting_flight_check(To,From).


flight_details(From, To, Airline, Price, Duration) :- 
    nl,write('From:           '),
    write(From),

    nl,write('To:             '),
    write(To),

    nl,write('Airline:        '),
    write(Airline),

    nl,write('Price:          ₹'),
    write(Price),

    nl,write('Duration:       '),
    write(Duration),
    write(' minutes').

airport_details(City):-
    /* get details */
    code(City_code, City),
    place(City_code, AirportTax, SecurityDelay),

    nl,write('City:           '), write(City),
    nl,write('Airport Tax:    ₹'),write(AirportTax),
    nl,write('Security Delay: '), write(SecurityDelay),write(' minutes').
