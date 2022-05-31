x = -10:0.5:10;
y = -10:0.5:10;
[X,Y] = meshgrid(x,y);
Z = sin(sqrt(X.^2+Y.^2))./sqrt(sqrt(X.^2+Y.^2));
surfc(X,Y,Z)
xlabel('x')
ylabel('y')
zlabel('z')