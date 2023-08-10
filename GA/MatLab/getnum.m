function num = getnum(pop, a, b)
% приводим бинарный вид в десятичный
two = 2;
N = size(pop, 2);
tpl = (N - 1:-1:0);
pow = two.^tpl .* pop;
x1 = sum(pow, 2);
num = a + x1 * (b - a)/(2 ^ N - 1);
num = [num(:, :, 1) num(:, :, 2)];
end