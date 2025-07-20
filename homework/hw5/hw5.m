% hw5-p5-a
f = @(t, y) (y/t - (y/t)^2);
function result = myfunc(f, a, b, h)
    n = (b - a) / h;
    t = a;
    result = 1;
    for i = 1:(n - 1)
        result = result + h * f(t, result);
        t = t + h;
    end