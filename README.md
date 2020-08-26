# Differential-equation-solver
Using Runge-Kuttah algorithm to solve a wide variety of differential equations


Numerical techniques are clever algorithms created by clever SCIENSTISTS to solve differnt topics in maths but this is just part of the story as this algorithms could go into complex loops where 
precision and accuracy are essential if we want results close to the ones from the classical analytical methods and that is what computers are all about solving stuff fast and in magical accuracy. So in this mini project I will use Python's Tkintrer library to implemnt such algorithm into living scripts.



bellow is a screen shot from the basic UI
![runge](https://user-images.githubusercontent.com/62334815/91313216-694d6c80-e7b5-11ea-9c04-3f43935dbfdf.PNG)

the follwing script is capable to solve three types of DE numerically 
given for example the following DE y'= xy + x^2  with inital conditions x0 = 0 and y0 = 1. We input the x-variable we need its y-variable this way:
for this example we will be checking the y fo x-value= 0.1 then click execute

![e1](https://user-images.githubusercontent.com/62334815/91315018-753a2e00-e7b7-11ea-8d91-5253ae59c93c.PNG)

the same thing goes with cases 2 and 3 
<h2> IMPORTANT NOTES </h2>
F(x,y) in case 1 is the y' being the subject of the DE <br>
f(x,y,z) in case 2 is the y'' being the subject of the DE and z being y' and z0 is y' intial comdition.<br>
Case 3 is solving two DE where Y' is the first and Z' is the second<br>
