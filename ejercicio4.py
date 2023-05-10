import math

def f(x):
    return x**3 + x + 16

def df(x):
    return 3*x**2 + 1

def metodo_biseccion(a, b, tol, max_iter):
    iteraciones = 0
    while iteraciones < max_iter:
        c = (a + b) / 2
        if f(c) == 0 or abs(b - a) < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iteraciones += 1
    return c, iteraciones

def metodo_secante(x0, x1, tol, max_iter):
    iteraciones = 0
    while iteraciones < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            break
        x0 = x1
        x1 = x2
        iteraciones += 1
    return x2, iteraciones

def metodo_newton_raphson(x0, tol, max_iter):
    iteraciones = 0
    while iteraciones < max_iter:
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
        iteraciones += 1
    return x1, iteraciones

a, b = -5, 5
tol = 1e-6
max_iter = 1000

solucion_biseccion, iter_biseccion = metodo_biseccion(a, b, tol, max_iter)
solucion_secante, iter_secante = metodo_secante(a, b, tol, max_iter)
solucion_newton_raphson, iter_newton_raphson = metodo_newton_raphson(a, tol, max_iter)

print("Método Secante: Solución = {:.6f}, Iteraciones = {}".format(solucion_secante, iter_secante))
print("Método Bisección: Solución = {:.6f}, Iteraciones = {}".format(solucion_biseccion, iter_biseccion))
print("Método Newton-Raphson: Solución = {:.6f}, Iteraciones = {}".format(solucion_newton_raphson, iter_newton_raphson))
