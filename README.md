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


p1.x=omega-(lambda*2);p1.y=alpha-lambda;
p2.x=omega-(lambda*2);p2.y=alpha-lambda;

draw_fill_rectangle(p1,p2,green);
lambda = lambda + omega/6;

}












wait_escape();
exit(0);

}
