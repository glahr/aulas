function A = aliasing_gustavo()
f = 10;
T = 1/f;
Tmax = 5*T;
t = 0:T/100:Tmax;
phi = 0;
% ref
for ii=1:length(t)
    y(ii) = seno(t(ii), f, phi);
end

f_12 = 12;
T_12 = 1/f_12;
t_12 = 0:T_12:Tmax;
for ii=1:length(t_12)
    y_12(ii) = seno(t_12(ii), f, phi);
end

f_10 = 10;
T_10 = 1/f_10;
t_10 = 0:T_10:Tmax;
for ii=1:length(t_10)
    y_10(ii) = seno(t_10(ii), f,pi/10);
end

f_20 = 100;
T_20 = 1/f_20;
t_20 = 0:T_20:Tmax;
for ii=1:length(t_20)
    y_20(ii) = seno(t_20(ii), f,0);
end

plot(t,y, '-', t_10, y_10, 'r', t_12, y_12, 'g', t_20, y_20, 'k')
grid on
legend('ref','10 Hz','12 Hz', '20 Hz')
end

function y = seno(t, f,phi)
y = sin(2*pi*f*t + phi) + 0.5*sin(2*pi*2*f*t + phi);
end