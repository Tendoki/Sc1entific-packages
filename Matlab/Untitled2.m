clear
t = -5:0.01:5;
a = 1/4;
b = 1/16;
m = 8;
n = 8;
k = 1;
x = cos(t)-a.*cos(m.*t)+b.*sin(n.*t);
y = sin(t)+a.*sin(m.*t)+b.*cos(n.*t);
for k = 1:1:10
    plot(x./k,y./k)
    hold on
end
hold off