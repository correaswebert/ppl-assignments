(setq mylist '(5 9 1 4 6 7 5 2 4 9 6 7 2))

(print "Please enter an index: ")  
(finish-output)
(setq i (read))

(format t "Element at index ~D -> ~D" i (nth i mylist))