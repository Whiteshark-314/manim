#!/usr/bin/env python

from manim import *

class FirstScene(Scene):
    def construct(self):
        def mov_up(x,y,z,t):
            return [x, y + 4*t, z]
        obj1=Paragraph("Newton's","Second Law","of Motion", font="TimesNewRoman").scale(1.5)
        obj2=Paragraph("In an inertial frame of reference,",
                        "the vector sum of Forces on a body",
                        "is directly proportional to",
                        "it's rate of change of momentum",font="TimesNewRoman")
        obj3=TexMobject("\\vec { F }"," \\propto",
                        " { m\\vec { v } -m\\vec { u } \\over \Delta t } ").scale(1.5)
        obj4=TextMobject("As $\\Delta t$ becomes infinitesimal").scale(0.8).move_to(np.array([0,3,0]))
        obj5=TexMobject("\\vec { F }"," \\propto",
                        " { d \\over dt } (m\\vec { v } )").scale(1.5)
        obj6=TextMobject("Introducing a proportionality constant $k$").scale(0.8).move_to(np.array([0,3,0]))
        obj7=TexMobject("\\vec { F }","=",
                        " k{ d \\over dt } (m\\vec { v } )").scale(1.5)
        obj8=TextMobject("Using Chain Rule of Differentiation").scale(0.8).move_to(np.array([0,3,0]))
        obj9=TexMobject("\\vec{ F }","=",
                        " k\\left( m { d\\vec { v } \\over dt } +\\vec { v }",
                        "{ dm \\over dt }","  \\right) ").scale(1.5)
        obj10=TextMobject("As common objects neither gain nor lose mass").scale(0.8).move_to(np.array([0,3,0]))
        obj11=Cross(obj9[3],TexMobject("0")).move_to(np.array([2.5,0.5,0]))
        obj12=TexMobject("\\vec{ F }","=",
                        " k\\left( m\\frac { d\\vec { v }  }{ dt }\\right) ").scale(1.5)
        obj13=TextMobject("Rate of change of velocity is acceleration").scale(0.8).move_to(np.array([0,3,0]))
        obj14=TexMobject("\\vec{ F }","="," k m \\vec{a}").scale(1.5)
        obj15=Paragraph("Choosing an appropriate","unit of measurement for Force",
                        "1 Newton is defined as","the amount of force required",
                        "to accelerate a mass of 1 kg",
                        "at the rate of 1 m/s^2", font="TimesNewRoman").scale(0.8)
        obj15[0:2].move_to(np.array([0,3,0]))
        obj15[2:].move_to(np.array([0,3,0]))
        obj16=TextMobject("This choice of unit of measurement makes\n"," $k = 1$").scale(0.8)
        obj16[0].move_to(np.array([0,3,0]))
        obj16[1].move_to(np.array([0,2,0]))
        obj17=TexMobject("\\vec{ F }","=","m \\vec{a}").scale(1.5)
        obj18=SurroundingRectangle(obj17, color="WHITE").scale(1.2)
        self.play(Write(obj1))
        self.wait(2)
        self.play(*[Homotopy(mov_up,obj1)])
        self.play(Write(obj2))
        self.wait(4)
        self.play(FadeOut(obj1))
        self.play(Transform(obj2,obj3))
        self.wait(2)
        self.play(FadeIn(obj4))
        self.wait(2)
        self.play(Transform(obj2,obj5))
        self.wait(2)
        self.play(FadeOut(obj4))
        self.wait()
        self.play(FadeIn(obj6))
        self.wait(2)
        self.play(Transform(obj2,obj7))
        self.wait(2)
        self.play(FadeOut(obj6))
        self.wait()
        self.play(FadeIn(obj8))
        self.wait(2)
        self.play(Transform(obj2,obj9))
        self.wait(2)
        self.play(FadeOut(obj8))
        self.wait()
        self.play(FadeIn(obj10))
        self.wait()
        self.play(FadeToColor(obj9[3],RED))
        self.play(ShowCreation(obj11))
        self.wait(2)
        self.play(FadeOut(obj10))
        self.wait()
        self.remove(obj11)
        self.remove(obj9[3])
        self.play(Transform(obj2,obj12))
        self.wait()
        self.play(FadeIn(obj13))
        self.wait(2)
        self.play(Transform(obj2,obj14))
        self.wait(2)
        self.play(FadeOut(obj13))
        self.wait()
        self.play(FadeIn(obj15[0:2]))
        self.wait(2)
        self.play(FadeOut(obj15[0:2]))
        self.wait()
        self.play(Write(obj15[2:]))
        self.wait(4)
        self.play(FadeOut(obj15[2:]))
        self.wait()
        self.play(Write(obj16))
        self.wait(2)
        self.play(Transform(obj2,obj17))
        self.wait(2)
        self.play(FadeOut(obj16))
        self.wait()
        self.play(ShowCreation(obj18))
        self.wait(5)
        self.play(FadeOut(obj18))
        self.play(FadeOut(obj2))
        self.clear()

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(ShowCreation(grid, run_time=2, lag_ratio=0.1),)
        matrix_1=Matrix([["a","b"],["c","d"]]).move_to(4*UP+2.7*LEFT).set_color(RED_B)
        mult=TexMobject("\\times").move_to(4*UP+0.5*LEFT).set_color(RED_B)
        matrix_2=Matrix([1,1]).move_to(4*UP+0.6*RIGHT).set_color(RED_B)
        equal=TexMobject("=").move_to(4*UP+1.6*RIGHT).set_color(RED_B)
        matrix_3=Matrix([1,1]).move_to(4*UP+3.2*RIGHT).set_color(RED_B)
        eqn=VGroup(matrix_1,mult,matrix_2,equal,matrix_3)
        eqn.bg=BackgroundRectangle(eqn,fill_opacity=0.5)
        eQn=VGroup(eqn.bg,eqn)
        self.play(Write(eQn))
        self.play(FadeToColor(matrix_1,WHITE))
        self.wait(10)

class What_is_RM(Scene):
    def construct(self):
        ques=Paragraph("What is a"," Rotation Matrix?",font="TimesNewRoman").scale(1.5)
        text_1=Paragraph("Let's start","with a","planar case",font="TimesNewRoman")
        grid = NumberPlane()
        text_2=Paragraph("As the name suggests,",
                        "Rotation Matrices are Matrices",
                        "that somehow have encoded in them",
                        "the act of Rotation",font="TimesNewRoman")
        text_3=Paragraph("So...",
                        "Are all matrices Rotation Matrices?",
                        "Or are they special in some way?",font="TimesNewRoman")
        text_3[2].move_to(ORIGIN)
        text_4=Paragraph("Let's consider a",
                        "2 x 1 Vector....", font="TimesNewRoman")
        vector_1=Matrix([1, 1])
        vector_1_copy=Matrix([1, 1]).move_to(2*UR)
        text_5=Paragraph("Multiplying this vector with",
                        "different 2 x 2 Matrices","changes the vector",
                        font="TimesNewRoman")
        text_5.bg=BackgroundRectangle(text_5)
        teXt_5=VGroup(text_5.bg,text_5).move_to(4*DOWN)


        mat_blank=Matrix([["a","b"],["c","d"]]).move_to(4*UP+2.7*LEFT).set_color(RED_B)
        mult=TexMobject("\\times").move_to(4*UP+0.5*LEFT).set_color(RED_B)
        vector_1_f=Matrix([1, 1]).move_to(4*UP+0.6*RIGHT).set_color(RED_B)
        equal=TexMobject("=").move_to(4*UP+1.6*RIGHT).set_color(RED_B)
        vector_out=Matrix(["e","f"]).move_to(4*UP+3.2*RIGHT).set_color(RED_B)
        trsfm=VGroup(mat_blank,mult,vector_1_f,equal,vector_out)
        trsfm.bg=BackgroundRectangle(trsfm,fill_opacity=0.5)
        tRsfm=VGroup(trsfm.bg,trsfm)


        mat1=np.array([[3,0],[0,3]])
        mat2=np.array([[0,-0.8],[-0.8,0]])
        mat3=np.array([[-2.7,0],[0,-2.7]])
        mat4=np.array([[0,1.5],[1.5,0]])
        mat5=np.array([[2.5,-3.5],[-3.5,2.5]])
        vec1=np.array([[1/np.sqrt(2)],[1/np.sqrt(2)]])
        text_6=Paragraph("It can be observed that",
                        "whenever the principal or","secondary diagonal elements",
                        "have same value and sign","the vector stretches",
                        "or squishes proportional","to the value",
                        font="TimesNewRoman")
        text_6.bg=BackgroundRectangle(text_6)
        teXt_6=VGroup(text_6.bg,text_6).move_to(4*DOWN)

        text_7=Paragraph("Positive sign indicates",
                        "that the stretch occurs","in the direction of the original vector",
                        "Negative sign indicates","an extra 180^\\circ rotation",
                        "along with the stretching",font="TimesNewRoman")
        text_7.bg=BackgroundRectangle(text_7)
        teXt_7=VGroup(text_7.bg,text_7).move_to(4*DOWN)

        text_8=Paragraph("If the sum of values of the 1^st",
                        "column of the matrix is","greater than the 2^nd,",
                        "the vector rotates clockwise","along with streaching",
                        "and anti-clockwise when","sum of values of the 2^nd",
                        "column of the matrix is","greater than the 1^st,",font="TimesNewRoman")
        text_8.bg=BackgroundRectangle(text_8)
        teXt_8=VGroup(text_8.bg,text_8).move_to(4*DOWN)

        text_9=Paragraph("Rotation Matrix is a matrix which",
                        "only rotates the vector without changing it's length",font="TimesNewRoman")
        text_9.bg=BackgroundRectangle(text_9)
        teXt_9=VGroup(text_9.bg,text_9).move_to(4*DOWN)
        #mat1=Matrix([[][]])
        text_x=Paragraph("1) Represent an Orientation",
                        "2) Change reference frame",
                        "3) Rotate a vector or frame",font="TimesNewRoman",alignment="left")
        text_x1=Paragraph("1) Represent an Orientation",
                        "2) Change reference frame",
                        "3) Rotate a vector or frame",font="TimesNewRoman",alignment="left").to_edge(DL)
        vector=Vector(direction=np.array((1/np.sqrt(2),1/np.sqrt(2),0)))

        self.play(Write(ques))
        self.wait(3)
        self.play(Transform(ques,text_1))
        self.wait(3)
        self.play(
            FadeOut(ques),
            ShowCreation(grid, run_time=2, lag_ratio=0.1),
        )
        self.play(FadeOut(grid))
        self.wait()
        self.play(Write(text_2))
        self.wait(5)
        self.play(Transform(text_2,text_3[0:2]))
        self.wait(5)
        self.play(Transform(text_2,text_3[2]))
        self.wait(2)
        self.play(FadeOut(text_2))
        self.wait()
        self.play(Write(text_4))
        self.wait(5)
        self.play(FadeOut(text_4))
        self.play(ShowCreation(grid, run_time=4, lag_ratio=0.1),)
        self.play(Write(vector_1))
        self.play(Transform(vector_1,vector_1_copy))
        self.play(ShowCreation(vector))
        self.play(Write(teXt_5))
        self.wait(5)
        self.play(FadeOut(teXt_5),ReplacementTransform(vector_1,tRsfm))
        self.wait(2)
        self.play(Write(teXt_6))
        self.wait(10)
        self.play(FadeOut(teXt_6))
        self.wait(2)
        for mat in mat1,mat2,mat3,mat4,mat5:
            #new_vec=np.vstack([np.dot(mat,vec1),[0]])
            new_vec=np.around(np.append(np.dot(mat,vec1),[0]),decimals=1)
            temp_vector=Vector(direction=new_vec).set_color(BLUE_C)
            temp_mat=Matrix([[mat[0][0], mat[0][1]],[mat[1][0],mat[1][1]]]).move_to(4*UP+2.7*LEFT).set_color(RED_B)
            temp_vec_out=Matrix([new_vec[0],new_vec[1]]).move_to(4*UP+3.2*RIGHT).set_color(BLUE_C)
            self.play(ReplacementTransform(vector,temp_vector),
                    ReplacementTransform(mat_blank,temp_mat),
                    ReplacementTransform(vector_out,temp_vec_out))
            vector=Vector(direction=np.array((1/np.sqrt(2),1/np.sqrt(2),0)))
            mat_blank=Matrix([["a","b"],["c","d"]]).move_to(4*UP+2.7*LEFT).set_color(RED_B)
            vector_out=Matrix(["e","f"]).move_to(4*UP+3.2*RIGHT).set_color(RED_B)
            self.wait(5)
            self.play(ReplacementTransform(temp_vector,vector),
                    ReplacementTransform(temp_mat,mat_blank),
                    ReplacementTransform(temp_vec_out,vector_out))
            self.wait(3)
        #for mat in
        #self.play()
        self.play(Write(text_x))
        self.wait(3)
        self.play(Transform(text_x,text_x1))
        self.wait(3)

class ValueTrackerWithColor(Scene):
    def construct(self):
        gradient_rectangle = Rectangle(
                                    width=FRAME_WIDTH-1,
                                    height=1,
                                    fill_opacity=1,
                                    # Gradient direction
                                    sheen_direction=RIGHT,
                                    stroke_width=0
                                    )
        square = Square(fill_opacity=1)
        square.to_edge(UP,buff=1)
        gradient_rectangle.to_edge(DOWN,buff=1)

        gradient_rectangle.set_color(color=self.get_hsl_set_colors())

        color_tracker = ValueTracker(0)

        color_label = Integer(color_tracker.get_value(),unit="^\\circ").set_color(BLACK)
        color_label.add_updater(lambda v: v.set_value(color_tracker.get_value()).next_to(square,ORIGIN))

        square.add_updater(lambda s: s.set_color(HSL(color_tracker.get_value()/360)))

        line_color = Line(
                        gradient_rectangle.get_corner(UL),
                        gradient_rectangle.get_corner(UR)
                        )
        arrow = Arrow(LEFT,RIGHT)
        arrow.add_updater(lambda a: a.put_start_and_end_on(square.get_bottom()+DOWN*0.3,line_color.point_from_proportion(color_tracker.get_value()/360)))

        self.add(gradient_rectangle,square,color_label,arrow)
        self.wait(3)
        self.play(
            color_tracker.set_value,360,
            rate_func=double_linear,
            run_time=20,
            )
        self.wait(3)

    def get_hsl_set_colors(self,saturation=1,lightness=0.5):
        return [*[HSL(i/360,saturation,lightness) for i in range(360)]]

def HSL(hue,saturation=1,lightness=0.5):
    return Color(hsl=(hue,saturation,lightness))

def double_linear(t):
    if t < 0.5:
        return linear(t*2)
    else:
        return linear(1-(t-0.5)*2)
