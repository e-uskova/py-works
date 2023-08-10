N = 100;
L = 16;
% тыкаю носом в оптимум, не помогает :(
a = 3;
b = 4;
prob_c = 0.5;
prob_m = 0.1;
epoch_num = 100;

pop_bin = init_pop(N, L);
cur_pop = pop_bin;
pop_co = crossover(pop_bin, prob_c);
pop_m = mutation(pop_co, prob_m);
cur_pop = [cur_pop; pop_m];
[pop_sel, m, me] = selection(cur_pop, N, a, b);
min_ar = [m];
mean_ar = [me];
cur_pop = pop_sel;
for epoch = (2:epoch_num)
    pop_co = crossover(pop_bin, prob_c);
    pop_m = mutation(pop_co, prob_m);
    cur_pop = [cur_pop; pop_m];
    [pop_sel, m] = selection(cur_pop, N, a, b);
    min_ar = [min_ar m];
    mean_ar = [mean_ar me];
    cur_pop = pop_sel;
end
