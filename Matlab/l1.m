n = 4*pi;
t1 = pi*(-n:n)/n;
t2 = pi/2*(-n:n)'/n;
x = cos(t2)*cos(t1);
y = cos(t2)*sin(t1);

z = sin(t2);
plot3(x,y,z);