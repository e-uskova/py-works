function [population] = init_pop(N, L)
% инициализация популяции
% случайным образом создаём N особей с L аллелями в хромосоме
population = randi([0, 1], [N, L, 2]);
end
