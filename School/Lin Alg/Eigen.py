from sympy import Matrix , symbols , factor , pprint , I

 # Initialization of numeric matrix
A = Matrix ([[2 , 4 ] , [4 , 8]])
pprint ( A )

 # Characteristic polynomial
lamda = symbols ('lamda ')
p = A . charpoly ( lamda )
pprint ( p )

# Factored characteristic polynomial
p_fact = factor ( p . as_expr () , extension =[ I ])
pprint ( p_fact )

 # Eigenvalues
Aeigvals = A . eigenvals ()
pprint ( Aeigvals )