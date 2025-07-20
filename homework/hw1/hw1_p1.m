% % hw1-p1-a
% f = @(x) x.^2;
% 
% a = 0; b1 = 2;
% x1 = 0.5; x2 = 1.5;
% 
% average = (f(x1) + f(x2))/2;
% 
% xi = fzero(@(x) f(x) - average, [x1, x2]);
% 
% figure;
% x = linspace(a,b1,100);
% plot(x, f(x), 'b-', x1, f(x1), 'ro', x2, f(x2), 'ro', xi, average, 'g*');
% legend('f(x)', 'f(x1)', 'f(x2)', 'f(\xi)');
% title('第一部分：等权重平均值');
% 
% 
% % hw1-p1-b
% clc; clear;
% f = @(x) x.^2;
% 
% a = 0; b1 = 2;
% c1 = 3; c2 = 7;
% x1 = 0.5; x2 = 1.5;
% 
% weighted_average = (c1*f(x1) + c2*f(x2))/(c1 + c2);
% 
% xi = fzero(@(x) f(x) - weighted_average, [x1, x2]);
% 
% figure;
% x = linspace(a,b1,100);
% plot(x, f(x), 'b-', x1, f(x1), 'ro', x2, f(x2), 'ro', xi, weighted_average, 'g*');
% legend('f(x)', 'f(x1)', 'f(x2)', 'f(\xi)');
% title('第二部分：正权重加权平均值');
% 
% 
% % hw1-p1-c
% clc; clear;
% f = @(x) x.^2;
% 
% a = 0; b1 = 2;
% c1 = 3; c2 = 7;
% x1 = 0.5; x2 = 1.5;
% 
% weighted_average = (c1*f(x1) + c2*f(x2))/(c1 + c2);
% 
% try
%     xi = fzero(@(x) f(x) - weighted_average, [x1, x2]);
%     figure;
%     x = linspace(a,b1,100);
%     plot(x, f(x), 'b-', x1, f(x1), 'ro', x2, f(x2), 'ro', xi, weighted_average, 'g*');
%     legend('f(x)', 'f(x1)', 'f(x2)', 'f(\xi)');
%     title('第三部分：权重相反加权平均值的反例');
%     disp(['解为：', num2str(xi)]);
% catch
%     disp('在区间内无解');
% end
% 
% 
% % hw1-p3-a
% a = 4/5 + 1/3;
% disp(a);
% 
% function y = chop3(x)
%     s = sprintf('%.2e', x);
%     y = str2double(s);
% end
% a2 = chop3(a);
% disp(a2);
% 
% function z = round3(x)
%     z = round(x, 3, 'significant');
% end
% a3 = round3(a);
% disp(a3);
% 
% 
% % hw1-p5-a
% clc; clear; close all;
% a = 0; b1 = 1;
% c = (a + b1)/2;
% count = 0;
% f = @(x) exp(x) - x^2 + 3*x - 2;
% margin = 1e-5;
% while abs(f(c)) >= margin
%     count = count + 1;
%     if f(c) == 0
%         fprintf('%d: %f\n', count, c);
%         break;
%     elseif f(a)*f(c) < 0
%         b1 = c;
%     else
%         a = c;
%     end
%     % disp(sprintf('%d: %f', count, c));
%     fprintf('%d: %f\n', count, c);
%     c = (a+b1)/2;
% end
% 
% % hw1-p5-b
% clc; clear; close all;
% a1 = 0.2; b1 = 0.3;
% c1 = (a1 + b1)/2;
% count = 0;
% f = @(x) x*cos(x) - 2*x^2 + 3*x - 1;
% margin = 1e-5;
% while abs(f(c1)) >= margin
%     if f(c1) == 0
%         break;
%     elseif f(a1)*f(c1) < 0
%         b1 = c1;
%     else
%         a1 = c1;
%     end
%     count = count + 1;
%     % disp(sprintf('%d: %f', count, c1));
%     fprintf('%d: %f\n', count, c1);
%     c1 = (a1+b1)/2;
% end
% fprintf('%d: %f\n', count + 1, c1);
% 
% a2 = 1.2; b2 = 1.3;
% c2 = (a2 + b2)/2;
% count = 0;
% f = @(x) x*cos(x) - 2*x^2 + 3*x - 1;
% margin = 1e-5;
% while abs(f(c2)) >= margin
%     if f(c2) == 0
%         break;
%     elseif f(a2)*f(c2) < 0
%         a2 = c2;
%     else
%         b2 = c2;
%     end
%     count = count + 1;
%     % disp(sprintf('%d: %f', count, c1));
%     fprintf('%d: %f\n', count, c2);
%     c2 = (a2+b2)/2;
% end
% fprintf('%d: %f\n', count + 1, c2);
% % 会出现 c = 1.200000无限循环。所以需要增加循环条件限制循环次数，如设置循环次数的上限，或限制 b - a 的大小。
% 
% 
% % hw1-p6-a
% clc; clear; close all;
% g = @(x) (2*sin(pi*x) + 4*x)/3;
% p = 1;
% n = 0;
% margin = 1e-2;
% disp('ERROR     g(p)         p');
% while abs(g(p) - p) >= margin && p <= 2
%     if g(p) - p == 0
%         break;
%     else
%         fprintf('%.6f  %.6f  %.6f\n', abs(g(p)-p), g(p), p);
%         p = g(p);
%         n = n + 1;
%     end
% end
% fprintf('%.6f  %.6f  %.6f\n', abs(g(p)-p), g(p), p);
% fprintf('Solution is %.6f.', g(p));
% 

% figure;
% x = [0:2];
% f = @(x) 3*x^2 - exp(x);
% fplot(f,[0 2]);

% hw1-p6-a
clc; clear; close all;
g = @(x) exp(x)/(3*x);
p = 0.6;
n = 0;
margin = 1e-2;
disp('ERROR     g(p)         p');
while abs(g(p) - p) >= margin && p <= 2
    if g(p) - p == 0
        break;
    else
        fprintf('%.6f  %.6f  %.6f\n', abs(g(p)-p), g(p), p);
        p = g(p);
        n = n + 1;
    end
end
fprintf('%.6f  %.6f  %.6f\n', abs(g(p)-p), g(p), p);
fprintf('Solution is %.6f.', g(p));