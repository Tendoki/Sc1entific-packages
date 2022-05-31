[X,Y] = meshgrid(-1:.1:1,-1:.1:1);
Z = sin(X).*cos(Y)
contour(X,Y,Z,10)