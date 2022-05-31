x = linspace(-2,0,20)
[X,Y]= meshgrid(x,-x);
Z = 2./exp((X-.5).^2+Y.^2)-2./exp((X+0.5).^2+Y.^2)
subplot(2,2,1)
surf(X,Y,Z);
shading faceted;
title('shading faceted')
subplot(2,2,2)
surf(X,Y,Z);
shading flat;
title('shading flat')
subplot(2,2,3)
surf(X,Y,Z);
shading interp;
title('shading interp')