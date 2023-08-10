function res = mutation(pop, prob_m)
% оператор мутации
% с вероятностью prob_m меняем случайный аллель
len = size(pop, 1);
res = pop;
for i = (1:len)
    if rand <= prob_m
        k = randi(size(pop, 2),  1);
        %disp(k);
        res(i, k, :) = inv(res(i, k, :));
        % y почему-то не изменяется
    end
end  
end

function res = inv(n)
%disp(n);
if n == 1
    res = 0;
else 
    res = 1;
end
end

