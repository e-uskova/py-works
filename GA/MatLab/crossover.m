function res = crossover(pop, prob_c)
% оператор кроссинговера
% с вероятностью prob_c скрещиваем соседние хромосомы
len = size(pop, 1);
res = pop;
for i = (1:2:len)
    if rand <= prob_c
        k = randi(size(pop, 2) - 1,  1);
        %tmp1 = pop(i, 1:k, :);
        %disp(k);
        %disp(tmp1);
        %tmp2 = pop(i + 1, 1:k, :);
        %disp(tmp2);
        res(i, 1:k, :) = pop(i + 1, 1:k, :);
        res(i + 1, 1:k, :) = pop(i, 1:k, :);
    end
end    
end
