int main()
{
int omega = 600;
int alpha = 600;

init_graphics(omega,alpha);

POINT p1;
POINT p2;
int lambda = 0;

while(lambda <=omega)
{


p1.x=lambda;p1.y=lambda;
p2.y=lambda;p2.y=lambda;

draw_line(p1,p2,green);
lambda = lambda + omega/6;

}












wait_escape();
exit(0);

}
