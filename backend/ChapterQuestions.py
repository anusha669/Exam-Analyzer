
import json 
from pymongo import MongoClient 
myclient = MongoClient("mongodb://localhost:27017/") 
db = myclient["db3"] 
Maths=[
	    {
    	"ChapterName":"Sets",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"The union of the sets {1, 2, 5} and {1, 2, 6} is the set ",
				 "options":["{1, 2, 6, 1}"," {1, 2, 5, 6}","{1, 2, 1, 2}"," {1, 5, 6, 3}"],
				 "answer": [2, "The union of the sets A and B, is the set that contains those elements that are either in A or in B."],
			},
			{	"questionNumber":2,
				"question":"The intersection of the sets {1, 2, 5} and {1, 2, 6} is the set ",
				 "options":["{1, 2}","{5, 6}","{2, 5}","{1, 6}"],
				 "answer": [1, "The intersection of the sets A and B, is the set containing those elements that are in both A and B."],
			},
			{	"questionNumber":3,
				"question":"Which of the following two sets are disjoint? ",
				 "options":["{1, 3, 5} and {1, 3, 6}","{1, 2, 3} and {1, 2, 3}","{1, 3, 5} and {2, 3, 4}"," {1, 3, 5} and {2, 4, 6}"],
				 "answer": [4, "Two sets are disjoint if the intersection of two sets is the empty set."]
			},
			{	"questionNumber":4,
				"question":"The difference of {1, 2, 3} and {1, 2, 5} is the set",
				 "options":["{1}","{5}","{3}","{2}"],
				 "answer": [3, "The difference of the sets A and B denoted by A-B, is the set containing those elements that are in A not in B."]
			},
			{	"questionNumber":5,
				"question":"The complement of the set A is",
				 "options":["A – B","U – A"," A – U","B – A"],
				 "answer": [2, "The complement of the set A is the complement of A with respect to U."]
			},
			{	"questionNumber":6,
				"question":"The bit string for the set {2, 4, 6, 8, 10} (with universal set of natural numbers less than or equal to 10) is",
				 "options":["0101010101","1010101010","1010010101","0010010101"],
				 "answer": [1, "The bit string for the set has a one bit in second, fourth, sixth, eighth, tenth positions, and a zero elsewhere."]
			},
			{	"questionNumber":7,
				"question":"The bit strings for the sets are 1111100000 and 1010101010. The union of these sets is ",
				 "options":["1010100000","1010101101","1111111100","1111101010"],
				 "answer": [4, "The bit string for the union is the bitwise OR of the bit strings"]
			},
			{	"questionNumber":8,
				"question":"The set difference of the set A with null set is",
				 "options":["A"," null","U","B"],
				 "answer": [1, "The set difference of the set A by the null set denoted by A – {null} is A."]
			},
			{	"questionNumber":9,
				"question":"The set O of odd positive integers less than 10 can be expressed by",
				 "options":["{1, 2, 3}","{1, 3, 5, 7, 9}","{1, 2, 5, 9}","{1, 5, 7, 9, 11}"],
				 "answer": [2, " Odd numbers less than 10 is {1, 3, 5, 7, 9}."],
			},
			{	"questionNumber":10,
				"question":"What is the Cartesian product of A = {1, 2} and B = {a, b}?",
				 "options":["{(1, a), (1, b), (2, a), (b, b)}","{(1, 1), (2, 2), (a, a), (b, b)}"," {(1, a), (2, a), (1, b), (2, b)}"," {(1, 1), (a, a), (2, a), (1, b)}"],
				 "answer": [3, "A subset R of the Cartesian product A x B is a relation from the set A to the set B."]
			},
			{	"questionNumber":11,
				"question":"Let the set A is {1, 2, 3} and B is {2, 3, 4}. Then the number of elements in A U B is?",
				 "options":["4","5","6","7"],
				 "answer": [1, "AUB is {1, 2, 3, 4}."]
			},
			{	"questionNumber":12,
				"question":" Let the set A is {1, 2, 3} and B is { 2, 3, 4}. Then number of elements in A ∩ B is?",
				 "options":["1","2","3","4"],
				 "answer": [2, " A ∩ B is {2, 3}."]
			},
			{	"questionNumber":13,
				"question":"Let the set A is {1, 2, 3} and B is {2, 3, 4}. Then the set A – B is?",
				 "options":["{1, -4}","{1, 2, 3}","{1}","{2, 3}"],
				 "answer": [3, "In A – B the common elements get cancelled."]
			},
			{	"questionNumber":14,
				"question":"In which of the following sets A – B is equal to B – A?",
				 "options":[" A = {1, 2, 3}, B = {2, 3, 4}"," A = {1, 2, 3}, B = {1, 2, 3, 4}","A = {1, 2, 3}, B = {2, 3, 1}","A = {1, 2, 3, 4, 5, 6}, B = {2, 3, 4, 5, 1}"],
				 "answer": [3, " A- B= B-A = Empty set."]
			},
			{	"questionNumber":15,
				"question":"Let A be set of all prime numbers, B be the set of all even prime numbers, C be the set of all odd prime numbers, then which of the following is true? ",
				 "options":[" A ≡ B U C","B is a singleton set.","A ≡ C U {2}","All of the mentioned"],
				 "answer": [4, "2 is the only even prime number."]
			},
			{	"questionNumber":16,
				"question":"If A has 4 elements B has 8 elements then the minimum and maximum number of elements in A U B are ",
				 "options":["4, 8"," 8, 12","4, 12","None of the mentioned"],
				 "answer": [2, "Minimum would be when 4 elements are same as in 8, maximum would be when all are distinct."]
			},
			{	"questionNumber":17,
				"question":"If A is {{Φ}, {Φ, {Φ}}}, then the power set of A has how many element?",
				 "options":["2","4","6","8"],
				 "answer": [2, "The set A has got 2 elements so n(P(A))=4."]
			},
			{	"questionNumber":18,
				"question":"Two sets A and B contains a and b elements respectively. If power set of A contains 16 more elements than that of B, value of ‘b’ and ‘a’ are  ",
				 "options":["4, 5","6,7","2,3","None of the mentioned"],
				 "answer": [1, " 32-16=16, hence a=5, b=4."]
			},
			{	"questionNumber":19,
				"question":" Let A be {1, 2, 3, 4}, U be set of all natural numbers, then U-A’(complement of A) is given by set.",
				 "options":["{1, 2, 3, 4, 5, 6, ….}","{5, 6, 7, 8, 9, ……}"," {1, 2, 3, 4}","All of the mentioned"],
				 "answer": [3, "U – A’ ≡ A."]
			},
			{	"questionNumber":20,
				"question":"Which sets are not empty?",
				 "options":["{x: x is a even prime greater than 3}","{x : x is a multiple of 2 and is odd}","{x: x is an even number and x+3 is even}"," { x: x is a prime number less than 5 and is odd}"],
				 "answer": [4, "Because the set is {3}."]
			}
		]
        },
	   {
    	"ChapterName":"Relations and Functions",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"The binary relation {(1,1), (2,1), (2,2), (2,3), (2,4), (3,1), (3,2)} on the set {1, 2, 3} is ",
				 "options":["reflective, symmetric and transitive","irreflexive, symmetric and transitive","neither reflective, nor irreflexive but transitive","irreflexive and antisymmetric"],
				 "answer": [3, "Not reflexive -> (3,3) not present; not irreflexive -> (1, 1) is present; not symmetric -> (2, 1) is present but not (1, 2); not antisymmetric – (2, 3) and (3, 2) are present; not asymmetric -> asymmetry requires both antisymmetry and irreflexivity. So, it is transitive closure of relation."]
			},
			{	"questionNumber":2,
				"question":"Consider the relation: R’ (x, y) if and only if x, y>0 over the set of non-zero rational numbers,then R’ is ",
				 "options":["not equivalence relation","an equivalence relation","transitive and asymmetry relation","reflexive and antisymmetric relation"],
				 "answer": [2, "Reflexive: a, a>0 ,Symmetric: if a, b>0 then both must be +ve or -ve, which means b, a > 0 also exists,Transitive: if a, b>0 and b, c>0 then to have b as same number, both pairs must be +ve or -ve which implies a, c>0. Hence, R’ is an equivalence relation."]
			},
			{	"questionNumber":3,
				"question":"Let S be a set of n>0 elements. Let be the number Br of binary relations on S and let Bf be the number of functions from S to S. The expression for Br and Bf, in terms of n should be  ",
				 "options":[" n^2 and 2(n+1)^2"," n^3 and n^(n+1)","n and n^(n+6)","2^(n*n) and n^n"],
				 "answer": [4, "For a set with n elements the number of binary relations should be 2^(n*n) and the number of functions should be n^n. Hence Br = 2^(n*n) and Bf = n^n."]
			},
			{	"questionNumber":4,
				"question":" Let A be a set of k (k>0) elements. Which is larger between the number of binary relations (say, Nr) on A and the number of functions (say, Nf) from A to A?  ",
				 "options":["number of relations","number of functions"," the element set"," number of subsets of the relation"],
				 "answer": [1, "For a set with k elements the number of binary relations should be 2^(n*n) and the number of functions should be nn. Now, 2^(n*n) => n^2log (2) [taking log] and n^n => n^log (n) [taking log]. It is known that n^2log (2) > n^log (n). Hence, the number of binary relations > the number of functions i.e, Nr > Nf."]
			},
			{	"questionNumber":5,
				"question":"Consider the binary relation, A = {(a,b) | b = a – 1 and a, b belong to {1, 2, 3}}. The reflexive transitive closure of A is? ",
				 "options":["{(a,b) | a >= b and a, b belong to {1, 2, 3}}","{(a,b) | a > b and a, b belong to {1, 2, 3}}"," {(a,b) | a <= b and a, b belong to {1, 2, 3}}","{(a,b) | a = b and a, b belong to {1, 2, 3}}"],
				 "answer": [1, "By definition of Transitive closure we have that a is related to all smaller b (as every a is related to b – 1) and from the reflexive property a is related to a."]
			},
			{	"questionNumber":6,
				"question":"The time complexity of computing the transitive closure of a binary relation on a set of n elements should be ",
				 "options":["O(n)","O(logn)","O(n^(n+(3/2)))","O(n3)"],
				 "answer": [4, "Calculation of transitive closure results into matrix multiplication. We can do matrix multiplication in O(n3) time. There are better algorithms that do less than cubic time."]
			},
			{	"questionNumber":7,
				"question":" Let A and B be two non-empty relations on a set S. Which of the following statements is false? ",
				 "options":["A and B are transitive ⇒ A∩B is transitive","A and B are symmetric ⇒ A∪B is symmetric","A and B are transitive ⇒ A∪B is not transitive","A and B are reflexive ⇒ A∩B is reflexive"],
				 "answer": [3, "In terms of set theory, the binary relation R defined on the set X is a transitive relation if, for all a, b, c ∈ X, if aRb and bRc, then aRc. If there are two relations on a set satisfying transitive property then there union must satisfy transitive property. "]
			},
			{	"questionNumber":8,
				"question":"Determine the characteristics of the relation aRb if a2 = b2. ",
				 "options":["Transitive and symmetric"," Reflexive and asymmetry","Trichotomy, antisymmetry, and irreflexive"," Symmetric, Reflexive, and transitive"],
				 "answer": [4, " Since, x^2 = y^2 is just a special case of equality, so all properties that apply to x = y also apply to this case. Hence, the relation satisfies symmetric, reflexive and transitive closure."]
			},
			{	"questionNumber":9,
				"question":"Let R be a relation between A and B. R is asymmetric if and only if  ",
				 "options":[" Intersection of D(A) and R is empty, where D(A) represents diagonal of set","R-1 is a subset of R, where R-1 represents inverse of R","intersection of R and R-1 is D(A)","D(A) is a subset of R, where D(A) represents diagonal of set"],
				 "answer": [1, " A relation is asymmetric if and only if it is both antisymmetric and irreflexive. As a consequence, a relation is transitive and asymmetric if and only if it is a strict partial order. If D(A) is a diagonal of A set and intersection of D(A) and R is empty, then R is asymmetric."]
			},
			{	"questionNumber":10,
				"question":"R is a binary relation on a set S and R is reflexive if and only if",
				 "options":["r(R) = R","s(R) = R","t(R) = R","f(R) = R"],
				 "answer": [1, " Let reflexive closure of R:r(R) = R. If R is reflexive, it satisfies all the condition in the definition of reflexive closure. So, a reflexive closure of a relation is the smallest number of reflexive relation contain in R. Hence, R = r(R)."]
			},
			{	"questionNumber":11,
				"question":"The condition for a binary relation to be symmetric is ",
				 "options":["s(R) = R","R ∪ R = R","R = R^c","f(R) = R"],
				 "answer": [3, "If <a,b> ∈ R then <b,a> ∈ R, where a and b belong to two different sets and so its symmetric.Rc also contains <b,a>,Rc = R."]
			},
			{	"questionNumber":12,
				"question":"number of reflexive closure exists in a relation R = {(0,1), (1,1), (1,3), (2,1), (2,2), (3,0)} where {0, 1, 2, 3} ∈ A ",
				 "options":["2^6","6","8","36"],
				 "answer": [2, " The reflexive closure of R is the relation, R ∪ Δ = { (a,b) | (a,b) R (a,a) | a A }. Hence, R ∪ Δ = {(0,1), (1,1), (1,3), (2,1), (2,2), (3,0)} and the answer is 6 "]
			},
			{	"questionNumber":13,
				"question":"The transitive closure of the relation {(0,1), (1,2), (2,2), (3,4), (5,3), (5,4)} on the set {1, 2, 3, 4, 5} is ",
				 "options":["{(0,1), (1,2), (2,2), (3,4)} ","{(0,0), (1,1), (2,2), (3,3), (4,4), (5,5)}","{(0,1), (1,1), (2,2), (5,3), (5,4)}","{(0,1), (0,2), (1,2), (2,2), (3,4), (5,3), (5,4)}"],
				 "answer": [4, "Let R be a relation on a set A. The connectivity relation on R* consists of pairs (a,b) such that there is a path of length at least one from a to b in R. Mathematically, R* = R1 ∪ R2 ∪ R3 ∪ … ∪ Rn. Hence the answer is {(0,1), (0,2), (1,2), (2,2), (3,4), (5,3), (5,4)}."]
			},
			{	"questionNumber":14,
				"question":"Amongst the properties {reflexivity, symmetry, antisymmetry, transitivity} the relation R={(a,b) ∈ N2 | a!= b} satisfies   ",
				 "options":["symmetry","transitivity","antisymmetry","reflexivity"],
				 "answer": [1, "It is not reflexive as aRa is not possible. It is symmetric as if aRb then bRa. It is not antisymmetric as aRb and bRa are possible and we can have a!=b. It is not transitive as if aRb and bRc then aRc need not be true. This is violated when c=a. So the answer is symmetry property."]
			},
			{	"questionNumber":15,
				"question":"The number of equivalence relations of the set {3, 6, 9, 12, 18} is ",
				 "options":["4","2^5","22","90"],
				 "answer": [1, "Number of equivalence Relations are given by BELL number. The nth of these numbers i.e, Bn counts the number of different ways to partition a set that has exactly n elements, or equivalently, the number of equivalence relations on it. Let’s say, 1 -> Equivalence relation with 1 element; 1 2 -> Equivalence relation with 2 element; 2 3 5 -> Equivalence relation with 3 element; 5 7 10 15 -> Equivalence relation with 4 element. Hence, the answer is 4."]
			},
			{	"questionNumber":16,
				"question":"Let R1 and R2 be two equivalence relations on a set. Is R1 ∪ R2 an equivalence relation? ",
				 "options":["an equivalence relation","reflexive closure of relation","not an equivalence relation","partial equivalence relation"],
				 "answer": [1, "R1 union R2 is not equivalence relation because transitivity property of closure need not hold. For instance, (x, y) can be in R1 and (y, z) be in R2 and (x, z) not in either R1 or R2. However, R1 intersection R2 is an equivalence relation."]
			},
			{	"questionNumber":17,
				"question":"A relation R is defined on the set of integers as aRb if and only if a+b is even and R is termed as",
				 "options":["an equivalence relation with one equivalence class","an equivalence relation with two equivalence classes","an equivalence relation","an equivalence relation with three equivalence classes"],
				 "answer": [2, "R is reflexive as (a+b) is even for any integer; R is symmetric as if (a+b) is even (b+a) is also even; R is transitive as if ((a+b)+c) is even, then (a+(b+c)) is also even.So, R is an equivalence relation. For set of natural numbers, sum of even numbers always give even, sum of odd numbers always give even and sum of any even and any odd number always give odd. So, must have two equivalence classes -> one for even and one for odd.{…, -4, -2, 0, 2, … } and {…, -3, -1, 1, 3, … }."]
			},
			{	"questionNumber":18,
				"question":"The binary relation U = Φ (empty set) on a set A = {11, 23, 35} is  ",
				 "options":["Neither reflexive nor symmetric","Symmetric and reflexive","Transitive and reflexive","Transitive and symmetric"],
				 "answer": [4, "U = Φ (empty set) on a set A = {11, 23, 35} need to be hold Irreflexive, symmetric, anti-symmetric, asymmetric and transitive closure property, but it is not Reflexive as it does not contain any self loop in itself."]
			},
			{	"questionNumber":19,
				"question":"Suppose S is a finite set with 7 elements. How many elements are there in the largest equivalence relation on S? ",
				 "options":["56","78","49","100"],
				 "answer": [3, " Let R is an equivalence relation on the set S and so it satisfies the reflexive, symmetric and transitive property. The largest equivalence relation means it should contain the largest number of ordered pairs. Since we can have n2 ordered pairs in R x R where n belongs to S and all these ordered pairs are present in this relation; its the largest equivalence relation.So there are n2 elements i.e 72 = 49 elements in the largest equivalence relation."]
			},
			{	"questionNumber":20,
				"question":"The rank of smallest equivalence relation on a set with 12 distinct elements is ",
				 "options":["12","144","136","79"],
				 "answer": [1, "In the case of smallest equivalence relation, each element is in one equivalence class like {a1}, {a2}, … are equivalence classes. So, the rank or number of equivalence classes is n for a set with n elements and so the answer is 12."]
			}
		]
        },
		{
    	"ChapterName":"Trignometric Functions",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"If sin x=0 then x =  ",
				 "options":["nπ","(2n+1) π/2","(n+1) π"," nπ/2"],
				 "answer": [1,"When know, sin x =0 whenever x is 0, π, 2π, 3π,….. i.e. all integral multiples of π so, x=nπ when sin x=0."]
			},
			{	"questionNumber":2,
				"question":"If cos x=0 then x =   ",
				 "options":["nπ","(2n+1) π/2","(n+1) π","nπ/2"],
				 "answer": [2," When know, cos x =0 whenever x is π/2, 3π/2, 5π/2, ………… i.e. all odd integral multiples of π/2so, x=(2n+1) π/2 when cos x=0."]
			},
			{	"questionNumber":3,
				"question":"If tan x = 0 then x =  ",
				 "options":["nπ","(2n+1) π/2","(n+1) π","nπ/2"],
				 "answer": [1, "We know, tan x = sin x / cos x. So, tan x will be zero wherever sin x is zero except the points where cos x is also zero. We know there is no point where sin x as well as cos x both are zero. So, tan x = 0 => x=nπ."]
			},
			{	"questionNumber":4,
				"question":"1-sin245° = ",
				 "options":["1/2","1","0","√3 /2"],
				 "answer": [1, "We know, sin245° + cos245°=1,So, 1- sin245° = cos245° = (1/√2)2 = 1/2."]
			},
			{	"questionNumber":5,
				"question":"1-cos^2x=",
				 "options":["sin x","cos x","sin 2x","sin^2^x"],
				 "answer": [4," We know, sin^2^x+ cos^2^x=1,So, 1-cos^2^x=sin^2^x."]
			},
			{	"questionNumber":6,
				"question":"1-sec^2x=",
				 "options":["cot^2x"," tan^2x","-tan^2x","-cot^2x"],
				 "answer": [3, "We know, sec2x – tan2x=1.So, 1-sec2x=-tan2x."]
			},
			{	"questionNumber":7,
				"question":"1+ tan2x=",
				 "options":["sec2x","-sec^2x","cosec^2x","-cosec^2x"],
				 "answer": [1, "We know, sec^2x – tan^2x=1.So, 1+ tan^2x=sec^2x."]
			},
			{	"questionNumber":8,
				"question":"cot^2x – cosec^2x = ",
				 "options":["1","-1","sin^2x","cos^2x"],
				 "answer": [2, "We know, cosec^2x – cot^2x = 1.So, cot^2x – cosec^2x = -1."]
			},
			{	"questionNumber":9,
				"question":"cosec^2x – 1=",
				 "options":["cot^2x","-cot^2x","tan^2x"," -tan^2x"],
				 "answer": [1, "We know, cosec^2x – cot^2x = 1.So, cosec^2x – 1 = cot^2x."]
			},
			{	"questionNumber":10,
				"question":" tan x is not defined for  ",
				 "options":["0","nπ/2","(2n+1) π/2","nπ"],
				 "answer": [3, "We know, tan x is not defined when cos x = 0.cos x = 0 whenever x is π/2, 3π/2, 5π/2, ………… i.e. all odd integral multiples of π/2.so, x=(2n+1) π/2."]
			},
			{	"questionNumber":11,
				"question":"sin (-45°) =  ",
				 "options":["1","-1","1/√2","-1/√2"],
				 "answer": [4, "We know, sin(-x) = sin x.So, sin (-45°) = -sin 45° = -1/√2."]
			},
			{	"questionNumber":12,
				"question":"cos (-60°) = ",
				 "options":["-√3/2","1/2","√3/2","-1/2"],
				 "answer": [2, " We know, cos (-x) = cos x.So, cos(-60°) = cos 60°=1/2."]
			},
			{	"questionNumber":13,
				"question":"If the initial side is overlapping on the terminal side, then angle is  ",
				 "options":["0°","180°","90°","360°"],
				 "answer": [1, "The angle is formed if we start to rotate from initial side till terminal side comes. If they both overlap then angle is said to be 0°."]
			},
			{	"questionNumber":14,
				"question":"If we start to rotate and after completing one revolution again initial side overlap with terminal side, then the angle formed is  ",
				 "options":["0°","180°","90°","360°"],
				 "answer": [4, "The angle is formed if we start to rotate from initial side till terminal side comes. If we start to rotate and after completing one revolution again initial side overlap with terminal side, then the angle formed is 360°."]
			},
            {	"questionNumber":15,
				"question":"1 radian is   ",
				 "options":["54°48’","57°16’","180°","17°46’"],
				 "answer": [2, "We know, π radian = 180 degree,1 radian = 180/π degree = 57.27° = 57° (0.27*60)’ = 57°16’. "]
			},
			{	"questionNumber":16,
				"question":"4 radians  ",
				 "options":[" 720°","240°51’53”","229°10’59”"," 233°11’48”"],
				 "answer": [3, "We know, π radians = 180 degrees,1 radian = 180/π degrees,4 radians = 720/π degrees = 229.183° = 229° (0.183*60)’ = 229 (10.98)’ = 229°10’59”."]
			},
			{	"questionNumber":17,
				"question":"If angle of arc is 60° and the length of arc is 20 cm. Find the radius of the circle from which arc is intercepted.  ",
				 "options":["18.08 cm","17.07 cm"," 19.09 cm","18 cm"],
				 "answer": [3, "180 degree = π radian,1 degree = π/180 radians,60 degrees = 60* π/180 radians = π/3 radians,Angle=Arc length/Radius,π/3 = 20/Radius => Radius = 60/π = 19.09 cm."]
			},
			{	"questionNumber":18,
				"question":"If length of arc is 40 cm and radius of circle of arc is 10 cm then find the angle made by the arc.  ",
				 "options":["720°","240°51’53”","229°10’59”","233°11’48”"],
				 "answer": [3, " We know, Angle=Arc length/Radius,Angle = 40/10 = 4 radians,π radians = 180 degrees,1 radian = 180/π degrees,4 radians = 720/π degrees = 229.183° = 229° (0.183*60)’ = 229°(10.98)’= 229°10’59”."]
			},
			{	"questionNumber":19,
				"question":"The second hand of the watch is 2 cm long. How far the tip will move in 40 seconds?  ",
				 "options":[" 6.28 cm","12.56 cm","3.14 cm","1.57 cm"],
				 "answer": [2, " Radius of circle=2 cm,In 60 seconds, angle covered by second hand is 360°,In 40 seconds, angle covered by second hand is 360°*4/6 = 240°,240°=240*Angle=Arc length/Radius,240*π/180 = Arc length/2,Arc length=8 π/3 = 12.56 cm."]
			},
			{	"questionNumber":20,
				"question":"If in two circles, arcs of the same length subtend angles 45° and 60° at Centre, find the ratio of their radii.  ",
				 "options":["2:3","2:5","3:4","4:3"],
				 "answer": [4, " Given θ1=45° and θ2=60°, L1=L2,We know, θ = l/r,r1 θ1 = r2 θ2,r1/r2=60/45=4/3.So, radii are in ratio 4:3."]
			}

		]
        },
		{
    	"ChapterName":"Complex Numbers and Quadratic Equations",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"Value of i(iota) is  ",
				 "options":[" -1","1","(-1)^1/2"," (-1)^1/4"],
				 "answer": [3, " Iota is used to denote complex number.The value of i (iota) is −1−−−√ i.e. (-1)1/2."]
			},
			{	"questionNumber":2,
				"question":"In z=4+i, what is the real part?  ",
				 "options":["4","i","1","4+i"],
				 "answer": [1, "In z=a+bi, a is real part and b is imaginary part.,So, in 4+i, real part is 4."]
			},
			{	"questionNumber":3,
				"question":" In z=4+i, what is imaginary part?  ",
				 "options":["4","i","1","4+i"],
				 "answer": [3, "In z=a+bi, a is real part and b is imaginary part.,So, in 4+i, imaginary part is 1."]
			},
			{	"questionNumber":4,
				"question":"(x+3) + i(y-2) = 5+i2, find the values of x and y.  ",
				 "options":["x=8 and y=4","x=2 and y=4","x=2 and y=0"," x=8 and y=0"],
				 "answer": [2, " If two complex numbers are equal, then corresponding parts are equal i.e. real parts of both are equal and imaginary parts of both are equal."]
			},
			{	"questionNumber":5,
				"question":"If z1 = 2+3i and z2 = 5+2i, then find sum of two complex numbers.  ",
				 "options":[" 4+8i","3-i","7+5i","7-5i"],
				 "answer": [3, "In addition of two complex numbers, corresponding parts of two complex numbers are added i.e. real parts of both are added and imaginary parts of both are added.So, sum = (2+5) + (3+2) i = 7+5i."]
			},
			{	"questionNumber":6,
				"question":" If z1 = 2+3i and z2 = 5+2i, then find z1-z2.  ",
				 "options":["-3+1i","3-i"," 7+5i","7-5i"],
				 "answer": [1, " In subtracting one complex number from other, difference of corresponding parts of two complex numbers is calculated. So, z1-z2 = (2-5) + (3-2) i = -3+1i."]
			},
			{	"questionNumber":7,
				"question":"z1=1+2i and z2=2+3i. Find z1z2.  ",
				 "options":["2+6i","-4+0i","-4+7i","8+7i"],
				 "answer": [3, "z1z2 = (1+2i) (2+3i)= 2 + 3i + 4i -6= -4 + 7i."]
			},
			{	"questionNumber":8,
				"question":" i^2 = ",
				 "options":["1","-1","i","-1"],
				 "answer": [2, " We know, i = −1−−−√=> i2 = -1."]
			},
			{	"questionNumber":9,
				"question":" i^7 =  ",
				 "options":["1","-1","i","-1"],
				 "answer": [4,"We know, i = −1−−−√=> i2 = -1 => i4 = 1.So, i7 = i4.i3 = 1*i2*i = (-1)*i = -i."]
			},
			{	"questionNumber":10,
				"question":"i^241=  ",
				 "options":["1","-1","i","-1"],
				 "answer": [3, "i = −1−−−√=> i2 = -1 => i4 = 1.So, i241 = (i4)60 * i = 1 * i = i."]
			},
			{	"questionNumber":11,
				"question":"Square roots of -7 are  ",
				 "options":["7i and -7i","√ 7i","–√7i","√7i and –√7i"],
				 "answer": [4, "We know, i2 = -1.-7 = 7(i2)Square root of i2 is ±i so, square root of -7 are 7–√i and –7–√i."]
			},
			{	"questionNumber":12,
				"question":" (-i) (8+5i) =  ",
				 "options":["8+5i"," -8-5i","-5-8i"," 5-8i"],
				 "answer": [4, "(-i) (8+5i) = -8i – 5 i2= -8i -5(-1) = 5-8i."]
			},
			{	"questionNumber":13,
				"question":" (2-i)^3 =  ",
				 "options":["2-3i","8-i","2-11i","2+11i"],
				 "answer": [3, "We know, (a-b)3 = a3-b3-3ab(a-b),So, (2-i)3 = 23-(i)3-3(2)(i) (2-i)= 8-(-i)-6i(2-i)= 8+i-12i-6= 2-11i."]
			},
			{	"questionNumber":14,
				"question":"Find multiplicative inverse of 3+5i.  ",
				 "options":["87+145i","87-145i","145-87i","145+87i"],
				 "answer": [2, "We know, z*z¯ = |z|2.,(1/z) = z¯|z|2,z-1=(3-5i) (32+52) = (3-5i) (29) = 87-145i."]
			},
			{	"questionNumber":15,
				"question":" i^-35   ",
				 "options":["1","-1","i","-i"],
				 "answer": [3, " We know, i-35= 1/i^35 = i/i^36= i/(i^4)9 = i/1 = i."]
			},
			{	"questionNumber":16,
				"question":"Which axis is known as real axis in argand plane?  ",
				 "options":["x-axis","y-axis","z-axis","any axis"],
				 "answer": [1, "The plane having a complex number assigned to each of its point is called the complex plane or the Argand plane. When (x + y i) is plotted in argand plane, x-axis is real axis."]
			},
			{	"questionNumber":17,
				"question":"Which axis is known as imaginary axis in argand plane?  ",
				 "options":["x-axis","y-axis","z-axis","any axis"],
				 "answer": [2, "The plane having a complex number assigned to each of its point is called the complex plane or the Argand plane. When (x + y i) is plotted in argand plane, y-axis is imaginary axis."]
			},
			{	"questionNumber":18,
				"question":"Find mirror image of point representing x+i y on real axis.  ",
				 "options":["(x, y)","(-x, -y)"," (-x, y)","(x, -y)"],
				 "answer": [4, "Mirror image of point (x, y) on real axis is (x, -y).Since real axis is acting as mirror x-coordinate remains same whereas y-coordinate gets inverted.So, (x, -y) is mirror image of (x, y) on real axis."]
			},
			{	"questionNumber":19,
				"question":"Find mirror image of point representing x+i y on imaginary axis.  ",
				 "options":["(x, y)","(-x, -y)"," (-x, y)","(x, -y)"],
				 "answer": [3, "Mirror image of point (x, y) on imaginary axis is (-x, y).Since imaginary axis is acting as mirror y-coordinate remains same whereas x-coordinate gets inverted. So, (-x, y) is mirror image of (x, y) on imaginary axis."]
			},
			{	"questionNumber":20,
				"question":" If P and Q are conjugate complex numbers then their points on argand plane are mirror image on  ",
				 "options":["x-axis","y-axis","z-axis","any axis"],
				 "answer": [1, "Conjugate complex numbers means their real part is same and imaginary part is inverted i.e. same x part and opposite imaginary part. So, they are mirror image on real axis i.e. x-axis."]
			}
		
		]
        },
		{
    	"ChapterName":"Linear Inequalities",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"7>5 is ",
				 "options":["double inequality"," quadratic inequality","numerical inequality"," linear inequality"],
				 "answer": [3, " Since here numbers are compared with inequality sign so, it is called numerical inequality."]
			},
			{	"questionNumber":2,
				"question":"x>5 is ",
				 "options":["double inequality"," quadratic inequality","numerical inequality"," linear inequality"],
				 "answer": [4, "Since a variable ‘x’ is compared with number ‘5’ with inequality sign so it is called literal inequality."]
			},
			{	"questionNumber":3,
				"question":"ax + b > 0 is ",
				 "options":["double inequality"," quadratic inequality","numerical inequality"," linear inequality"],
				 "answer":[ 4, "Since it has highest power of x ‘1’ and has inequality sign so, it is called linear inequality.It is not numerical inequality as it does not have numbers on both sides of inequality.It does not have two inequality signs so it is not double inequality."]
			},
			{	"questionNumber":4,
				"question":"ax^2+bx+c > 0 is",
				 "options":["double inequality"," quadratic inequality","numerical inequality"," linear inequality"],
				 "answer": [2,"Since it has highest power of x ‘2’ and has inequality sign so, it is called quadratic inequality.It is not numerical inequality as it does not have numbers on both sides of inequality.It does not have two inequality signs so it is not double inequality."]
			},
			{	"questionNumber":5,
				"question":"If Ram has x rupees and he pay 40 rupees to shopkeeper then find range of x if amount of money left with Ram is at least 10 rupees is given by inequation",
				 "options":[" x ≥ 10","x ≤ 10","x ≤ 50","x ≥ 50"],
				 "answer": [4, " Amount left is at least 10 rupees i.e. amount left ≥ 10.x-40 ≥ 10 => x ≥ 50."]
			},
			{	"questionNumber":6,
				"question":"If Ram has x rupees and he pay 40 rupees to shopkeeper then find range of x if amount of money left with Ram is at most 10 rupees is given by inequation",
				 "options":[" x ≥ 10","x ≤ 10","x ≤ 50","x ≥ 50"],
				 "answer": [3, " Amount left is at most 10 rupees i.e. amount left ≤ 10.x-40 ≤ 10 => x ≤ 50."]
			},
			{	"questionNumber":7,
				"question":"If x>7 then which is impossible?",
				 "options":["x>4","x<6","x>9"," x<14"],
				 "answer": [2, " x>7 and 7>4 => x>7>4 => x>4.If x>7 then x cannot be less than 6.If x=11 then x>7 and x>9.If x=11 then x>7 and x<14."]
			},
			{	"questionNumber":8,
				"question":"If x>7 then -x>-7 is ",
				 "options":[" possible"," certainly false"," certainly true","depend on x"],
				 "answer": [2, "If we multiply by negative number on both sides of inequality then sign of inequality will change i.e. if x>7 then (-1) x < (-1)7 => -x<-7."]
			},
			{	"questionNumber":9,
				"question":"If x is a positive integer and 20x<100 then find solution set of x.",
				 "options":["{0,1,2,3,4,5}"," {1,2,3,4,5}","{1,2,3,4}","{0,1,2,3,4}"],
				 "answer": [3, "20x<100,Dividing by 20 on both sides, x< (100/20) => x<5,Since x is a positive integer so x = 1,2,3,4."]
			},
			{	"questionNumber":10,
				"question":"If x is a natural number and 20x≤100 then find solution set of x.",
				 "options":["{0,1,2,3,4,5}"," {1,2,3,4,5}","{1,2,3,4}","{0,1,2,3,4}"],
				 "answer": [2, "20x≤100,Dividing by 20 on both sides, x ≤ (100/20) => x≤5,Since x is a natural number so x = 1,2,3,4,5."]
			},
			{	"questionNumber":11,
				"question":"If x is a whole number and 10x≤50 then find solution set of x.",
				 "options":["{0,1,2,3,4,5}"," {1,2,3,4,5}","{1,2,3,4}","{0,1,2,3,4}"],
				 "answer": [1, "10x≤50,Dividing by 10 on both sides, x ≤ (50/10) => x≤5,Since x is a whole number so x = 0,1,2,3,4,5."]
			},
			{	"questionNumber":12,
				"question":"If 2x+1 > 5 then which is true?",
				 "options":[" x>4"," x>4"," x>2"," x<2"],
				 "answer": [3, " 2x+1>5=>2x>5-1=>2x>4 => x>2."]
			},
			{	"questionNumber":13,
				"question":"If x-1>-x+7 then which is true?",
				 "options":["x>4"," x>4"," x>2"," x<2"],
				 "answer": [1, " x-1>-x+7=>2x>8 => x>4."]
			},
			{	"questionNumber":14,
				"question":"Rahul obtained 20 and 25 marks in first two tests. Find the minimum marks he should get in the third test to have an average of at least 30 marks.",
				 "options":["60","35","180","45"],
				 "answer": [4, "Average is at least 30 marks.Let x be the marks in 3rd test.Average = (20+25+x)/3 ≥30=>45+x≥90 => x≥90-45 => x≥45.Minimum marks in 3rd test should be 45."]
			},
			{	"questionNumber":15,
				"question":"Find all pairs of consecutive odd positive integers both of which are smaller than 8 such that their sum is more than 10",
				 "options":["(5,7)","(3,5), (5,7)"," (3,5), (5,7), (7,9)"," (5,7), (7,9)"],
				 "answer": [1, "Let two numbers be x and x+2.x + x+2 >10 => 2x>8 => x>4and x<8and x+2<8 => x<6.4<x<6 => x can be 5.For x =5, x+2=7,So, Pairs of odd consecutive positive integers are (5,7)."]
			},
			{	"questionNumber":16,
				"question":"The longest side of a triangle is 2 times the shortest side and the third side is 4 cm shorter than the longest side. If the perimeter of the triangle is at least 61 cm, find the minimum length of the shortest side.",
				 "options":["7","9","11","13"],
				 "answer": [4, " Let shortest side be x. Then longest side = 2x.Third side = 2x-4.Given, perimeter of triangle is at least 61 cm=>x+2x+2x-4 ≥ 61 => 5x≥65 = x≥13.Minimum length of the shortest side is 13 cm."]
			},
			{	"questionNumber":17,
				"question":"2x+y>5. Which of the following will satisfy the given equation?",
				 "options":[" (1,1)","(1,2)","(2,1)","(2,2)"],
				 "answer": [4, " 2x+y>5 (1,1) x=1 and y=1 gives 2(1)+1>5 =>3>5 which is false.(1,2) x=1 and y=2 gives 2(1)+2>5 =>4>5 which is false.(2,1) x=2 and y=1 gives 2(2)+1>5 =>5>5 which is false.(2,2) x=2 and y=2 gives 2(2)+2>5 =>6>5 which is true."]
			},
			{	"questionNumber":18,
				"question":"IQ of a person is given by the formula IQ =(MA/CA) × 100, where MA is mental age and CA is chronological age. If 40 ≤ IQ ≤ 120 for a group of 10 years old children, find the range of their mental age.",
				 "options":["(9,16)","[9,16]","(4,12)","[4,12]"],
				 "answer": [4, " IQ =(MA/CA) × 100=>MA = IQ * CA /100. Given, CA=10 years 40≤ IQ ≤120=> 40*CA ≤ IQ*CA ≤ 120*CA=> 40*10 ≤ IQ*CA ≤ 120*10=> 40∗10 100≤IQ∗CA100≤120∗10 100=> 4 ≤ MA ≤ 12."]
			},
			{	"questionNumber":19,
				"question":"A solution is to be kept between 77° F and 86° F. What is the range in temperature in degree Celsius (C) if the Celsius / Fahrenheit (F) conversion formula is given by F = 9/5 C + 32°?",
				 "options":[" [15°, 20°]"," [20°, 25°]","[25°, 30°]","[30°, 35°]"],
				 "answer": [3, "F = 9/5 C + 32°C=(F-32°)*5/9 77° ≤ F ≤ 86°=> 77°-32° ≤ F-32° ≤ 86° -32°=> 45° ≤ F-32° ≤ 54°=>45o*5/9 ≤ (F-32°) *5/9 ≤ 54°*5/9=>25° ≤ C ≤ 30°."]
			},
			{	"questionNumber":20,
				"question":"y<-2 involves region are ",
				 "options":["above dotted line y=-2","below dotted line y=-2","above complete line y=-2","below complete line y=-2"],
				 "answer": [2, " y<-2 does not satisfy (0,0) so, region is below y = -2.Since only inequality sign given, so dotted line y = -2."]
			}
		]
        },
		{
    	"ChapterName":"Permutation and Combination",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"6!=",
				 "options":["24","120","720","8"],
				 "answer": [ 3," We know, n! = n.(n-1).(n-2).(n-3)…..6! = 6.5.4.3.2.1 = 720."]
			},
			{	"questionNumber":2,
				"question":"7!/5!=  ",
				 "options":["7","42","230","30"],
				 "answer": [ 2,"We know, n! = n.(n-1).(n-2).(n-3)…… = n(n-1)!,7!/5!=7.6!/5!=7.6.5!/5! = 7.6 = 42"]
			},
			{	"questionNumber":3,
				"question":"100/10!=18!+x9! . Find x. ",
				 "options":["1","2","3","4"],
				 "answer": [ 1,"10010!=18!+x9! .We know, n! = n.(n-1). (n-2). (n-3) …………… = n(n-1)!,100/10.9.8!=1/8!+x/9.8!=> 100/10.9=11+x/9=> 109=1+x/9=> x/9=10/9–1=1/9=> x=1."]
			},
			{	"questionNumber":4,
				"question":" nP0=",
				 "options":["n! ","1","1/(n)!","(n-1)!"],
				 "answer": [ 2,"We know, nPr = n!/(n−r)!.nP0 = n!/(n−0)!=n!/(n)! = 1."]
			},
			{	"questionNumber":5,
				"question":"nPn=",
				 "options":["n! ","1","1/n!"," (n-1)!"],
				 "answer": [1 ,"We know, nPr = n!/(n−r)!.nPn = n!/(n−n)!=n!/(0)! = n!"]
			},
			{	"questionNumber":6,
				"question":"The number of permutations of n different objects taken r at a time, where repetition is allowed is ",
				 "options":["n! ","r!","nPr","n^r"],
				 "answer": [4 ,"The number of permutations of n different objects taken r at a time, where repetition is allowed is n*n*n*n*n……………. r times = n^r."]
			},
			{	"questionNumber":7,
				"question":"Find the number of permutations of word DEPENDENT. ",
				 "options":["132400","1512500","1663200","1723400"],
				 "answer": [3 ," There are total 9 letters out of which 1T, 2N, 2D, 3E, 1P.Total number of permutations are 9!/3!2!2!=9.8.7.6.5.4.3.2.1/6∗2∗2=362880/24 = 15120."]
			},
			{	"questionNumber":8,
				"question":"Find the number of 5 letter words which can be formed from word IMAGE without repetition using permutations. ",
				 "options":["20","60","120","240"],
				 "answer": [ 3,"IMAGE is a 5 letters word. We have to arrange all 5 letters of the word IMAGE without repetition. So, total permutations are nPr = 5P5 = 5! = 5.4.3.2.1 = 120."]
			},
			{	"questionNumber":9,
				"question":"Find the number of 5 letter words that can be formed from word IMAGE using permutations if repetition is allowed.",
				 "options":["25","120","125","3125"],
				 "answer": [4 ,"IMAGE is a 5 letters word. We have to arrange all 5 letters of the word IMAGE with repetition allowed. So, total permutations are nr = 55 = 3125."]
			},
			{	"questionNumber":10,
				"question":"Find the number of 4 letter words which can be formed from word IMAGE using permutations without repetition. ",
				 "options":["20 ","60","120","240"],
				 "answer": [3 ," We have to arrange 4 letters of the 5 letters word IMAGE without repetition. So, total permutations are nPr = 5P4 = 5! / (5-4)! = 5! = 5.4.3.2.1 = 120."]
			},
			{	"questionNumber":11,
				"question":"How many 3-digit numbers are possible using permutations without repetition of digits if digits are 1-9? ",
				 "options":["504 ","729","1000","720"],
				 "answer": [ 1,"1-9 digits which means 9 digits are possible. We have to arrange 3 digits at a time out of 9 digits without repetition. So, total permutations are nPr = 9P3 = 9!(9−3)!=9!6! = 9.8.7 = 504."]
			},
			{	"questionNumber":12,
				"question":"How many 3-digit numbers are possible using permutations with repetition allowed if digits are 1-9? ",
				 "options":["504 ","729","1000","720"],
				 "answer": [2 ,"1-9 digits which means 9 digits are possible. We have to arrange 3 digits at a time out of 9 digits with repetition allowed. So, total permutations are nr = 93 = 729."]
			},
			{	"questionNumber":13,
				"question":" If nP3 = 4*nP2. Find n. ",
				 "options":["3 ","2","6","5"],
				 "answer": [ 3," nP3 = 4*nP2 n!(n−3)!=4∗n!(n−2)!=> n-2 = 4=> n=6."]
			},
			{	"questionNumber":14,
				"question":"  4Pr = 4*5Pr-1. Find r.",
				 "options":["1 ","2","3","4"],
				 "answer": [ 1,"4Pr = 4*5Pr-1=> 4!(4−r)!=4∗5!(5−r+1)!=> (6−r)!(4−r)!=4∗5!4!=> (6-r) (5-r) = 4*5=> r=1."]
			},
			{	"questionNumber":15,
				"question":" Find the number of different 8-letter arrangements that can be made from the letters of the word EDUCATION so that all vowels occur together. ",
				 "options":["40320 "," 37440","1440","2880"],
				 "answer": [4 ,"There are 5 vowels in word EDUCATION. 5 vowels can be arranged in 5P5 i.e. 5! ways. When all vowels are together, 5 vowels together form one letter and remaining 3 letters i.e. together 4 letters can be arranged in 4P4 i.e. 4! ways. Total possible arrangements are 5! * 4! = 120*24 = 2880."]
			},
			{	"questionNumber":16,
				"question":"Find the number of different 8-letter arrangements that can be made from the letters of the word EDUCATION so that all vowels do not occur together. ",
				 "options":["40320 "," 37440","1440","2880"],
				 "answer": [2,"There are 5 vowels in word EDUCATION. 5 vowels can be arranged in 5P5 i.e. 5! ways. When all vowels are together, 5 vowels together form one letter and remaining 3 letters i.e. together 4 letters can be arranged in 4P4 i.e. 4! ways. Total possible arrangements are 5! * 4! = 120*24 = 2880.So, when all vowels do not occur together, total possible arrangements = 8! – 2880 = 40320 – 2880 = 37440."]
			},
			{	"questionNumber":17,
				"question":"In how many ways 2 red pens, 3 blue pens and 4 black pens can be arranged if same color pens are indistinguishable? ",
				 "options":[" 362880 ","1260"," 24","105680"],
				 "answer": [2 ,"Total number of pens are 2+3+4 = 9 out of which 2 are of 1 type, 3 are of 2nd type and 4 are of 3rd type so, total number of arrangements = 9!2!3!4!=9∗8∗7∗6∗52∗6 = 1260."]
			},
			{	"questionNumber":18,
				"question":"Find the number of words which can be made using all the letters of the word IMAGE. If these words are written as in a dictionary, what will be the rank of MAGIE? ",
				 "options":["97 ","98","99","100"],
				 "answer": [3 ,"Words starting with letter A comes first in dictionary. Starting with A, number of words = 4! = 24. Starting with E, number of words = 4! = 24. Starting with I, number of words = 4! = 24. Starting with G, number of words = 4! = 24. Since our word also start with M so, we have to consider one more letter i.e. MA. Since our word also start with MA so, we have to consider one more letter i.e. MAE. Starting with MAE, number of words = 2! = 2. Since our word also start with MAG so, we have to consider one more letter i.e. MAGE. Starting with MAGE, only one letter i.e. MAGEI. After this, MAGIE comes. Total number of words before MAGIE = 24 + 24 + 24 + 24 + 2 = 98. So, rank of MAGIE is 99."]
			},
			{	"questionNumber":19,
				"question":" If nC2 = nC3 then find n. ",
				 "options":["2 ","3","5","6"],
				 "answer": [ 3," We know, nCp = nCq=>either p = q or p + q = n.Here p=2 and q=3 so, p ≠ q.Hence p + q = n => n = p + q = 2 + 3 = 5."]
			},
			{	"questionNumber":20,
				"question":"Determine n if 2nC3: nC3 = 9:1. ",
				 "options":["7 ","14","28","32"],
				 "answer": [2 ," We know, nCr = n!(n−r)!r!.2nC3 / nC3 = n!3!(2n−3)!n!3!(n−3)!= 2n!(n−3)!n!(2n−3)!9/1 = 2n(2n−1)(2n−2)n(n−1)(n−2)9 = 2(2n−1)2(n−2)9n-18 = 8n-4=>n=14."]
			}
		]
        },
		{
    	"ChapterName":"Sequence and Series",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"Complete 2,3,5,7, ",
				 "options":["8","9","10","11"],
				 "answer": [4, " Since 2,3,5 and 7 all are consecutive prime numbers so, it is a sequence of prime numbers. Prime number next to 7 is 11. So, 2,3,5,7,11."]
			},
			{	"questionNumber":2,
				"question":" Complete 2, 4, 6, 8, ",
				 "options":["10","9","13","11"],
				 "answer": [1, "Since 2,4,6 and 8 are even numbers so it is a sequence of even numbers. Even number next to 8 is 10. So, 2,4,6,8,10."]
			},
			{	"questionNumber":3,
				"question":" Which of the following is finite sequence? ",
				 "options":[" 48,24,12, …………","1,2,3, …………"," 2,4,6,8,10"," 2,3,5,7,11,13, ……………………"],
				 "answer": [3, "Since sequence 2,4,6,8,10 contains limited number of terms so, it is finite sequence. Rest all are infinite sequences."]
			},
			{	"questionNumber":4,
				"question":"Which of the following relation gives Fibonacci sequence? ",
				 "options":["an = an-1 + an-2","an-1 = an + an-2","an-2 = an + an-1"," an = an+1 + an-2"],
				 "answer": [1, "an = an-1 + an-2, n>2.This is a recurrence relation which gives Fibonacci sequence."]
			},
			{	"questionNumber":5,
				"question":"What is the first term of Fibonacci sequence? ",
				 "options":["0","1","2","3"],
				 "answer": [2, " a1=1 and a2=1.an = an-1 + an-2, n>2.This is a recurrence relation which gives the Fibonacci sequence."]
			},
			{	"questionNumber":6,
				"question":"What is the third term of Fibonacci sequence? ",
				 "options":["0","1","2","3"],
				 "answer": [3, "a1=1 and a2=1.an = an-1 + an-2, n>2.This is a recurrence relation which gives Fibonacci sequence.=>a3=a1+a2=1+1=2."]
			},
			{	"questionNumber":7,
				"question":"If an = 4n+6, find 15th term of the sequence. ",
				 "options":["6","10","60","66"],
				 "answer": [4, "an = 4n+6 and n=15=>a15 = 4*15 + 6 = 60+6 = 66."]
			},
			{	"questionNumber":8,
				"question":"a1 = a2 = 2, an = an – 1–1, n > 2. Find a5. ",
				 "options":["2","-1","1","0"],
				 "answer": [2, "an = an – 1–1, n > 2=> a3 = a2 – 1 = 2 – 1 = 1=> a4 = a3 – 1 = 1 – 1 = 0=> a5 = a4 – 1 = 0 – 1 = -1."]
			},
			{	"questionNumber":9,
				"question":"A series can also be denoted by symbol  ",
				 "options":["π an","∑an","Φ an","θ an"],
				 "answer": [2, "When we use addition between the terms of sequence, it is said to be series.We know that addition can also be written in the form of sigma so, series can also be denoted by ∑an."]
			},
			{	"questionNumber":10,
				"question":"1+2+3+4 or 10 is a series? ",
				 "options":[" 1+2+3+4 only","10 only"," 1+2+3+4 and 10","neither 1+2+3+4 nor 10"],
				 "answer": [1, "1+2+3+4 is a finite series of 4 terms.10 is sum of the terms of this series not a series itself."]
			},
			{	"questionNumber":11,
				"question":"Find sum of series 2+3+5+7. ",
				 "options":["5","10","17","infinite"],
				 "answer": [3, "Sum of the series 2+3+5+7 is finite because given series has finite number of terms. The sum of given 4 terms i.e. 17."]
			},
			{	"questionNumber":12,
				"question":" Find the sum of first 5 terms of series 2+4+6+ ",
				 "options":["14","16","20","30"],
				 "answer": [4, "Since 2, 4 and 6 all are even numbers so, given series involve all even number terms.The next two terms will be 8 and 10 so, sum will be 2+4+6+8+10 = 30."]
			},
			{	"questionNumber":13,
				"question":"Which of the following is not a series? ",
				 "options":["Arithmetic series","Geometric series","Isometric series","Harmonic series"],
				 "answer": [3, "The isometric series is not a series. Rest all are series i.e. arithmetic series, geometric series and harmonic series."]
			},
			{	"questionNumber":14,
				"question":"What is nth term of an A.P.? ",
				 "options":[" an = a + (n-1) d"," an = a + (n) d","an = a*rn-1","an = a*rn"],
				 "answer": [1, " Since every term of an A.P. is incremented by common difference d.i.e. an+1 = an + d = an-1 + 2d = ……. = a1 + n*d or an = a + (n-1) d"]
			},
			{	"questionNumber":15,
				"question":"If 3rd term of an A.P. is 6 and 5th term of that A.P. is 12. Then find the 21st term of that A.P. ",
				 "options":["40","42","60","63"],
				 "answer": [3, " Given, a3 = 6 and a5 = 12.=> a + 2d = 6 and a + 4d = 12=> 2d = 6 => d=3.=> a + 2*3 = 6 => a=0 So, a21 = a + 20 d = 0 + 20*3 = 60."]
			},
			{	"questionNumber":16,
				"question":"If sum of n terms of an A.P. is n2+5n then find general term. ",
				 "options":["n+1","2n","3n","n2+3n"],
				 "answer": [2, " Given, Sn = n2+5n We know, an = Sn– Sn-1 = (n2+5n) – ((n-1)2+5(n-1)) = (n2+5n) – (n2+1-2n+5n-1) = 2n."]
			},
			{	"questionNumber":17,
				"question":"If in an A.P., first term is 20 and 12th term is 120. Find the sum up to 12th term. ",
				 "options":["420"," 840","140","1680"],
				 "answer": [2, " Given, a=20, a12= 120, n=12.Sn = n/2 (a+l) => S12 = 12/2(20+120) = 6*140 = 840."]
			},
			{	"questionNumber":18,
				"question":"If in an A.P., first term is 20, common difference is 2 and nth term is 42, then find n. ",
				 "options":["10","11","12","14"],
				 "answer": [3, " We know, a=20, d=2, an=42. a+(n-1) d = 42 => 20 + 2(n-1) = 42=>2(n-1) = 42-20=22 => n-1 =11 => n=12."]
			},
			{	"questionNumber":19,
				"question":"If in an A.P., first term is 20, common difference is 2 and nth term is 42, then find sum up to n terms. ",
				 "options":["12","42","352","372"],
				 "answer": [4, "We know, a=20, d=2, an=42.a+(n-1) d = 42 => 20 + 2(n-1) = 42=>2(n-1) = 42-20=22 => n-1 = 11 => n=12.Sn = n2 (a+l) => S12 = 122 (20+42) = 6*62 = 372."]
			},
			{	"questionNumber":20,
				"question":"If general term of an A.P. is 3n then find common difference. ",
				 "options":["2","3","5","6"],
				 "answer": [2, " Given, an = 3n.We know, d = an-an-1 = 3n – 3(n-1) = 3."]
			}
			
		
		]
        },
		{
    	"ChapterName":"Straight Lines",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"What is the distance between (1, 3) and (5, 6)? ",
				 "options":["3 units","4 units","5 units","25 units"],
				 "answer": [3,"We know, distance between two points (x1, y1) and (x2, y2) is (x1−x2)2+(y1−y2)2−−−−−−−−−−−−−−−−−−√.So, distance between (1, 3) and (5, 6) is (1−5)2+(3−6)2−−−−−−−−−−−−−−−√=(4)2+(3)2−−−−−−−−−√ = 5 units."]
			},
			{	"questionNumber":2,
				"question":"What is the distance of (5, 12) from origin? ",
				 "options":[" 6 units","8 units","10 units","13 units"],
				 "answer": [4,"We know, distance between two points (x1, y1) and (x2, y2) is (x1−x2)2+(y1−y2)2−−−−−−−−−−−−−−−−−−√.So, distance between (5, 12) from origin (0, 0) is (5−0)2+(12−0)2−−−−−−−−−−−−−−−−√=(5)2+(12)2−−−−−−−−−−√ = 13 units."]
			},
			{	"questionNumber":3,
				"question":"The coordinates of a point dividing the line segment joining (1, 2) and (4, 5) internally in the ratio 2:1 is ",
				 "options":["(3, 4)","(4, 3)"," (5, 4)"," (5, 3)"],
				 "answer": [1,"The coordinates of a point dividing the line segment joining (x1, y1) internally in the ratio m: n is (mx2+nx1m+n,my2+ny1m+n).So, the coordinates of a point dividing the line segment joining (1, 2) and (4, 5) internally in the ratio 2:1 is (2∗4+1∗12+1,2∗5+1∗22+1) = (3, 4)."]
			},
			{	"questionNumber":4,
				"question":"In which ratio (3, 4) divides the line segment joining (1, 2) and (4, 5) internally? ",
				 "options":[" 1:2","2:1","3:4","4:3"],
				 "answer": [2,"The coordinates of a point dividing the line segment joining (x1, y1) and (x2, y2) internally in the ratio m: n is (mx2+nx1m+n,my2+ny1m+n).Let the ratio be k: 1.So, the coordinates of a point dividing the line segment joining (1, 2) and (4, 5) internally in the ratio k: 1 is (k∗4+1∗1k+1,k∗5+1∗2k+1)=> (k∗4+1∗1k+1,k∗5+1∗2k+1) is same as (3, 4).=> (4k+1)/(k+1) = 3=> 4k+1 = 3k+3=> k = 2So, ratio is 2:1."]
			},
			{	"questionNumber":5,
				"question":"The coordinates of a point dividing the line segment joining (1, 2) and (4, 5) externally in the ratio 2:1 is ",
				 "options":["(4, 5)","(6, 8)","(7, 8)","(8, 6)"],
				 "answer": [3,"The coordinates of a point dividing the line segment joining (x1, y1) and (x2, y2) externally in the ratio m: n is (mx2−nx1m−n,my2−ny1m−n).So, the coordinates of a point dividing the line segment joining (1, 2) and (4, 5) externally in the ratio 2:1 is (2∗4−1∗12−1,2∗5−1∗22−1) = (7, 8)."]
			},
			{	"questionNumber":6,
				"question":"What is the area of triangle whose vertices are (-4, -4), (-3, 2), (3, -16)? ",
				 "options":[" 24 sq. units","27 sq. units","32 sq. units"," 37 sq. units"],
				 "answer": [2,"We know, area of triangle joining vertices (x1, y1), (x2, y2) and (x3, y3) is (1/2)* determinant  is 12{(-4)(2+16) – (-4)(-3-3) + (1)(48-6)} = 12|(-72)+(-24)+42| = 27 square units."],
			},
			{	"questionNumber":7,
				"question":"Find slope of line if inclination made by the line is 60°. ",
				 "options":["1/2","1/√3","√3"," 1"],
				 "answer": [3,"Slope of a line is given by tanα if inclination of line is α. If inclination is 60° the slope is tan 60° = √3."]
			},
			{	"questionNumber":8,
				"question":"What is the inclination of a line which is parallel to x-axis? ",
				 "options":["0°"," 180°"," 45°","90°"],
				 "answer": [1," If a line is parallel to x-axis then angle formed by it with x-axis is zero. So, its inclination is zero."]
			},
			{	"questionNumber":9,
				"question":"What is the inclination of a line which is parallel to y-axis? ",
				 "options":["0°"," 180°"," 45°","90°"],
				 "answer": [4," If a line is parallel to y-axis then angle formed by it with x-axis is 90°. So, its inclination is 90°."]
			},
			{	"questionNumber":10,
				"question":"What is the slope of a line which is parallel to x-axis? ",
				 "options":["1","0","-1","Not Defined"],
				 "answer": [2,"If a line is parallel to x-axis then angle formed by it with x-axis is zero. So, its inclination is zero. Hence slope = tan 0° = 0."]
			},
			{	"questionNumber":11,
				"question":"What is the slope of a line which is parallel to y-axis? ",
				 "options":["1","0","-1","Not Defined"],
				 "answer": [4,"If a line is parallel to y-axis then angle formed by it with x-axis is zero. So, its inclination is 90°. Hence slope = tan 90° which is not defined."]
			},
			{	"questionNumber":12,
				"question":"If slope of a line is positive then its inclination is  ",
				 "options":[" right angle","acute angle","obtuse angle","zero"],
				 "answer": [2,"If inclination is α slope is given by tan α. Given that slope of line is positive which means tan α is positive. We know, tan α is positive in 1st quadrant i.e. α should be acute angle."]
			},
			{	"questionNumber":13,
				"question":" If slope of a line is negative then its inclination is ",
				 "options":[" right angle","acute angle","obtuse angle","zero"],
				 "answer": [3,"If inclination is α slope is given by tan α. Given that slope of line is negative which means tan α is negative. We know, tan α is negative in 2nd quadrant i.e. α should be obtuse angle."]
			},
			{	"questionNumber":14,
				"question":" Find slope of line joining (1, 2) and (4, 11). ",
				 "options":["1/3","3","9","1/9"],
				 "answer": [2,"We know, slope of line joining two points (x1, y1) and (x2, y2) is given by y2−y1x2−x1.So, slope of line joining (1, 2) and (4, 11) is 11−24−1=93 = 3."]
			},
			{	"questionNumber":15,
				"question":"If the two lines are perpendicular then difference of their inclination angle is  ",
				 "options":["45°","60°","90°","180°"],
				 "answer": [3," If the two lines are perpendicular then if one line form angle α with positive x-axis then the other line form angle 90°+ α."]
			},
			{	"questionNumber":16,
				"question":"If the two lines with slope m1 and m2 are perpendicular then their slopes has relation ",
				 "options":["m1 + m2 = 1","m1 * m2 = 1","m1 * m2 = -1","m1 + m2 = -1"],
				 "answer":[3," If the two lines are perpendicular then if one line form angle α with positive x-axis then the other line form angle 90° + α.If m1 = tan α then m2 will be tan (90°+ α) = – cot α = -1/tan α=> m1 * m2 = – 1."]
			},
			{	"questionNumber":17,
				"question":"If angle between the two lines is 45° and slope of one line is 1/4 then which of the following is possible value of the slope of other line. ",
				 "options":["3/5","-3/5","-5/3","4/5"],
				 "answer": [2,"If angle between two lines with slopes m1 and m2 is α then tan α = |(m1-m2)/(1+m1*m2)|tan 45° = |m−1/41+m/4|=> 4m−1m+4 = -1=>- m-4 = 4m-1 => 5m = -3=> m = -3/5."]
			},
			{	"questionNumber":18,
				"question":" If slope of a line is 2/3 then find the slope of line perpendicular to it. ",
				 "options":["-3/2","3/2","2/3","-2/3"],
				 "answer": [1,"If lines with slopes m1 and m2 are perpendicular then m1 * m2 = – 1.If m1 = 2/3 then m2 = -1 / (2/3) = -3/2."]
			},
			{	"questionNumber":19,
				"question":"If slope of one line is 1/4 and other is 5/3 then find the angle between two lines. ",
				 "options":["30°","45°"," 90°","180°"],
				 "answer": [2,"If angle between two lines with slopes m1 and m2 is α then tan α = |(m1-m2)/(1+m1*m2)|tan α = |5/3−1/41+5/3∗1/4|=|20−312+5| = 17/17 =1 => α = 45°"]
			},
			{	"questionNumber":20,
				"question":" Find slope of line passing through origin and (3, 6). ",
				 "options":["2","3","1/2","1/3"],
				 "answer": [1," We know, slope of line joining two points (x1, y1) and (x2, y2) is given by (y2-y1)/(x2-x1).So, slope of line joining (0, 0) and (3, 6) is (6-0)/(3-0) = 6/3 = 2."]
			}
			
		]
        },
		{
    	"ChapterName":"Conic Section",
		"questionSet":[
			{	"questionNumber":1,
				"question":"The equation of a parabola is y^2=4x  P(1,3) and Q(1,1) are two points in x-y plane then ,for the parabola ",
				 "options":["P and Q are exterior points","P is an interior point while Q is an exterior point","P and Q are interior points","P is an exterior while Q is an interior point"],
				 "answer": [4, "S=y^2-4x  P(1,3)= 32-4=5 >0 (1,3) is exterior Point. Q(1,1) =12-4=-3<0  (1,1) is an interior point."]
			  },
			{	"questionNumber":2,
				"question": "If the vertex of a parabola be at origin and directrix be x+5 = 0, then its latus rectum is", 	
				"options":["5","10","20","40"],
				"answer": [3 , "S = (5,0). Therefore, latus rectum 4a=20 ."]
			  },
			{	"questionNumber":3,
				"question": "For the ellipse 3x^2 + 4y^2 = 12, the length of latus rectum is",	
				"options":[ "3/2","3","8/3" ,"(3/2)^(1/2)" ],
				"answer": [2, "x^2/4 + y^2/3 = 1 Latus rectum 2b^2/a = 3 ."]
			  },
			{	"questionNumber":4,
				"question": "The equation of the lines joining the vertex of the parabola y^2=6x to the points on it whose abscissa is 24, is",	
				"options": [ "y _+ 2x = 0", "2y _+ x = 0", "3x _+ 2y = 0", "2x _+ y = 0"],
				"answer": [2,"y^2 = 6.24, points are (24,_+ 12), lines are 2y = -+ x"]
			  },
			{	"questionNumber":5,
				"question": "The points on the parabola y^2=12x whose focal distance is 4, are",
				"options": ["(2,3^0.5),(2,-3^0.5)", "(1, 2* 3^0.5),(1, -2* 3^0.5)" , "(1, 2)", "None of these"],
				"answer": [2, "a = 3 => abscissa 4-3=1 and y^2 = 12. Points are (1,_+12)"]
			  },
			{	"questionNumber":6,
				"question": "A parabola passing through the point (-4,-2) has its vertex at the origin and y-axis as its axis. The latus rectum of the parabola is",
				"options":[ "6", "8", "10", "12"],
				"answer": [2,"Let equation of parabola is x^2=4ay, but a=4/(-2). Then equation is x^2 =-8y and latus rectum 4a=8."]
			  },
			{	"questionNumber":7,
				"question": "The ends of latus rectum of parabola x^2+8y=9 are",
				"options":["(–4, –2) and (4, 2)", "(4, –2) and (–4, 2)", "(–4, –2) and (4, –2)"	,"(4, 2) and (–4, 2)"],
				"answer": [3," x^2 = -8y =>a=-2. So, focus = (0,-2). Ends of latus rectum =(4,-2),(-4,-2).Trick : Since the ends of latus rectum lie on parabola,so only points (-+4, -2) and  satisfy the parabola."]
			  },
			{	"questionNumber":8,
				"question": "The equation of the parabola with focus (3, 0) and the directirx x+3=0 is", 	
				"options": [ "y^2 = 3x", "y^2 = 2x", " y^2 = 12x", "y^2 = 6x"],
				"answer": [8, "SP^2 = PM^2"]
			  },
			{	"questionNumber":9,
				"question": "Vertex of the parabola 9x^2 - 6x + 36y + 9 = 0 is",
				"options":["(1/3, -2/9)", "(-1/3, -1/2)", "(-1/3,1/2)", "(1/3,1/2)"],
				"answer": [1, "The equation can be written as (3x-1)^2 = -4(9y+2) .Hence the vertex is (1/3,-2/9) ."]
			  },
			{	"questionNumber":10,
				"question": "The focus of the parabola y^2=4y - 4x is",
				"options": ["(0, 2)", "(1, 2)", "(2, 0)", "(2, 1)"],
				"answer": [1, "(y-2)^2 = -4(x-1), Vertex is (1,2) and focus = (0,2)."]
			  },
			{	"questionNumber":11,
				"question": " The equation 13[(x-1)^2 + (y-2)^2] = 3(2x + 3y -2)^2 represents",
				"options": ["Parabola", "Ellipse", "Hyperbola", "None of these"],
				"answer": [3, "Here coefficient of x^2  is +ve and that of y^2  is –ve i.e., a hyperbola."]
			  },
			{	"questionNumber":12,
				"question": " The number of values of c such that the straight line y = 4x + c touches the curve (x^2)/4 + y^2 = 1 is",	
				"options": ["0","1","2","Infinite"],
				"answer": [3, "The line y=4x+c touches the ellipse x^2/4 + y^2 = 1, .'. x^2/4 + (4x+c)^2 -1 = 0 has equal roots."]
			  },
			{	"questionNumber":13,
				"question": " What will be the equation of that chord of ellipse x^2/36 + y^2/9 = 1 which passes from the point (2,1) and bisected on the point ",
				"options": ["x+y = 2", "x + y = 3" , "x + 2y = 1", "x + 2y = 4"],
				"answer": [4]
			  },
			{	"questionNumber":14,
				"question": "Eccentricity of the rectangular hyperbola  is",
				"options": ["2","2^0.5" ,"1", "1/(2^0.5)"],
				"answer": [2, "Eccentricity of rectangular hyperbola is 2^(0.5)."]
			  },
			{	"questionNumber":15,
				"question": "The eccentricity of a hyperbola passing through the points (3, 0),(3*(2^0.5), 2)  will be ",
				"options": [ "13^0.5", "(13^0.5)/3", "(13^0.5)/4", "(13^0.5)/2"],
				"answer": [2, "9/a^2 = 1 hence, 18/a^2 - 4/b^2 = 1."]
			  },
			{	"questionNumber":16,
				"question": "If the centre, vertex and focus of a hyperbola be (0, 0), (4, 0) and (6, 0) respectively, then the equation of the hyperbola is",
				"options": [ "4x^2 - 5y^2 = 8", "4x^2 - 5y^2 = 80", "5x^2 - 4y^2 = 80", "5x^2 - 4y^2= 8"],
				"answer": [3, "Centre (0, 0), vertex (4,0) => a=4 and focus (6,0) ae=4 => e = 3/2 . Therefore b = 2(5^0.5)."]
			  },
			{	"questionNumber":17,
				"question": "The eccentricity of the hyperbola 2X^2 - y^2 = 6 is",
				"options": ["2^0.5" , "2", "3", "3^0.5"],
				"answer": [4, "a^2 = 3, b^2 = 6. Hence, e = (b^2/a^2 + 1)^0.5 ."]
			  },
			{	"questionNumber":18,
				"question": "Centre of hyperbola 9x^2 - 16y^2 + 18x + 32y - 151 = 0 is",
				"options": ["(1, –1)","(–1, 1)","(–1, –1)","(1, 1)"],
				"answer": [2, "Centre is given by ( (hf-bg)/(ab-h^2), (gh-af)/(ab-h^2) ) = (+16*9/-9*16, -9*16/-9*16)"]
			  },
			{	"questionNumber":19,
				"question": "The auxiliary equation of circle of hyperbola x^2/a^2 - y^2/b^2 = 1, is",
				"options": ["x^2 + y^2 = a^2", "x^2 + y^2 = b^2", "x^2 + y^2 = a^2 + b^2", "x^2 + y^2 = a^2 - b^2"],
				"answer": [1, "The equation is (x-0)^2 -(y-0)^2 = a^2"]
			  },
			{	"questionNumber":20,
				"question": "The distance between the directrices of the hyperbola x = 8*sec b, y = 8*tan b  is ",
				"options": ["16*2^(1/2)", "2^0.5", "8*2^0.5", "4*2^0.5"],
				"answer": [3, "Equation of hyperbola is a = 8, b= 8 and e = (1 + b^2/a^2)^0.5"]
			},
			{   "questionNumber":21,
				"question":"The equation of the directrices of the conic x^2+2*x-y^2+5=0 are",
				 "options":["x=_+1 ","y=_+2","y=_+sroot(2)","x=_+sroot(3)"],
				 "answer":[3,"(x+1)^2-y^2-1+5=0=>(x+1)^2/4+y^2/4=1. Equation of directrices  of y^2/b^2 -x^2/a^2=1 y=_+b/e are  Here b=2,e=sroot(1+1)=sroot(2) Hence y=_+2/sroot(2)=>y=_+sroot(2)."]
			  },
			{   
				"questionNumber":22,
				"question": "A hyperbola passes through the points (3, 2) and (–17, 12) and has its centre at origin and transverse axis is along x-axis. The length of its transverse axis is", 	
				"options":["2","4","6","None of these"],
				"answer":[1,"Let the equation of hyperbola is x^2/a^2-y^2/b^2=1 But it passes through (3, 2)=>9/a^2-4/b^2=1.....(i)Also its passes through (–17, 12)=>(-17)*(-17)/a^2-12^2/b^2=1.....(ii)Solving these, we get a=1 and b=sroot(2) .Hence length of transverse axis =2*a=2."]
			  },
			{
				"questionNumber":23,
				"question": "If transverse and conjugate axes of a hyperbola are equal, then its eccentricity is", 	
				"options":["sroot(3)","sroot(2)","1/sroot(2)",2],
				"answer":[2,"Hyperbola is  x^2/a^2-y^2/b^2=1. Here, transverse and conjugate axis of a hyperbola is equal.i.e. a=b x^2-y^2=a^2; which is a rectangular hyperbola. Hence, eccentricity e=sroot(1+b^2/a^2)=sroot(2)."]
			  },
			{
				"questionNumber":24,
				"question": "The equation of the director circle of the hyperbola x^2/16-y^2/4=1 is given by", 	
				"options":["x^2+y^2=16","x^2+y^2=4","x^2+y^2=20","x^2+y^2=12"],
				"answer":[4,"Equation of ‘director-circle’ of hyperbola is x^2+y^2=a^2-b^2 .  Here a^2=16 b^2=4 ,x^2+y^2=12 is the required ‘director circle’. "]
			  },
			{   "questionNumber":25,
				"question": "The equation of the tangent parallel to y-x+5 drawn to x^2/3-y^2/2=1", 	
				"options":["x-y-1=0","x-y+2=0","x+y-1=0","x+y=2=0"],
				"answer":[1,"Given hyperbola is x^2/3-y^2/2=1.....(i)Equation of tangent parallel to y-x+5=0 is y-x+lambda=0=>y=x-lambda.....(ii)If line (ii) is a tangent to hyperbola (i), then-lambda=_+sroot(3*1-2) (from c=_+sroot(a^2*m^2-b^2 ) -lambda=_+1=>lambda=-1,+1.Put the values of lambda  in (ii), we get x-y-1=0  and x-y=1  are the required tangents."]
			  }, 
			{"questionNumber":26,
				"question": "Let E be the ellipse x^2/9+y^2/4=1  and C be the circle x*x+y*y=9 . Let P and Q be the points (1, 2) and (2, 1) respectively. Then", 	
				"options":["Q lies inside C but outside E","Q lies outside both C and E","P lies inside both C and E","P lies inside C but outside E"],
				"answer":[4,"The given ellipse is  x^2/9+y^2/4=1. The value of the expression x^2/9+y^2/4-1  is positive for x=1,y=2  and negative for x=2,y=1 . ThereforeP lies outside E and Q lies inside E. The value of the expression x^2+y^2-9 is negative for both the points P and Q. ThereforeP and Q both lie inside C. Hence P lies inside C but outside E."]
			  },
			{   "questionNumber":27,
				"question": "If e and e’ are eccentricities of hyperbola and its conjugate respectively, then", 	
				"options":["(1/e)^2+(1/e')^2=1","(1/e)+(1/e')=1","(1/e)^2+(1/e')^2=0","(1/e)+(1/e')=2"],
				"answer":[1,"Let hyperbola is x^2/a^2-y^2/b^2=1....(i)Then its conjugate will be,x^2/a^2-y^2/b^2=-1  .....(ii)If e  is eccentricity of hyperbola (i), then b^2=a^2(e^2-1) or 1/e^2=a^2/a^2+b^2.....(iii),Similarly if e' is eccentricity of conjugate (ii),then  a^2=b^2(e'^2-1) or  1/e'^2=b^2/a^2+b^2.....(iv)Adding (iii) and (iv),1/(e')^2+1/e^2 = (a^2/a^2+b^2)+(b^2/a^2+b^2 )=1"]
			  }, 
			{   "questionNumber":28,
				"question": "The length of the latus rectum of the parabola whose focus is (3, 3) and directrix is 3*x-4*y-2=0 is", 	
				"options":["2","1","4","None of these"],
				"answer":[1,"Since the distance between the focus and directrix of the parabola is half of the length of the latus rectum (L.R.). Therefore, L.R. = 2 (Length of the perpendicular from (3,3)  on 3*x-4*y-2=0) i.e.,2. = 2.mod(9-12-2/sroot(9+16))=2"]
			  } , 
			{   "questionNumber":29,
				"question": "The equation of the directrix of the parabola y*y=4*y+4*x+2=0 is", 	
				"options":["x=-1","x=1","x=-3/2","x=3/2"],
				"answer":[4,"Here y^2+4*y+4=4*x-2=0 or (y+2)^2=-4(x-1/2)  Let y+2=Y,1/2-x=X  . Then the parabola is Y*Y=4X.Directrix is X+1=0 or 1/2-x+1=0. So,x=3/2 ."]
			  } , 
			{   "questionNumber":30,
				"question": "The equation of the ellipse whose one of the vertex is (0,7) and the corresponding directrix is y=12 , is ", 	
				"options":["95*x^2+144*y^2=4655","144*x^2+95*y^2=4655","95*x^2+144*y^2=13680","None of these"],
				"answer":[2,"Vertex (0,7), directrix y=12.b=7, Also b/e=12=>e=7/12,a=7*sroot(95/144).Hence equation of ellipse is 144x*x+95*y^2=4655 ."]
			  } ,
			{   "questionNumber":31,
				"question": "The radius of the circle having its centre at (0, 3) and passing through the foci of the ellipse x^2/16+y^2/9=1 , is  ", 	
				"options":["3","3.5","4","sroot(12)"],
				"answer":[3,"The co-ordinates of foci are (_+ae,0).Here a=4,b=3.b^2=a^2(1-e^2)=>9=16(1-e^2)=>9/16=(1-e^2).e=_+sroot(7/4).Points are (_+sroot(7),0).Radius =sroot((sroot(7-0)^2+(0-3)^2)=sroot(7+9)=sroot(16)=4 "]
			  },
			{   "questionNumber":32,
				"question": "The equation of an ellipse, whose vertices are (2, – 2), (2, 4) and eccentricity 1/3 , is", 	
				"options":["(x-2)^2/9+(y-1)^2/8 =1","(x-2)^2/8+(y-1)^2/9=1","(x+2)^2/8+(y+1)^2/9","(x-2)^2/9+(y+1)^2/8"],
				"answer":[2,"Given, co-ordinates of the vertices (A and A')  of ellipse  ((2.-2) and (2,4) and eccentricity(e)=1/3  . We know that AA'  is along a line parallel to y-axis. Therefore mid-point of AA'(c)=(h,k)=(2,1) and distance between AA'(2b)=6 or b=3  . We also know that the standard equation of an ellipse at co-ordinates (h,k) is (x-h)^2/a*a+(y-k)^2/b*b=1 and a*a=b*b(1-e*e)=9(1-1/9)=8. Therefore equation of the ellipse (x-2)^2/8+(y-1)^2/9=1"]
			  },
			{   "questionNumber":33,
				"question": "The equation of parabola whose vertex and focus are (0, 4) and (0, 2) respectively, is" , 	
				"options":["y^2-8*x=32","y^2+8*x=32","x^2-8*y=32","x^2-8*y=32"],
				"answer":[3,"Vertex(0,4);focus (0,2);a=2.Hence parabola is (x-0)^2=-4,2(y-4) i.e,x^2+8*y=32"]
			 },
			{   "questionNumber":34,
				"question": "If the vertex of the parabola y=x*x-8*x+c lies on x-axis, then the value of c is ", 	
				"options":["–16","–4","4","16"],
				"answer":[4,"The given equation can be written as (x-4)^2=y-(c-16).Therefore the vertex of the parabola is  (4,c-16). The point lies on x axis c-16=0=>c=16."]
			  } ,
			{   "questionNumber":35,
				"question": "Eccentricity of the parabola x^2-4*x-4*y+4=0 is", 	
				"options":["e=0","e=1","e>4","e=4"],
				"answer":[2,"Always eccentricity of parabola is  e=1."]
			  },
			{   "questionNumber":36,
				"question": "equation of the parabola with focus (0, 0) and directrix x+y=4 is", 	
				"options":["x^2+y^2-2*x*y+8*x+8*y-16","x^2+y^2-2*x*y+8*x+8*y","x^2+y^2+8*x+8*y-16","x^2-y^2-2*x*y+8*x+8*y-16"],
				"answer":[1,"SP=PM=>SP^2=PM^2=>x^2+y^2=(x+y-4/sroot(2))^2=>x^2+y^2-2*x*y+8*x+8*y-16=0"]
			  },
			{   "questionNumber":37,
				"question": "The equation of axis of the parabola 2*x^2+5*y-3*x+4=0",	
				"options":["x=3/4","y=3/4","x=-1/2","x-3y=5"],
				"answer":[1,"Given equation of parabola is 2*x^2+5*y-3*x+4=0=>x^2-3/2*x=-5/2*y-2=>(x-3/4)^2=-5/2-23/16=>x-3/4=0=>x=3/4"]
			  },
			{   "questionNumber":38,
				"question": "The point of intersection of the latus rectum and axis of the parabola y^2+4*x+2*y-8=0", 	
				"options":["(5/4, –1)","(9/4, –1)","(7/2, 5/2)","None of these"],
				"answer":[1,"The required point is nothing but the focus of the parabola. Therefore (y+1)^2=-(4*x-9)=>-4(x-9/4).s=(-1+9/4,-1) or(5/4,-1)"]
			  },
			{   "questionNumber":39,
				"question": "The point of intersection of tangents at the ends of the latus-rectum of the parabola y^2=4*x is equal to", 	
				"options":["(1, 0)","(–1, 0)","(0, 1)","(0, –1)"],
				"answer":[2,"Equation of the tangent at (x1,y1)  on the parabola y^2=4*a*x is yy'=2a(x+x1). In this case, a=1 The co-ordinates at the ends of the latus rectum of the parabola  y*y=4*x are L(1,2)  and L(1,-2) Equation of tangent at L and L1  are 2y=2(x+1) and -2y=2(x+1) , which gives x=-1 and y=0 . Thus, the required point of intersection is (–1, 0)."]
		  
			  },
			{   "questionNumber":40,
				"question": "The ends of the latus rectum of the conic x^2+10*x-16*y+25=0 are", 	
				"options":["(3, –4), (13, 4)","(–3, –4), (13, –4)","(3, 4), (–13, 4)","(5, –8),(–5, 8)"],
				"answer":[3,"Equation of conic is x^2+10*x-16*y+25 i.e.,(x+5)^2=16*y . Conic is parabola with focus (–5, 4)focus is mid point of latus rectum.only points given in option (c) can be end points of the latus rectum."]
			},
			{	"questionNumber":41,
				"question":"P is any point on the ellipse 9x*x +36y*y=324 , whose foci are S and S’. Then  SP +SP' equals  ",
				"options":[3,12,36,324],
				"answer": [2,"SP +SP'=2a=> 2.6=12"]
			 },
		   {   "questionNumber":42,
			   "question": "The lengths of major and minor axis of an ellipse are 10 and 8 respectively and its major axis along the y-axis. The equation of the ellipse referred to its centre as origin is  ", 	
			   "options":["x*x/25 + y*y/16 =1","x*x/16 + y*y/25 =1","x*x/100 + y*y/64 =1","x*x/64 + y*y/100 =1"],
			   "answer":[2,"Here given that2b=10,2a=8 thus b=5 a=4 Hence the required equation is ."]
			 },
			 { "questionNumber":43,
			   "question":"If the eccentricity of the two ellipse x*x/169 + y*y/25 =1 and x*x/a*a + y*y/b*b =1 are equal, then the value of a/b is ",
			   "options":["5/13","6/13","13/5","13/6"],
			   "answer": [3]
			},
			{  "questionNumber":44,
			   "question":"The distance between the foci of the ellipse 3x*x +4y*y=48 is ",
			   "options":[3,4,6,8],
			   "answer": [2]
			},
			{  "questionNumber":45,
			   "question":"The co-ordinates of the foci of the ellipse 3x*x +4y*y-12x+8y-4=0 are  ",
			   "options":["(1, 2), (3, 4)","(1, 4), (3, 1)","(1, 1), (3, 1)","(2, 3), (5, 4)"],
			   "answer": [3]
			},
			{  "questionNumber":46,
			   "question":"If the line y=2x=c be a tangent to the ellipse x*x/8 + y*y/4 =1, then c= ",
			   "options":["+-4","+-6","+-1","+-8"],
			   "answer": [2]
			},
			{  "questionNumber":47,
			   "question":"The position of the point (4, –3) with respect to the ellipse 2x*x +5y*y=20 is  ",
			   "options":["Outside the ellipse","On the ellipse ","On the major axis","None of these"],
			   "answer": [1]
			},
			{  "questionNumber":48,
			   "question":"The locus of the point of intersection of mutually perpendicular tangent to the ellipse x*x/a*a + y*y/b*b =1 , is  ",
			   "options":["A straight line","A parabola","A circle","None of these"],
			   "answer": [3]
			},
			{  "questionNumber":49,
			   "question":"If the latus rectum of an hyperbola be 8 and eccentricity be 3/sroot5 , then the equation of the hyperbola is  ",
			   "options":["4x*x -5y*y=100","5x*x -4y*y=100","4x*x +5y*y=100","5x*x +4y*y=100"],
			   "answer": [1]
			},
			{  "questionNumber":50,
			   "question":"The equation of the transverse and conjugate axis of the hyperbola 16x*x -y*y+64x+4y-44=0 are ",
			   "options":["x=2 y+2=0","x=2 y=2","y=2 x+2=0","none of these"],
			   "answer": [3]
			},
			{  "questionNumber":51,
			   "question":"The eccentricity of the hyperbola can never be equal to  ",
			   "options":["sroot 9/5","2 sroot 1/9 ","3 sroot 1/8",2],
			   "answer": [2]
			},
			{  "questionNumber":52,
			   "question":"The number of parabolas that can be drawn if two ends of the latus rectum are given",
			   "options":[1,2,4,3],
			   "answer": [2]
			},
			{  "questionNumber":53,
			   "question":" If the latus rectum of an ellipse be equal to half of its minor axis, then its eccentricity is  ",
			   "options":["3/2","sroot 3/2","2/3","sroot 2/3"],
			   "answer": [2]
			},
			{  "questionNumber":54,
			   "question":" The equation of the ellipse whose centre is at origin and which passes through the points (–3, 1) and (2, –2) is ",
			   "options":["5x*x +3y*y=32","3x*x +5y*y=32","5x*x -3y*y=32","3x*x +5y*y+32=0"],
			   "answer": [2]
			},
		   {   "questionNumber":55,
			   "question":"If the eccentricity of an ellipse be 5/8 and the distance between its foci be 10, then its latus rectum is  ",
			   "options":["39/4",12,15,"37/2"],
			   "answer": [1]
			},
		   {   "questionNumber":56,
			   "question":"The eccentricity of an ellipse is 2/3, latus rectum is 5 and centre is (0, 0). The equation of the ellipse is  ",
			   "options":["x*x/81 + y*y/45 =1","4x*x/81 + 4y*y/45 =1","x*x/9 + y*y/5 =1","x*x/a*a + y*y/b*b=1"],
			   "answer": [2]
			},
		   {   "questionNumber":57,
			   "question":" Equation of the hyperbola with eccentricity 3/2 and foci at (=-2 , 0) is ",
			   "options":["x*x/4 + y*y/5 =4/9","x*x/9 + y*y/9 =4/9","x*x/4 + y*y/9 =1","none of these"],
			   "answer": [2]
			},
		   {   "questionNumber":58,
			   "question":"The equation x*x/2-r + y*y/r-5+1 =0 represents an ellipse if ",
			   "options":["r > 2","r > 5","2 < r <5","r > 5 or r < 2"],
			   "answer": [4]
			},
			{  "questionNumber":59,
			   "question":"The area of the rectangle formed by the ends of latus rectum of ellipse  x*x/25+y*y/9= 1, is ",
			   "options":["18/5 sq units","144/5 sq units","24/5 sq units","36/5 sq units"],
			   "answer": [3]
			}
		]
		},
	   {
    	"ChapterName":"Mathematical Reasoning",
		"questionSet":[
			{	"questionNumber":1,
				"question":"A sentence is called statement if it is ",
				"options":["always true","always false","either true or false but not both"," both true and false"],
				"answer": [4, "A sentence is called mathematically acceptable statement if it is either true or false but not both."]
			  },
			  {	"questionNumber":2,
				"question":"Which of the following is a statement? ",
				 "options":["Women are more intelligent than men","Two plus two is three"," Open the door","Shut your mouth"],
				 "answer": [2, " A sentence is called mathematically acceptable statement if it is either true or false but not both.“Two plus two is three” is false so it is a statement. Rest we cannot decide whether they are true or false."]
			},
			{	"questionNumber":3,
				"question":"Which of the following is not a statement?  ",
				 "options":["Two and two makes four","A prime number is always odd"," Sum of a and b is 5"," Elephant is heavier than ant"],
				 "answer": [3, "“Two and two makes four” and “Elephant is heavier than ant” are true so they are statements. “A prime number is always odd” is false as prime number may be even so it is a statement. “Sum of and b is 5” is not a statement as it can be true or false based on the values of a and b taken."]
			},
			{	"questionNumber":4,
				"question":"Which of the following is a statement?  ",
				 "options":["Today is Monday","Tomorrow will be holiday","If today is Tuesday then tomorrow will be Sunday","There will be full moon tonight"],
				 "answer": [3, "“Today is Monday”, “Tomorrow will be holiday”, “There will be full moon tonight” are not the statements because we are not sure which day or night we are talking about.“If today is Tuesday then tomorrow will be Sunday” is a statement because we are sure that it is false.Wednesday come after Tuesday so if today is Tuesday then tomorrow will be Wednesday."]
			},
			{	"questionNumber":5,
				"question":"Which of the following is a statement?  ",
				 "options":["There are 27 days in this month","February has 28 days","February has 29 days","There are 32 days in this month"],
				 "answer": [4, "When we talk about this, that, here, there, we are not sure about what we are talking about so “There are 27 days in this month” is not a statement.“February has 28 days” and “February has 29 days” both are not statements because February may have 28 days or 29 das based on the year. “There are 32 days in this month” is a statement as it is false. We cannot have 32 days in a month."]
			},
			{	"questionNumber":6,
				"question":"Which of the following is not a statement?  ",
				 "options":["Product of 1 and 2 is -4","Squares are always positive"," Give me a cup of tea","Sum of 2 and 3 is 9"],
				 "answer": [3, " “Product of 1 and 2 is -4” is a statement as it is false. We know, product of 1 and 2 is 2.“Squares are always positive” is a statement as it is true. “Sum of 2 and 3 is 9” is a statement as it is false. But “Give me a cup of tea” is not a statement as it is an order so it is imperative sentence."]
			},
			{	"questionNumber":7,
				"question":"Which of the following is true?  ",
				 "options":["Statements generally not use word like today and tomorrow","Statements generally not use word like here and there","Statements generally not use word like sum and product","Statements generally not use word like this and that"],
				 "answer": [3, "Statements generally not use ambiguous words like here, there, this, that, today, tonight, tomorrow."]
			},
			{	"questionNumber":8,
				"question":"Which of the following is a statement?  ",
				 "options":["Close the door","11 comes after 12"," India is a beautiful country","This is useless"],
				 "answer": [2, "“Close the door” is not a statement as it is an imperative sentence. “11 comes after 12”is a statement as it is true. “India is a beautiful country” is not a statement as opinion of beautifulness vary from person to person. “This is useless” is not a statement as it involves this which doesn’t give any idea about what we are talking."]
			},
			{	"questionNumber":9,
				"question":"The denial of statement is called  ",
				 "options":["negation","contradiction","contrapositive"," compound"],
				 "answer": [1, "The denial of statement is known as negation of the statement. It is denoted by ~p if statement is denoted by p."]
			},
			{	"questionNumber":10,
				"question":"Which of the following cannot be the negation of the statement “Delhi is in India”?  ",
				 "options":["Delhi is not in India","It is false that Delhi is in India"," It is false that Delhi is not in India","t is not the case that Delhi is in India"],
				 "answer": [3, "“Delhi is not in India”, “It is false that Delhi is in India”, “It is not the case that Delhi is in India” are negations of the given statement. Negation of a statement can be formed by adding ‘it is false that’ or ‘it is not the case that’. In statement “It is false that Delhi is not in India” two negation phrases are used which is wrong so it is not the negation statement."]
			},
			{	"questionNumber":11,
				"question":"People need Aadhar card or voter id to apply for Ration card. Which phrase is used?  ",
				 "options":["And","Exclusive Or","Inclusive Or","For all"],
				 "answer": [3, "Since people can have both Aadhar card and voter id. In such case also, they are eligible to apply for Ration card so phrase used is inclusive or."]
			},
			{	"questionNumber":12,
				"question":"Identify the type of Or and whether the statement “2 is a prime number or even number” is true or not?  ",
				 "options":["Inclusive Or, true","Exclusive Or, true","Inclusive Or, false","Exclusive Or, false"],
				 "answer": [1, "2 is a prime number as well as even number. Since for the statement to be true, we need at least one to be true so it is true. Since both are correct so or used is Inclusive."]
			},
			{	"questionNumber":13,
				"question":"Students can take English or Hindi as fifth subject. Which phrase is used?  ",
				 "options":["And"," Exclusive Or"," Inclusive Or","For all"],
				 "answer": [2, "Students can take any one of English and Hindi as fifth subject so phrase used in the give statement is Exclusive Or."]
			},
			{	"questionNumber":14,
				"question":"If all the component statements cannot be true simultaneously then ‘Or’ is said to be   ",
				 "options":["Inclusive Or","Exclusive Or","Inclusive And","Exclusive And"],
				 "answer": [2, "If all the component statements can be true simultaneously then ‘Or’ is said to be ‘Exclusive Or’."]
			},
			{	"questionNumber":15,
				"question":"Which of the following compound statement has both true component statements?  ",
				 "options":["A prime number is divisible by 2 and odd","Two and two makes four or five","All integers are positive and divisible by 2"," 100 is divisible by 2 and 5"],
				 "answer": [4, "Prime number is not divisible by 2 always. Two and two makes our not five. All integers are not positive. 100 is divisible by 2 and 5 both. So, component statements of “100 is divisible by 2 and 5” are true."]
			},
			{	"questionNumber":16,
				"question":"A rectangle is a quadrilateral and its four sides are equal. Which is not correct?  ",
				 "options":["A rectangle is a quadrilateral is false","A rectangle has four sides is true","A rectangle is a quadrilateral is true","A rectangle has all sided equal is false"],
				 "answer": [1, "A rectangle has four sides so it is a quadrilateral. All the four sides are not equal as two are equal and other two are equal."]
			},
			{	"questionNumber":17,
				"question":"Connect “0 is positive number” and “0 is a negative number”?  ",
				 "options":["0 is a positive or negative number","0 is a positive and negative number"," 0 is either positive or negative number","0 is neither positive nor negative number"],
				 "answer": [1, "0 is a positive or negative number” is formed by connecting the given statements using or."]
			},
			{	"questionNumber":18,
				"question":" Which of the following is not negation of statement “Sum of 2 and 3 is greater than 4”?  ",
				 "options":[" Sum of 2 and 3 is smaller than 4","Sum of 2 and 3 is smaller than or equal to 4","Sum of 2 and 3 is not greater than 4","Sum of 2 and 3 is not greater than 4"],
				 "answer": [1, "Negation of greater is ‘not greater’. ‘Not greater’ means either smaller than or equal to. So, “Sum of 2 and 3 is smaller than or equal to 4”, “Sum of 2 and 3 is not greater than 4”, “Sum of 2 and 3 is not greater than 4” are negation of the given statement. And “Sum of 2 and 3 is smaller than 4” is not the negation of given statement as it should include equal to also."]
			},
			{	"questionNumber":19,
				"question":"Which of the following cannot be the negation of the statement “All angles are equal in equilateral triangle”?  ",
				 "options":["There is at least one angle different in equilateral triangle","It is false that all angles are equal in equilateral triangle"," It is not the case that all angles are equal in equilateral triangle","All angles are unequal in equilateral triangle"],
				 "answer": [4, "Negation of all angles is ‘not all angles’. So, negation of the given statement is “There is at least one angle different in equilateral triangle”, “It is false that all angles are equal in equilateral triangle”, “It is not the case that all angles are equal in equilateral triangle”. But “All angles are unequal in equilateral triangle” cannot be the negation of given statement as this does not include isosceles triangles."]
			},
			{	"questionNumber":20,
				"question":" Which of the following cannot be the negation of the statement “Everyone in India speaks Hindi”?  ",
				 "options":["Not everyone in India speaks Hindi"," No person in India speaks Hindi","Someone in India does not speaks Hindi","At least one person in India who does not speaks Hindi"],
				 "answer": [2, "Negation of everyone is not everyone. So, negation of the given statement should be “Not everyone in India speaks Hindi”, “Someone in India does not speaks Hindi”, “At least one person in India who does not speaks Hindi”. “No person in India speaks Hindi” cannot be the negation of the given statement as this means no one speaks Hindi which does not means not everyone."]
			}
			]
		 },
		{
    	"ChapterName":"Statistics",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"If the standard deviation of a data is 0.012. Find the variance. ",
				 "options":["0.144","0.00144","0.000144","0.0000144"],
				 "answer": [3, " S.D. = √variance⇒ (0.012)2 = Variance⇒ Variance = 0.000144"]
			},
			{	"questionNumber":2,
				"question":"The mean of two samples of the sizes 250 and 320 were found to be 20,12 respectively. Their standard deviations were 2 & 5, respectively. Find the variance of combined sample of size 650. ",
				 "options":["10.23","32.5"," 65"," 26.17"],
				 "answer": [4, "Combined Mean = X = (n1x1 + n2x2)/(n1 + n2) = (250 × 20 + 320 × 12)/650 = 13.6 Let d1 = x1 – X = 20-13.6 = 6.4, d2 = x2 – X = 12-13.6 = -1.6 Variance = [250(6.4 + 40.96) + 320(13.6 + 2.56)]/650 = 26.17."]
			},
			{	"questionNumber":3,
				"question":"Find the variance of the first 10 natural numbers. ",
				 "options":[" 7.25","7"," 8.25"," 8"],
				 "answer": [3, "Variance = 1/10 [12 + 22 +…+ 102] – 120[1 + 2 +…. 10]2 = 38.5 – 30.25 = 8.25."]
			},
			{	"questionNumber":4,
				"question":"If the standard deviation of the numbers 2, 4, 5 & 6 is a constant a, then find the standard deviation of the numbers 4, 6, 7 & 8. ",
				 "options":["a + 2","2a","4a","a"],
				 "answer": [4, "The standard deviation is independent of the change of origin. So, the standard deviation for the new set will remain the same."]
			},
			{	"questionNumber":5,
				"question":" Assuming the variance of four numbers w, x, y, and z as 9. Find the variance of 5w, 5x, 5y and 5z. ",
				 "options":[" 225","5/9","9/5","54"],
				 "answer": [1, "(σx)2 = h2(σu)2, if u = (x – h)/a Now, h = (1/5). ⇒ Variance, (σu)2 = 9 × 25 = 225"]
			},
			{	"questionNumber":6,
				"question":"A fisherman is weighing each of 50 fishes. Their mean weight worked out is 50 gm and a standard deviation of 2.5 gm. Later it was found that the measuring scale was misaligned and always under reported every fish weight by 2.5 gm. Find the mean and standard deviation of fishes. ",
				 "options":["52.5,2.5","30,5","50,5","48.5,2.5"],
				 "answer": [1, " Since mean(X + b) = meanX + b and Var(X + b) = VarX, so we get correct mean as 50 + 2.5 = 52.5 gm and S.D. is 2.5 gm."]
			},
			{	"questionNumber":7,
				"question":" What is the median and standard deviation of a distribution are 50 and 5 respectively, if each item is increased by 4. ",
				 "options":["Median will increase and S.D. will increase","Both will remain same","median will go up by 2 but S.D. will remain same","median will increase and S.D. will decrease"],
				 "answer": [3, "Median will change if the observations are changes but standard deviation is unaffected by the origin. So, here the median will go up by 4 and S.D. will remain same."]
			},
			{	"questionNumber":8,
				"question":"If the S.D. is a set of observations is 4 and if each observation is divided by 4, find the S.D. of the new observations. ",
				 "options":["4","3","2""1"],
				 "answer": [4, " σ1 = 4 and d = (X – 0)/4 And σ1 = |4|σd ⇒ σd = 4/4 = 1."]
			},
			{	"questionNumber":9,
				"question":"The change in which of following terms does not affect the standard deviation? ",
				 "options":["Origin","Scale","Origin and scale","Neither origin nor scale"],
				 "answer": [1, " Change in origin does not affect the standard deviation, whereas standard deviation is affected by scale."]
			},
			{	"questionNumber":10,
				"question":"The mean and Standard deviation of a sample were found to be 9.5 and 2.5, respectively. Later, an additional observation 15 was added to the original data. Find the S.D. of the 11 observation. ",
				 "options":[" 2.6","2.8","2.86","3.24"],
				 "answer": [3, "1n  (Σ xi) = 9.5,1/n (Σ [(xi)2 – (X)2] = 6.25, Σ xi = 95 and 110 Σ[(X)2] = 96.5Corrected mean = (95 + 15)/11 = 10Corrected Variance = [(1/11) x (965 + 225)] – 100 = 90/11⇒ Standard deviation = √Variance = √(90/11) = 2.86."]
			},
			{	"questionNumber":11,
				"question":"The mean of 5 observations is 3 and variance is 2. If three of the five observations are 1, 3, 5, find the other two ",
				 "options":["2, 6","3, 3","1, 5","2, 4"],
				 "answer": [4, "15 (Σ xi) = 3 = 1 + 3 + 5 + x4 + x5⇒ x4 + x5 = 15 ———— (i)Now, 15 Σ (xi)2 – [15 Σ xi]2 = 4⇒ (x4)2 + (x5)2 = 30 —————-(ii)Solving equation i and ii, x4 = 2 and x5 = 4."]
			},
			{	"questionNumber":12,
				"question":"If the coefficient of variation is 100 the mean of the data is 25, then find the standard deviation. ",
				 "options":["5","10","15","25"],
				 "answer": [4, " Coefficient of Variance = (Standard Deviation/Mean) × 100⇒ Standard Deviation = 25."]
			},
			{	"questionNumber":13,
				"question":" If the standard deviation of a data is 820 and mean of the data is 50, find the coefficient of variation. ",
				 "options":["16.4"," 164","1640","1.64"],
				 "answer": [1, "Coefficient of Variance = (Standard Deviation/Mean) × 100⇒ Coefficient of Variance = (820/50) × 100 = 16.4."]
			},
			{	"questionNumber":14,
				"question":"If standard deviation of a data is 40 and the coefficient of variation is 25600, then find the mean. ",
				 "options":["64","6.4","640","0.64"],
				 "answer": [2, "Coefficient of Variance = (Standard Deviation/Mean) × 100⇒ Mean = 25600/4000 = 6.4."]
			},
			{	"questionNumber":15,
				"question":"The mean deviation of an ungrouped data is 150. If each observation is increased by 3.5%, then what is the new mean deviation? ",
				 "options":["153.5","3.5","155.25","150"],
				 "answer": [3, "If x1, x2, …, xn are the observations, then the new observations are (1.035) x1, (1.035) x2, ……, (1.035) xn.Therefore, the new mean is (1.035) x̄Now, Mean deviation = 1n[Σi = n |xI – mean|]⇒ New mean deviation = 1n[Σi = n|(1.035)xI – (1.035) x̄|] = (1.035) × 1n[Σi = n |xI – mean|] = 1.035 x 150 = 155.25."]
			},
			{	"questionNumber":16,
				"question":"What is the geometric mean of 5,52, ….,5n? ",
				 "options":["5^n/2","5^(n+1)/2"," 5^n(n+1)/2","5^n"],
				 "answer": [2, "Geometric Mean = (5 x 52 x …… x 5n)1/n = [5(1+2+…+n)]1/n = [5n(n+1)/2]1/n = 5^(n+1)/2."]
			},
			{	"questionNumber":17,
				"question":"In a class there are 20 juniors, 15 seniors and 5 graduate students. If the junior averaged 65 in the midterm exam, the senior averaged 70 and the graduate students averaged 91, then what is the mean of the centre class approximately? ",
				 "options":["71","74","70","72"],
				 "answer": [3, "Combined mean = (Σ xini)/(Σ ni) = (20 × 65 + 15 × 70 + 5 × 91)/(20 + 15 + 5) = 70."]
			},
			{	"questionNumber":18,
				"question":"Find the mean deviation from mean of the observations: a, a+d, …., (a+2nd). ",
				 "options":["n(n + 1)d^2/3","n(n + 1)d^2/2","a + n(n + 1)d^2/2","n(n + 1)d/(2n + 1)"],
				 "answer": [4, "Mean = 1n Σ xi = 12n+1 [a + (a + d) + … + (a + 2nd)] = a + nd⇒ Mean Deviation = 12n+1 [2 × d × (1 + 2 + … + n)] = [n (n + 1) (d)]/(2n + 1)."]
			},
			{	"questionNumber":19,
				"question":"Find the variance of the observation values (4.2,4.3,4,4.1) ",
				 "options":[" 0.27"," 0.28","0.3","0.31"],
				 "answer": [2, "X = (4.2 + 4.3 + 4 + 4.1)/4 = 4.15,Variance = 1n Σ (xi – X)2 = 1.11/4 = 0.28"]
			},
			{	"questionNumber":20,
				"question":"An analysis of the monthly wages paid to the workers of a form is given below. Calculate the total monthly wages.No. of workers=100,Average monthly wages=280,Variance of distribution of wages=10 ",
				 "options":["2800","280","28000","2.8"],
				 "answer": [3, " Number of wage earners (n1) = 100Mean of monthly wages (X1) = ₹280Mean of monthly wages = Total monthly wage/Number of workers⇒ 280 = total monthly wages/100⇒ Total monthly wages = 28000."]
			}
		]
        },
		{
    	"ChapterName":"Probability",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"Probability is ",
				 "options":["Number of outcomes in favour of event","Total number of possible outcomes","Ratio of number of outcomes in favour to total number of outcomes","Ratio of total number of outcomes to number of outcomes in favour"],
				 "answer": [3, "Probability is chance of an outcome to appear. It is the ratio of number of outcomes in favour to total number of outcomes."]
			},
			{	"questionNumber":2,
				"question":" Probability of getting head on an unbiased coin is",
				 "options":["1/4","1","0","1/2"],
				 "answer": [4, "An unbiased coin can have head or tail as outcome i.e. there are two possible outcomes.So, probability of getting head on an unbiased coin is 1/2."]
			},
			{	"questionNumber":3,
				"question":"Probability of getting tail on an unbiased coin is",
				 "options":["1/4","1","0","1/2"],
				 "answer": [4, "An unbiased coin can have head or tail as outcome i.e. there are two possible outcomes.So, probability of getting tail on an unbiased coin is 1/2."]
			},
			{	"questionNumber":4,
				"question":"Probability of getting an even number on dice is ",
				 "options":["1","1/2","1/3","0"],
				 "answer": [2, "There are six possible outcomes on dice i.e. 1 to 6.Even numbers on dice are 2,4,6 i.e. three outcomes in favour of the event.So, probability of getting an even number on dice is 3/6 = 1/2."]
			},
			{	"questionNumber":5,
				"question":"Probability of getting an odd number on dice is",
				 "options":["1","1/2","1/3","0"],
				 "answer": [2, "There are six possible outcomes on dice i.e. 1 to 6.Odd numbers on dice are 1,2,3 i.e. three outcomes in favour of the event.So, probability of getting an odd number on dice is 3/6 = 1/2."]
			},
			{	"questionNumber":6,
				"question":"Probability of getting prime number on dice is ",
				 "options":["1/2","1/4","1/3","1"],
				 "answer": [1, "There are six possible outcomes on dice i.e. 1 to 6.Prime numbers on dice are 2,3,5 i.e. three outcomes in favour of the event.So, probability of getting a prime number on dice is 3/6 = 1/2."]
			},
			{	"questionNumber":7,
				"question":"Probability of getting composite number on dice is",
				 "options":["1/2","1/4","1/3","1"],
				 "answer": [3, "There are six possible outcomes on dice i.e. 1 to 6.Composite numbers on dice are 4,6 i.e. two outcomes in favour of the event.So, probability of getting a composite number on dice is 2/6 = 1/3."]
			},
			{	"questionNumber":8,
				"question":" Probability of getting 7 on a dice is",
				 "options":["1/2","0","1","1/3"],
				 "answer": [2, "There are six possible outcomes on dice i.e. 1 to 6.7 does not appear on a dice so probability of getting 7 on a dice is zero."]
			},
			{	"questionNumber":9,
				"question":"If two coins are tossed simultaneously what are total number of possible outcomes?",
				 "options":["2","4","6","8"],
				 "answer": [2, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH}"]
			},
			{	"questionNumber":10,
				"question":" If two coins are tossed simultaneously what is the probability of getting exactly one head?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [1, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {HT, TH} favour the event.So, probability of getting exactly one head = 2/4 = 1/2."],
			},
			{	"questionNumber":11,
				"question":"If two coins are tossed simultaneously what is the probability of getting exactly one tail?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [1, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {HT, TH} favour the event.So, probability of getting exactly one tail = 2/4 = 1/2."],
			},
			{	"questionNumber":12,
				"question":"If two coins are tossed simultaneously what is the probability of getting at least one head?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [4, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {HH, HT, TH} favour the event.So, probability of getting at least one head = 3/4."],
			},
			{	"questionNumber":13,
				"question":"If two coins are tossed simultaneously what is the probability of getting at most one head?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [4, " If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {HT, TH, TT} favour the event.So, probability of getting at most one head = 3/4."],
			},
			{	"questionNumber":14,
				"question":"If two coins are tossed simultaneously what is the probability of getting all heads?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [3, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {HH} favour the event.So, probability of getting all heads = 1/4."],
			},
			{	"questionNumber":15,
				"question":"If two coins are tossed simultaneously what is the probability of getting no heads?",
				 "options":["1/2","1/3","1/4","3/4"],
				 "answer": [3, "If two coins are tossed simultaneously total number of possible outcomes are 4.{HH, TT, HT, TH} out of which {TT} favour the event.So, probability of getting no heads = 1/4."],
			},
			{	"questionNumber":16,
				"question":"If 4 bulbs are there each of which can be defective or non-defective then what is the probability that at least one bulb is non- defective?",
				 "options":["7/8","15/16","3/4","1/2"],
				 "answer": [2, "Each bulb can have two cases i.e. either defective or non-defective. Then total number of outcomes will be 24 = 16.Probability that all the bulbs are defective is 1/16.So, the probability that at least one bulb is non-defective is 1-1/16 = 15/16."]
			},
			{	"questionNumber":17,
				"question":"If 4 bulbs are there each of which can be defective or non-defective then what is the probability that all the bulbs are defective?",
				 "options":["1/8","1/16","1/4","1/2"],
				 "answer": [2, "Each bulb can have two cases i.e. either defective or non-defective. Then total number of outcomes will be 24 = 16.So, the probability that all the bulbs are defective is 1/16."]
			},
			{	"questionNumber":18,
				"question":" If 4 bulbs are there each of which can be defective or non-defective then what is the total number of possible outcomes?",
				 "options":["8","16","4","2"],
				 "answer": [2, "Each bulb can have two cases i.e. either defective or non-defective. Then total number of outcomes will be 24 = 16."]
			},
			{	"questionNumber":19,
				"question":"A coin is tossed and if head come then a red dice is rolled and if tail come then a blue dice is rolled then what is the possible number of outcomes?",
				 "options":["6","12","24","72"],
				 "answer": [2, "If head come on coin then red dice can have 6 outcomes so total 1*6 = 6 outcomes. And if tail come on coin then blue dice can have 6 outcomes so total 1*6 = 6 outcomes.So, total number of possible outcomes = 6 + 6 = 12."]
			},
			{	"questionNumber":20,
				"question":"A coin is tossed and a dice is rolled simultaneously what is total number of possible outcomes?",
				 "options":["2","6","12","24"],
				 "answer": [3, "If a coin is tossed and a dice is rolled simultaneously then total number of possible outcomes will be 2*6 =12."]
			}
			
		]
        },
		{
    	"ChapterName":"Differentiation",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":" The pedal Equation of the polar curve rn=an cos⁡nθ is given by ",
				 "options":["r^n=pa^n","r^n-1=pa^n","r^n+1=pa^n+1","r^n+1=pa^n"],
				 "answer": [4, "Taking logarithm for the given curve we get n log⁡r = n log⁡a + log⁡(cos⁡nθ) differentiating w.r.t θ, we get nrdrdθ=−nsinnθcosnθ→1rdrdθ=−tanθ thus cot∅=cot(π2+nθ)→∅=π2+nθ……(1) from the eqn w.k.t p=r sin ∅ substituting from (1) p = r sin (π2 + nθ) = r cos (nθ), but we have rn = an cos⁡nθ hence dividing them we get prn=rcos(nθ)ancosnθ r^n+1=pa^n."]
			},
			{	"questionNumber":2,
				"question":"Angle of intersection between two polar curves given by r=a(1+sin⁡θ) & r=a(1-sin⁡θ) is given by",
				 "options":["π/4","π/2","Π","0"],
				 "answer": [2, "r=a(1+sin⁡θ) : r=a(1-sin⁡θ) taking logarithm on both the equationslog⁡r = log⁡a + log⁡(1+sin⁡θ) : log⁡r = log⁡a + log⁡(1-sin⁡θ)differentiating on both side we get1/r.dr/dθ=cosθ1+sinθ:1/r.dr/dθ=−cosθ1−sinθcot∅1=cosθ1+sinθ:cot∅2=−cosθ1−sinθ,where ∅1&∅2 are the angle between tangent & the vector respectivelytan∅1=1+sinθcosθ:tan∅2=1−sinθcosθ tan∅1.tan∅2=1+sinθcosθ.1−sinθ−cosθ=1−sin2θ−cos2θ=−cos2θcos2θ=−1 above is the condition of orthogonality of two polar curves thus |∅1-∅2|=π2."]
			},
			{	"questionNumber":3,
				"question":"One among the following is the correct explanation of pedal equation of an polar curve, r=f (θ), p=r sin(∅) (where p is the length of the perpendicular from the pole to the tangent & ∅ is the angle made by tangent to the curve with vector drawn to curve from pole)is ",
				 "options":["It is expressed in terms of p & θ only"," It is expressed in terms of p & ∅ only","It is expressed in terms of r & θ only","It is expressed in terms of p& r only"],
				 "answer": [4, "It is expressed in terms of p& r only where p=r sin(∅) & tan∅=rdrdθ=r(drdθ) & r=f (θ) or after solving we get direct relationship between p & r as 1/p2=1/r2cosec2∅."]
			},
			{	"questionNumber":4,
				"question":"The length of the perpendicular from the pole to the tangent at the point θ=π2 on the curve. r=a sec2(π2) is",
				 "options":["p=2a√3","p=4a√3"," p=2a√2","p = 4a"],
				 "answer": [3, "Taking Logarithm on both side of the polar curve we get log⁡r = log⁡a + 2 log⁡sec⁡(θ2),differentiating w.r.t θ we get,1/rdrdθ=2sec(θ2).tan(θ2)2sec(θ2)=tan(θ2),cot∅=cot(π2–θ2)→∅=π2−θ2,w.k.t length of the perpendicular is given by p=r sin ∅,thus substituting ∅ value we get p=rsin(π2–θ2)=rcos(θ2),at θ=π4,p=rcosπ4=r2√….(1),but r=asec2(θ2)atθ=π4,r=asec2(π4)=4a…(2),from (1) & (2) p=4a√2=2a√2."]
			},
			{	"questionNumber":5,
				"question":" Polar equations of the circle for the given coordinate (x,y) which satisfies the equation given by (x-a)2+(y-b)2=r2 where (a,b) is the coordinates of the centre of the circle &r is the radius.",
				 "options":[" x = r cos⁡θ, y = r sin⁡θ","x = a+ r cos⁡θ, y = b + r sin⁡θ"," y = a+r cos⁡θ, x = b + r sin⁡θ","x = r sin⁡θ, y = r cos⁡θ"],
				 "answer": [2, "option x = a+ r cos⁡θ, y = b + r sin⁡θ satisfies the equation (x-a)2+(y-b)2=r2 because LHS=(a+r cos⁡θ-a)2 + (b+ r sin⁡θ-b)2 = r2(cos2 θ + sin2 θ)= r2=RHS."]
			},
			{	"questionNumber":6,
				"question":" In an polar curve r=f (θ) what is the relation between θ & the coordinates (x,y)?",
				 "options":["tan⁡θ = x/y","(1+sin⁡θ) = y/x","(1+sec2 θ) = y2/x2","(1+cos⁡θ) = x/y"],
				 "answer": [3, " w.k.t for the polar curve r=f (θ) x=rcos⁡θ, y=rsin⁡θ dividing them we get yx=rsinθrcosθ=tanθ squaring on both side y2x2=tan2θ=(1+sec2θ)."],
			},
			{	"questionNumber":7,
				"question":"The curvature of a function f(x) is zero. Which of the following functions could be f(x)?",
				 "options":["ax + b","ax^2 + bx + c","sin(x)","cos(x)"],
				 "answer": [1, " The expression for curvature is k=∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣ Given that k = 0 we have f” (x) = 0 f(x) = a + b."],
			},
			{	"questionNumber":8,
				"question":"The curvature of the function f(x) = x^2 + 2x + 1 at x = 0 is?",
				 "options":[" 3⁄2"," 2"," ∣∣∣2/5^3/2∣∣∣","0"],
				 "answer": [3, "The expression as we know is k=∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣ Substituting f(x)=x^2+2x+1 we have k=∣∣∣2(1+[2x+2]2)32∣∣∣ Put x=0 to get k=∣∣∣2(1+[2]2)32∣∣∣ k=∣∣∣2/5^3/2∣∣∣"]
			},
			{	"questionNumber":9,
				"question":" Find the curvature of the function f(x) = 3x3 + 4680x2 + 1789x + 181 at x = -520.",
				 "options":[" 1","0","∞","-520"],
				 "answer": [4, "For a Cubic polynomial the curvature at x = -b⁄3a is zero because f”(x) is zero at that point. Looking at the form of the given point we can see that x = -4680⁄3*3 = -520 Thus, curvature is zero."]
			},
			{	"questionNumber":10,
				"question":" Let c(f(x)) denote the curvature function of given curve f(x). The value of c(c(f(x))) is observed to be zero. Then which of the following functions could be f(x).",
				 "options":["f(x) = x^3 + x + 1"," f(x)^2 + y^2 = 23400","f(x) = x^19930 + x + 90903","No such function exist"],
				 "answer": [2, "We know that the curvature of a given circle is a constant function. Further, the curvature of any constant function is zero. Thus, we have to choose the equation of circle from the options."]
			},
			{	"questionNumber":11,
				"question":" The curvature of the function f(x) = x3 – x + 1 at x = 1 is given by?",
				 "options":["∣6⁄5∣","∣3⁄5∣"," ∣∣∣6/5^3/2∣∣∣"," ∣∣∣3/5^3/2∣∣∣"],
				 "answer": [3, "Using expression for curvature we have k=∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣ Substituting f(x)=x3-x+1 we have k=∣∣∣2(1+[3x^2−1]2)32∣∣∣ Put x=1 to get k=∣∣∣6/5^3/2∣∣∣"]
			},
			{	"questionNumber":12,
				"question":"The curvature of a function depends directly on leading coefficient when x=0 which of the following could be f(x)?",
				 "options":[" y = 323x^3 + 4334x + 10102"," y = x^5 + 232x^4 + 232x^2 + 12344","y = ax^5 + c","y = 33x2 + 112345x + 8945"],
				 "answer": [4, "Using formula for curvature k=∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣ Observe numerator which is f”(x) Now this second derivative must be non zero for the above condition asked in the question Looking at all the options we see that only quadratic polynomials can satisfy this."]
			},
			{	"questionNumber":13,
				"question":"Given x = k1ea1t : y = k2ea2t it is observed that the curvature function obtained is zero. What is the relation between a1 and a2?",
				 "options":["a1 ≠ a2","a1 = a2","a1 = (a2)^2","a2 = (a1)^2"],
				 "answer": [2, "Using formula for Curvature in parametric form k=∣∣∣y”x′−y′x”((x′)2+(y′)2)32∣∣∣ Equating y”x’-y’x” to zero (given curvature function is zero) we get y”y′=x”x′ Put x=k1ea1t:y=k2ea2t k1(a1)2.ea1tk1.a1.ea1t=k2(a2)2.ea2tk2.a2.ea2t a1=a2"]
			},
			{	"questionNumber":14,
				"question":"The curvature function of some function is given to be k(x) = 1[2+2x+x2]32 then which of the following functions could be f(x)?",
				 "options":[" x2⁄2 + x + 101","x2⁄4 + 2x + 100","x2 + 13x + 101","x3 + 4x2 + 1019"],
				 "answer": [1, "The equation for curvature is k(x) = ∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣Observe that there is no term in the numerator of given curvature function. Hence, the function has to be of the quadratic form. Using f(x) = ax2+bx+c we have k=∣∣∣2a[1+(2a+b)2]32∣∣∣=∣∣∣1[2+2x+x2]32∣∣∣ ∣∣∣2a[1+(2ax+b)2]32∣∣∣=∣∣∣1[1+(x+1)2]32∣∣∣ 2a = 1; b = 1 The values of a, b are a = 1⁄2; b = 1c Could be anything."]
			},
			{	"questionNumber":15,
				"question":" Consider the curvature of the function f(x) = ex at x=0. The graph is scaled up by a factor of and the curvature is measured again at x=0. What is the value of the curvature function at x=0 if the scaling factor tends to infinity?",
				 "options":["a","2","1","0"],
				 "answer": [4, "If the scaling factor is a then the function can be written as f(x) = eax Now using curvature formula we have ∣∣∣f”(x)(1+[f′(X)]2)32∣∣∣=∣∣∣a2.eax[1+a2.e2ax]32∣∣∣ Put x=0 =∣∣∣a2[1+a2]32∣∣∣ Now taking the limit as a → ∞ we get =lta→∞a2a3.[1+1a2]32 =lta→∞1a.[1+1a2]32 =0"]
			},
			{	"questionNumber":16,
				"question":"The name of the evolute of an ellipse is ",
				 "options":["Centroid","Astroid","Asteroid"," Cycloid"],
				 "answer": [2, "Astroid is known as the evolute of ellipse whereas centroid is associated with triangle. Asteroids are small planet like structures found in space. Cycloid is the curve traced by a point on the circumference of a circle."]
			},
			{	"questionNumber":17,
				"question":" The curvature of a curve is equal to",
				 "options":["Reciprocal of radius of curvature"," Radius of Curvature"," Twice the radius of curvature","One"],
				 "answer": [1, "Curvature is the property of a curve by which the curve deviates from that of a straight line. It is equal to the reciprocal of the radius of curvature of the curve. The radius of curvature is equal to the radius of the curve by magnitude."]
			},
			{	"questionNumber":18,
				"question":"Involute is also known as ",
				 "options":[" Evolute","Evolvent","Envelope","Tangent"],
				 "answer": [2, " The curve itself is the involute of the evolute of the curve with a known starting point. The other name for involute is evolvent."]
			},
			{	"questionNumber":19,
				"question":"What is the evolute of parabola called?",
				 "options":["Cycloid","Spiral","Congruent parabola","Semicubical parabola"],
				 "answer": [4, "The evolute of parabola is called semicubical parabola. It is defined parametrically as x=t2 and y=at3."]
			},
			{	"questionNumber":20,
				"question":" Definition of evolute of a curve is",
				 "options":["locus of centre of the given curve","locus of centre of tangential curve"," locus of circumferential point on the curve","locus of tangent to the curve"],
				 "answer": [1, "The evolute of a curve is defined as the locus of centre of the given curve. It is the path traced by the centre of the curve."]
			}
			
			

		]
        },
		{
    	"ChapterName":"Integration",
		"questionSet":
		[
			{	"questionNumber":1,
				"question":"Integrate xe^2x.",
				 "options":["e^2x/4(x−14)+C","e^2x/4(2x−1)+C","e^2x/2(2x−1)+C","e^2x/4(x+1)+C"],
				 "answer": [2, "By using the formula ∫u.vdx=u∫vdx−∫u′(∫vdx) we get ∫xe2xdx=x∫e2xdx−∫(x)′∫e2xdx =xe2x2−∫1.e2x2dx =xe2x2−e2x4 =e2x4(2x−1)+C"]
			},
			{	"questionNumber":2,
				"question":"Find ∫ 7 log⁡x.x dx",
				 "options":["7/2(logx−x)+C","–7/2(x2logx−x3)+C","7/2(x2logx−x)+C","(x2 log⁡x+x)+C"],
				 "answer": [3, "∫ 7 log⁡x.x dx=7∫ log⁡x.x dx Using ∫ u.v dx=u∫ v dx-∫ u'(∫ v dx) , we get 7∫ log⁡x.x dx=7(log⁡x ∫ x dx-(log⁡x)’∫ x dx) =7(x2logx2−1x.x^2/2)=7/2(x2logx−x)+C"],
			},
			{	"questionNumber":3,
				"question":"Find ∫ sin⁡x log⁡(cos⁡x) dx.",
				 "options":["cos⁡x (log⁡(sin⁡x)-1)+C","sin⁡x (log⁡(cos⁡x)+1)+C"," cos⁡x (log⁡(cos⁡x)-1)+C"," cos⁡x (log⁡(cos⁡x)-1)+C"],
				 "answer": [3, "Let cos⁡x=t Differentiating w.r.t x, we get -sin⁡x dx=dt sin⁡x dx=-dt ∴∫ sin⁡x log⁡(cos⁡x) dx=∫ -log⁡t dt Using ∫ u.v dx=u∫ v dx-∫ u’ (∫ v dx) , we get ∫ -log⁡t dt=-log⁡t ∫ 1 dt-∫ (-log⁡t)’ ∫ 1 dt =-t log⁡t+∫ dt =-t log⁡t+t =t(log⁡t-1) Replacing t with cos⁡x, we get ∫ sin⁡x log⁡(cos⁡x) dx=cos⁡x (log⁡(cos⁡x)-1)+C"]
			},
			{	"questionNumber":4,
				"question":"Integrate 5x sin⁡3x.",
				 "options":["–5/3xcos3x+5/9tan3x+C","5/3cos3x−5/9sin3x+C","xcos3x+5/9sin3x+C","–5/3xcos3x+5/9sin3x+C"],
				 "answer": [4, "By using the formula, ∫ u.v dx=u∫ v dx-∫ u’ (∫ v dx) ,we get ∫ 5x sin⁡3x dx=5x∫ sin⁡3x dx -∫ (5x)’∫ sin⁡3x dx =5x(−cos3x3)+∫5cos3x3dx =-53xcos3x+59sin3x+C"]
			},
			{	"questionNumber":5,
				"question":"Find ∫ 2x3 ex2 dx.",
				 "options":["-ex2 (x2+2)+C","ex2 (x2-1)+C",") 2ex2 (x2+1)+C"," ex2 (x-1)+C"],
				 "answer": [2, "Let x2=t Differentiating w.r.t x, we get 2x dx=dt ∴∫ 2x2 ex2 dx=∫ tet dt By using the formula, ∫ u.v dx=u∫ v dx-∫ u’ (∫ v dx) ,we get ∫ t et dt=t∫ et dt-∫ (t)’∫ et dt =tet-∫ et dt =tet-et=et (t-1) Replacing t with x2, we get ∫ 2x3 ex2 dx=ex2 (x2-1)+C"]
			},
			{	"questionNumber":6,
				"question":" In ∫baf(y) dy, what is ‘a’ called as?",
				 "options":["Integration"," Upper limit","Lower limit","Limit of an integral"],
				 "answer": [2, " In ∫baf(y) dy ‘a’ is the called as lower limit and ‘b’ is called the upper limit of the integral. The fuction f in ∫baf(y) dy is called the integrand. The letter ‘y’ is a dummy symbol and can be replaced by any other symbol."]
			},
			{	"questionNumber":7,
				"question":"Compute ∫cos(x)-3x4dx.",
				 "options":["sin(x)+3/4x-7+c"," sec(x)+3/4x-3+c","sin(x)+3/4x-3","sin(x)+3/4x-3+c"],
				 "answer": [4, " ∫cos(x)-3x4dx = ∫cos(x) dx−∫3(x-4) dx= sin(x)+34x-3+c"]
			},
			{	"questionNumber":8,
				"question":"What is the value of ∫32cos⁡(x)-3x4dx .",
				 "options":["sin (3) – sin (2)","sin (3) – sin (9) – 19/288","sin (8) – sin (2) – 19/288","sin (3) – sin (2) – 19/288"],
				 "answer": [4, "∫32 cos⁡(x)-3x4dx = ∫32sin(x) dx + ∫3234x-3 dx = (sin (3) + 343-3) – (sin (2) + 342-3) = sin (3) – sin (2) – 19288"]
			},
			{	"questionNumber":9,
				"question":"Evaluate ∫9/7cos⁡(x)dx.",
				 "options":["8 (-sin 9 – sin 7)"," 8 (sin 9 + sin 7)"," 8 (sin 9 – sin 7)","7 (sin 9 – sin 7)"],
				 "answer": [3, ": ∫9/7.8cos⁡(x)dx = 8 ∫9/7cos⁡(x)dx = 8 (cos x)9/7= 8 (sin 9 – sin 7)"]
			},
			{	"questionNumber":10,
				"question":"Compute ∫3/2cosx−sinx4dx.",
				 "options":["1/4  (sin 2 + cos 3 – sin 3 – cos 2)","1/4  (sin 3 – cos 3 – sin 2 – cos 2)","1/4  (sin 3 + cos 3 – sin 2 – cos 2)","1/4  (sin 3 + cos 3 + sin 2 – cos 2)"],
				 "answer": [3, "∫3/2cosx−sinx4dx = 1/4 [sin x – (- cos x)]3/2 = 1/4 (sin x + cos x)3/2 = 1/4 (sin 3 + cos 3) – 14 (sin 2 + cos 2) = 1/4 (sin 3 + cos 3 – sin 2 – cos 2)"]
			},
			{	"questionNumber":11,
				"question":"What is y in ∫baf(y) dy called as?",
				 "options":["Random variable","Dummy symbol ","Integral","Integrand"],
				 "answer": [2, "In ∫baf(y) dy ‘a’ is the called as lower limit and ‘b’ is called the upper limit of the integral. The fuction ‘f’ in ∫baf(y) dy is called the integrand. The letter ‘y’ is a dummy symbol and can be replaced by any other symbol."]
			},
			{	"questionNumber":12,
				"question":"The value of ∫211y5 dy is",
				 "options":["10.5","56","9","23"],
				 "answer": [1, " ∫211y5 dy = (y6/6)21= 646–16= 10.5"]
			},
			{	"questionNumber":13,
				"question":" The value of ∫211y5/5dy is ",
				 "options":["12","2.1"," 21","11.1"],
				 "answer": [2, "∫21 1y5/5dy = 15(y6/6)21= 15(646–16)= 2.1"]
			},
			{	"questionNumber":14,
				"question":" Evaluate ∫π0sin⁡x dx.",
				 "options":["2","6","17","3"],
				 "answer": [1, "∫π0 sin⁡x dx = [- cos x]x0= – cos π – (-cos 0)= -(-1)-(-1)= 2"]
			},
			{	"questionNumber":15,
				"question":"Evaluate ∫32cosx dx.",
				 "options":["38.2","sin (9) – sin (4)","89.21 ","sin (3) – sin (2)"],
				 "answer": [4, " ∫32cosx dx = (sin x)32= sin (3) – sin (2)"]
			},
			{	"questionNumber":16,
				"question":"Compute ∫322ex dx.",
				 "options":["2(e9 – e4)","84.32","2(e3 – e2)","83.25"],
				 "answer": [3, "∫32 2ex dx = 2(ex)32 dx= 2(e3 – e2)"]
			},
			{	"questionNumber":17,
				"question":" Compute ∫639 ex dx.",
				 "options":["30.82","9(e6 – e3)","11.23","81(e6 – e3)"],
				 "answer": [2, " ∫639 ex dx = 9(ex)63 dx= 9(e6 – e3)"]
			},
			{	"questionNumber":18,
				"question":"Evaluate ∫73sin(t)-2cos(t)dt.",
				 "options":[" cos(7) – 2sin(7) + (cos(3) + 2sin(3)","-17","12","cos(7) – 2sin(7) – (cos(3) + 2sin(3)"],
				 "answer": [4, "∫7/3sin(t)-2cos(t)dt = (cos(t)−2sin(t))73= (cos(7) – 2sin(7)) – (cos(3) – 2sin(3))= cos(7) – 2sin(7) – (cos(3) + 2sin(3)"]
			},
			{	"questionNumber":19,
				"question":"Find ∫80xdx.",
				 "options":["32","34","21","24"],
				 "answer": [1, " Let I=∫80xdx F(x)=∫xdx=x2/2 Using the second fundamental theorem of calculus, we get I=F(8)-f(0)∴∫80xdx=822−0=32"]
			},
			{	"questionNumber":20,
				"question":"Find ∫π205sinxdx.",
				 "options":["-5","9","5","-9"],
				 "answer": [3, "Let I=∫π205sinxdx F(x)=∫5sinxdx=−5cosx Applying the limits by using the fundamental theorem of calculus, we get I=F(π2)-F(0) ∴∫π205sinxdx=−5[cosπ2−cos0] =-5[0-1]=5"]
			}
			]
        }
]
		


rec=db.maths.insert_many(Maths)