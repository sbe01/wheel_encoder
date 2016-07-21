import svgwrite
from svgwrite import *

encoder_radius = 15.0
cut_begin_radius = 8.0
cut_end_radius = 14.0
cut_width = 0.5
increments = 60.0
stroke_width = 0.001 # Zing Lasercutter needs 0.001 inch
cut_height = cut_end_radius-cut_begin_radius

dwg = svgwrite.Drawing('wheel_encoder.svg', profile='tiny')
# outer circle
dwg.add(svgwrite.shapes.Circle(center=(0.0, 0.0), r=encoder_radius*mm,
                               stroke='black', stroke_width=stroke_width*inch, fill='white'))
# increment cuts
step = 0.0
while(step < 360.0):
  cut = dwg.rect(insert=(-cut_width/2.0*mm, -cut_end_radius*mm), size=(cut_width*mm, cut_height*mm),
                 stroke='black', stroke_width=stroke_width*inch, fill='white')
  cut.rotate(step, center=(0.0, 0.0))
  dwg.add(cut)
  step += 360.0/increments

# lego axle, here the basic components for a lego axle are only generated. svgwrite can not combine them to actually make the axle-hole
# I did that manually in inkscape afterwards.
axle_radius = 2.4
axle_tooth_height = 1.6
axle_tooth_width = 2.5*axle_radius
dwg.add(svgwrite.shapes.Circle(center=(0.0, 0.0), r=axle_radius*mm,
                               stroke='black', stroke_width=stroke_width*inch, fill='white'))
axle = dwg.rect(insert=(-axle_tooth_width/2.0*mm, -axle_tooth_height/2.0*mm), size=(axle_tooth_width*mm, axle_tooth_height*mm),
  stroke='black', stroke_width=stroke_width*inch, fill='white')
dwg.add(axle)
axle2 = dwg.rect(insert=(-axle_tooth_width/2.0*mm, -axle_tooth_height/2.0*mm), size=(axle_tooth_width*mm, axle_tooth_height*mm),
  stroke='black', stroke_width=stroke_width*inch, fill='white')
axle2.rotate(90)
dwg.add(axle2)

dwg.save()
