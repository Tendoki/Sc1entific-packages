F = @(x,y)(x.^2+y.^2).^2
fsurf(F,[-pi,pi,-pi,pi])
fx = @(u,v)u.*cos(v);
fy = @(u,v)u.*sin(v);
fz = @(u,v)u.^4;
fsurf(fx,fy,fz, [-pi,pi,-pi,pi])