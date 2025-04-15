
# Programmatically Computing Derivatives of Polynomial Functions

This is an implementation of Forward Mode Automatic Differentiation to programmatically compute derivatives of polynomial functions.

Dual Numbers are a type of number system with a real component and an epsilon component. The trick with Dual Numbers is that for the epsilon component, E, E != 0 and E^2 = 0

Consider f(x) = 6x^2 + 7x

The derivative of the function is f'(x) = 12x + 7

To find the derivative, compute f(x + E)

f(x + E) = 6(x + E)(x + E) + 7(x + E)
= 6(x^2 + Ex + Ex + E^2) + 7x + 7E
= 6(x^2 + 2Ex) + 7x + 7E
= 6x^2 + 12Ex + 7x + 7E
= (6x^2 + 7x) + (12Ex + 7E)
= (6x^2 + 7x) + E(12x + 7)

The coefficient of the epsilon component is equal to the derivative of the function
