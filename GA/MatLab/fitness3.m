function y = fitness3(x)
y = - cos(x(1)) * cos(x(2)) * cos(x(3))* exp(-((x(1) - pi) ^ 2 + (x(2) - pi) ^ 2 + (x(3) - pi) ^ 2));
end