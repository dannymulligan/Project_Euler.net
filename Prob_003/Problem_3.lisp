;; Problem 3 from http://projecteuler.net
;; 
;; What is the largest prime factor of the number 317584931803?
;;
;; Answer: 3,919
;;  67 * 829 * 1,459 * 3,919 = 317,584,931,803
;;
;; Danny Mulligan
;; 2008-02-05
;;

(defconstant +size+ 1000000)

(defparameter *primes*
  (make-array (1+ +size+) :initial-element t))

(defun primes-sieve-of-eratosthenes ()
  (setf (elt *primes* 0) NIL)		; 0 is not a prime
  (setf (elt *primes* 1) NIL)		; 1 is not a prime

  (loop for i from 2 to (isqrt +size+) do
       (if (elt *primes* i) 
	   (progn (format t "~d " i)
		  (loop for j from 2 to (floor +size+ i) do
		       (setf (elt *primes* (* i j)) NIL)))))

  (loop for i from (1+ (isqrt +size+)) to +size+ do
       (if (elt *primes* i) 
	   (format t "~d " i))))

;;;
;;;
;;;
(defun find-next-factor (number start)
  (do ((i start (1+ i)))
      ((or (>= i +size+) (zerop (mod number i))) (list (truncate number i) i))
      ))
   
;; How to run this program
;;
;; CL-USER> (primes-sieve-of-eratosthenes)
;; 2 3 5 7 11 13 17 ...
;; CL-USER> (find-next-factor 317584931803 2)
;; (4740073609 67)
;; CL-USER> (find-next-factor 4740073609 67)
;; (5717821 829)
;; CL-USER> (find-next-factor 5717821 829)
;; (3919 1459)
;; CL-USER> (find-next-factor 3919 1459)
;; (1 3919)
;;
;; The factors of 317584931803 are therfore...
;;  67, 829, 1459, 3919
;; The solution to the problem is 3919
;;