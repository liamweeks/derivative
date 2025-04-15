

class DualNumber:
    """
    The DualNumber class represents a Dual Number. It has a real number component and an epsilon component.
    The epsilon component, E, is a special number. E != 0 and E^2 = 0

    The cool thing about dual numbers is that if you want to evaluate a function, f(x) at x, you can compute f(x + E)
    and the epsilon number component is equal to the derivative of the function
    """

    def __init__(self, real, epsilon):
        self.real= real
        self.epsilon= epsilon


    def __add__(self, other):

        if isinstance(other, DualNumber):
            real = self.real + other.real
            ep = self.epsilon + other.epsilon
            return DualNumber(real, ep)
        return DualNumber(self.real + other, self.epsilon)
    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, DualNumber):
            real = self.real * other.real
            ep = (self.epsilon * other.real) + (self.real * other.epsilon) # FOIL but the (epsilon)^2 equals zero
            #result = DualNumber(real, ep)
            return DualNumber(real, ep)

        return DualNumber(self.real * other, self.epsilon * other)
    __rmul__ = __mul__



def differentiate(f, x):
    return f(DualNumber(x, 1)).epsilon


if __name__ == "__main__":

    def math_func(x):
        return 6 * (x * x) + (7 * x)

    x = 5

    y = math_func(x)

    derivative = differentiate(math_func, x)


    print(f"f({x}) = {y}, f'({x}) = {derivative}")
