def gradient(f, x, h=1e-5): 
    if isinstance(x, (int, float)):
        return (f(x + h) - f(x - h)) / (2 * h)
    
    grad = []
    for i in range(len(x)):
        x_plus = x[:]
        x_minus = x[:]
        x_plus[i] += h
        x_minus[i] -= h
        partial = (f(x_plus) - f(x_minus)) / (2 * h)
        grad.append(partial)
    return grad
