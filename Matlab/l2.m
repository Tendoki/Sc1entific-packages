clear all
t = -5*pi:pi/250:5*pi;
x = (cos(2*t).^2).*sin(t);
y = (sin(2*t).^2).*cos(t);
comet3(x,y,t);