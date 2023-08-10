function [pop] = fit(pop)
% фитнесс-функция
pop(:, 3) = - cos(pop(:, 1)) .* cos(pop(:, 2)) .* exp(-((pop(:, 1) - pi) .^ 2 + (pop(:, 2) - pi) .^ 2));
end



