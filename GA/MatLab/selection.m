function [res, min_fit, mean_fit] = selection(pop_bin, N, a, b)
% оператор селекции
% выбираем N особей с наименьшим значением фитнесс-функции
pop = getnum(pop_bin, a, b);
fit_pop = fit(pop);
pop_bin = [pop_bin(:, :, 1) pop_bin(:, :, 2)];
pop_bin(:, size(pop_bin, 2) + 1) = fit_pop(:, 3);
tmp = sortrows(pop_bin, 3);
res = tmp(:, 1:floor(size(tmp, 2) / 2));
res(:, :, 2) = tmp(:, floor(size(tmp, 2) / 2) + 1:size(tmp, 2) - 1);
res = res(1:N, :, :);
min_fit = fit_pop(1, 3);
mean_fit = mean(fit_pop(1, 3));
end
