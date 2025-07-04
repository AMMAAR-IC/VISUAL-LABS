def predict(x, w, b):
    return w * x + b

def compute_cost(x, y, w, b):
    m = len(x)
    total_cost = 0.0
    for i in range(m):
        f_wb = predict(x[i], w, b)
        total_cost += (f_wb - y[i]) ** 2
    return total_cost / (2 * m)
