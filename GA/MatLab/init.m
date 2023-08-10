function [population] = init_pop(N, a, b)
population = a + (b-a).*rand(2, N);
end
