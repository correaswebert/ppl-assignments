;factorial using recursion
(defun factorial_recursion (n)
    (if (= n 1)              
        1                           
        (* n (factorial_recursion (- n 1))))) 

; factorial using for loop
(defun factorial_forloop (n)
    (setq a 1)
    (loop for i from 1 to n
        do (setf a (* a i)))
    a)

(print "Please enter a number: ")  
(finish-output)
(setq x (read))

(print "Using recursion...")
(format t "~D! is ~D" x (factorial_recursion x))
(print "Using for loop... ")
(format t "~D! is ~D" x (factorial_forloop x))
